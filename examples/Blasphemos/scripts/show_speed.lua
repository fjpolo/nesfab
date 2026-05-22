-- Lua script for Mesen / Fceux to display player speed and coordinates in real-time.

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

-- Helper to dynamically find variable addresses from ram_variables.txt
function get_var_address(var_name, fallback)
    local paths = {
        "analysis/ram_variables.txt",
        "C:\\Workspace\\nesfab\\nesfab\\examples\\Blasphemos\\analysis\\ram_variables.txt",
        "c:\\Workspace\\nesfab\\nesfab\\examples\\Blasphemos\\analysis\\ram_variables.txt"
    }
    for _, path in ipairs(paths) do
        local file = io.open(path, "r")
        if file then
            for line in file:lines() do
                local name, addr_hex = line:match("^([%w_]+)%s+%d+%s+%$(%x+)")
                if name == var_name then
                    file:close()
                    local addr = tonumber(addr_hex, 16)
                    print(string.format("[Speed Script] Found %s at address: 0x%04X", var_name, addr))
                    return addr
                end
            end
            file:close()
        end
    end
    print(string.format("[Speed Script] Warning: Could not find %s in ram_variables.txt, using fallback: 0x%04X", var_name, fallback))
    return fallback
end

-- Resolve player base address dynamically
local ADDR_P_BASE = get_var_address("p", 0x023A)

-- Calculate dynamic absolute addresses based on struct layout offsets
local ADDR_PX = ADDR_P_BASE + 0     -- Offset 0: player world x (s16)
local ADDR_PY = ADDR_P_BASE + 3     -- Offset 3: player world y (s16)
local ADDR_CAMX = ADDR_P_BASE + 33   -- Offset 33: camera x (s16)

function read_s16(addr)
    local low = memory.readbyte(addr)
    local high = memory.readbyte(addr + 1)
    local val = low + high * 256
    if val >= 32768 then
        val = val - 65536
    end
    return val
end

local prev_px = nil
local current_speed = 0.0
local frame_count = 0

function draw_status()
    -- Player coordinates read dynamically
    local px = read_s16(ADDR_PX)
    local py = read_s16(ADDR_PY)
    
    -- Camera coordinate read dynamically
    local cam_x = read_s16(ADDR_CAMX)
    
    -- Calculate speed based on frame-by-frame delta
    if prev_px ~= nil then
        current_speed = math.abs(px - prev_px)
    end
    prev_px = px
    
    -- Status info text
    local text = string.format("Player X: %d | Y: %d\nSpeed: %.1f px/frame\nCamera X: %d", px, py, current_speed, cam_x)
    
    -- 1. Output to emulator console every 60 frames to avoid flooding
    frame_count = frame_count + 1
    if frame_count % 60 == 0 then
        print("--- Player Status ---")
        print(text)
    end

    -- 2. Draw info block at the top center of the screen
    if emu.drawString then
        -- Mesen API (Yellow text with black background card)
        emu.drawString(10, 48, text, 0xFFFFFF, 0xFF000000)
    elseif gui.text then
        -- Fceux API
        gui.text(10, 48, text)
    end

    -- 3. Draw speed overlay directly above the player's head!
    local screen_x = px - cam_x
    local screen_y = py
    
    -- Check if player is on screen
    if screen_x >= -32 and screen_x <= 288 and screen_y >= -32 and screen_y <= 240 then
        local player_speed_text = string.format("%.1f px/f", current_speed)
        
        -- Offset coordinates to be centered above player's head
        local draw_x = screen_x - 12
        local draw_y = screen_y - 12
        
        if emu.drawString then
            -- Yellow text with black box background for perfect visibility
            emu.drawString(draw_x, draw_y, player_speed_text, 0x00FFFF, 0xFF000000)
        elseif gui.text then
            gui.text(draw_x, draw_y, player_speed_text)
        end
    end
end

-- Polyfill for execution loop: Mesen vs Fceux
if emu and emu.addEventCallback then
    -- Mesen callback model
    emu.addEventCallback(draw_status, emu.eventType.endFrame)
else
    -- Fceux loop model
    while true do
        draw_status()
        emu.frameadvance()
    end
end
