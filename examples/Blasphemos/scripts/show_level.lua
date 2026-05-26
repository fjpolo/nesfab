-- ==============================================================================
-- show_level.lua — Real-time level and game state visualizer for Blasphemos (NES)
-- Targets: Mesen & Fceux
-- ==============================================================================

-- Polyfill for Mesen and other emulators that do not have global 'memory' object
if not memory and emu then
    memory = {}
    memory.readbyte = function(addr)
        local memType = 0
        if emu.memType then
            memType = emu.memType.nesMemory or emu.memType.cpu or 0
        end
        return emu.read(addr, memType)
    end
end

-- Level names dictionary mapping index -> exact mapfab level key
local LEVEL_NAMES = {
    [0]  = "title",
    [1]  = "l1",
    [2]  = "l2",
    [3]  = "l2b",
    [4]  = "l3",
    [5]  = "l3b",
    [6]  = "l4",
    [7]  = "l4sub1",
    [8]  = "l5",
    [9]  = "l6",
    [10] = "l6b",
    [11] = "l7",
    [12] = "l7over1",
    [13] = "l8",
    [14] = "l9",
    [15] = "l10",
    [16] = "l9sub1",
    [17] = "l9over1",
    [18] = "l9over2",
    [19] = "l10sub1",
    [20] = "l8over1",
    [21] = "l11",
    [22] = "l11sub1",
    [23] = "l12",
    [24] = "l11sub1left1",
    [25] = "l11sub2",
    [26] = "l11sub3",
    [27] = "l11sub3left1",
    [28] = "game_over"
}

-- Game States mapping
local GAME_STATES = {
    [1]  = "Title Screen",
    [2]  = "Gameplay",
    [3]  = "Victory (Win Screen)",
    [4]  = "Map Screen",
    [5]  = "Dead Screen",
    [6]  = "Mea Culpa Altar",
    [63] = "Game Over"
}

-- Dynamic address resolver (tries MLB files first, then ram_variables.txt, then fallbacks)
local function get_address(var_name, fallback)
    local search_paths = {
        -- MLB Paths (best for Zero Page overlaid variables like current_level_index)
        { "BlasNESmous.mlb", "mlb" },
        { "BlasNESmous_dev.mlb", "mlb" },
        { "../BlasNESmous.mlb", "mlb" },
        { "../BlasNESmous_dev.mlb", "mlb" },
        { "scripts/BlasNESmous.mlb", "mlb" },
        { "scripts/BlasNESmous_dev.mlb", "mlb" },
        { "examples/Blasphemos/BlasNESmous.mlb", "mlb" },
        { "examples/Blasphemos/BlasNESmous_dev.mlb", "mlb" },
        -- RAM variables paths
        { "analysis/ram_variables.txt", "txt" },
        { "../analysis/ram_variables.txt", "txt" },
        { "scripts/analysis/ram_variables.txt", "txt" },
        { "examples/Blasphemos/analysis/ram_variables.txt", "txt" }
    }

    for _, entry in ipairs(search_paths) do
        local path = entry[1]
        local file_type = entry[2]
        local file = io.open(path, "r")
        if file then
            if file_type == "mlb" then
                for line in file:lines() do
                    if line:sub(1, 2) == "R:" then
                        local parts = {}
                        for part in line:gmatch("[^:]+") do
                            table.insert(parts, part)
                        end
                        if #parts >= 3 then
                            local addr_hex = parts[2]
                            local vars_str = parts[3]
                            -- Precise word-boundary match for var_name (avoiding partial substring matches)
                            local start_idx, end_idx = vars_str:find(var_name, 1, true)
                            if start_idx then
                                local before = start_idx > 1 and vars_str:sub(start_idx - 1, start_idx - 1) or ""
                                local after = end_idx < #vars_str and vars_str:sub(end_idx + 1, end_idx + 1) or ""
                                if not before:match("[%w_]") and not after:match("[%w_]") then
                                    file:close()
                                    local addr = tonumber(addr_hex, 16)
                                    if addr then
                                        print(string.format("[Level Script] Found '%s' in %s at: 0x%04X", var_name, path, addr))
                                        return addr
                                    end
                                end
                            end
                        end
                    end
                end
            elseif file_type == "txt" then
                for line in file:lines() do
                    local name, addr_hex = line:match("^([%w_]+)%s+%d+%s+%$(%x+)")
                    if name == var_name then
                        file:close()
                        local addr = tonumber(addr_hex, 16)
                        if addr then
                            print(string.format("[Level Script] Found '%s' in %s at: 0x%04X", var_name, path, addr))
                            return addr
                        end
                    end
                end
            end
            file:close()
        end
    end

    print(string.format("[Level Script] Warning: '%s' not found. Using fallback address: 0x%04X", var_name, fallback))
    return fallback
end

-- Resolve addresses dynamically
local ADDR_LEVEL_INDEX = get_address("current_level_index", 0x0013)
local ADDR_GAME_STATE  = get_address("game_state", 0x0219)
local ADDR_FRAME       = get_address("frame_counter", 0x0272)

-- Tracking previous states for logging changes to console
local prev_level = -1
local prev_state = -1

local function draw_level_info()
    -- Read RAM values safely
    local level_idx = memory.readbyte(ADDR_LEVEL_INDEX)
    local state_val = memory.readbyte(ADDR_GAME_STATE)
    local frame_val = memory.readbyte(ADDR_FRAME)

    -- Map level and state to strings
    local level_name = LEVEL_NAMES[level_idx] or string.format("Unknown (%d)", level_idx)
    local state_name = GAME_STATES[state_val] or string.format("Unknown (%d)", state_val)

    -- Detect and log changes to emulator console
    if level_idx ~= prev_level or state_val ~= prev_state then
        print(string.format("[LEVEL TRANSITION] Frame: %d | State: %s | Level: [%d] %s", 
            frame_val, state_name, level_idx, level_name))
        prev_level = level_idx
        prev_state = state_val
    end

    -- Construct simple text overlay string
    local text = "Level: " .. level_name

    -- Simple overlay (same way as FPS script)
    if emu and emu.drawString then
        -- Mesen API (Green text, transparent background)
        emu.drawString(10, 48, text, 0x00FF00)
    elseif gui and gui.text then
        -- Fceux API (Standard green text)
        gui.text(10, 48, text)
    end
end

-- Register callbacks based on emulator environment
if emu and emu.addEventCallback then
    -- Mesen Event Model
    emu.addEventCallback(draw_level_info, emu.eventType.endFrame)
    emu.log("[Level Script] show_level.lua loaded. Watching level and room state...")
else
    -- Fceux Execution Loop Model
    print("[Level Script] show_level.lua loaded (Fceux compatibility mode).")
    while true do
        draw_level_info()
        emu.frameadvance()
    end
end
