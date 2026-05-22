-- Lua script for Mesen / Fceux to display real-time FPS with a rolling graph at the bottom of the screen.
-- This script detects when low-level hardware NMIs are not taken (e.g., during screen transitions) 
-- and dynamically tracks the true ground-truth game loop ticker 'fps_ticks'.

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
                    print(string.format("[FPS Script] Found %s at address: 0x%04X", var_name, addr))
                    return addr
                end
            end
            file:close()
        end
    end
    print(string.format("[FPS Script] Warning: Could not find %s in ram_variables.txt, using fallback: 0x%04X", var_name, fallback))
    return fallback
end

-- Resolve addresses dynamically
local ADDR_NMI_COUNTER = get_var_address("runtime_nmi_counter", 0x000A)
local ADDR_FPS_TICKS = get_var_address("fps_ticks", 0x02C7)

-- State variables
local last_game_frame = nil
local last_nmi_counter = nil

-- Sliding window for FPS calculation (60 active NMI frames window)
local active_frame_history = {}
local window_size = 60
for i = 1, window_size do
    active_frame_history[i] = 0
end
local history_index = 1

-- Rolling history for the visual graph (100 columns wide)
local graph_history = {}
local graph_width = 100
for i = 1, graph_width do
    graph_history[i] = 60.0
end

local last_active_fps = 60.0

function update_fps()
    -- Read hardware NMI counter (1-byte counter at $000A)
    local current_nmi_counter = memory.readbyte(ADDR_NMI_COUNTER)
    
    -- Check if NMI was actually processed on this emulator frame
    if last_nmi_counter ~= nil then
        if current_nmi_counter == last_nmi_counter then
            -- NMI was NOT taken (game is loading, transitioning, or has interrupts disabled)
            -- We pause the sliding window and return the last active FPS to avoid fake lag readings.
            return last_active_fps
        end
    end
    last_nmi_counter = current_nmi_counter

    -- NMI was taken! Active frame processing:
    -- Read game's ground-truth game loop iteration counter 'fps_ticks'
    local current_game_frame = memory.readbyte(ADDR_FPS_TICKS)
    local game_frame_changed = 0
    
    if last_game_frame ~= nil then
        if current_game_frame ~= last_game_frame then
            game_frame_changed = 1
        end
    end
    last_game_frame = current_game_frame
    
    -- Record this active frame's status in our sliding window
    active_frame_history[history_index] = game_frame_changed
    history_index = (history_index % window_size) + 1
    
    -- Calculate active gameplay FPS
    local total_frames = 0
    for i = 1, window_size do
        total_frames = total_frames + active_frame_history[i]
    end
    
    local current_fps = total_frames * (60.0 / window_size)
    last_active_fps = current_fps
    
    -- Shift graph history left
    for i = 1, graph_width - 1 do
        graph_history[i] = graph_history[i + 1]
    end
    graph_history[graph_width] = current_fps
    
    return current_fps
end

function draw_fps_graph()
    -- Update FPS
    local fps = update_fps()

    ----------------------------------------------------
    -- RENDER ROLLING PERFORMANCE GRAPH (Bottom Screen)
    ----------------------------------------------------
    local graph_x = 28
    local graph_y = 175
    local graph_h = 55
    local bottom_y = graph_y + graph_h -- 230
    
    -- 1. Draw Background Glass Panel
    if emu.drawRectangle then
        -- Mesen API (semi-transparent black card, drawing horizontal width x=24 to x=232)
        -- Explicitly pass frameCount = 1 as the 7th parameter
        emu.drawRectangle(graph_x - 4, graph_y - 4, (graph_width * 2) + 8, graph_h + 8, 0x60000000, true, 1)
        emu.drawString(graph_x + 4, graph_y + 4, string.format("FPS: %.1f", fps), 0xFFFFFF)
    elseif gui.box then
        -- Fceux API
        gui.box(graph_x - 4, graph_y - 4, graph_x + (graph_width * 2) + 4, bottom_y + 4, "#000000aa")
        gui.text(graph_x + 4, graph_y + 4, string.format("FPS: %.1f", fps))
    end
    
    -- 2. Draw Reference Line (30 FPS & 60 FPS)
    local y_60 = bottom_y - math.floor((60.0 / 60.0) * 45) -- Y = 185
    local y_30 = bottom_y - math.floor((30.0 / 60.0) * 45) -- Y = 207
    
    if emu.drawLine then
        -- 60 FPS Guideline (Green, with frameCount = 1)
        emu.drawLine(graph_x, y_60, graph_x + (graph_width * 2), y_60, 0x4000FF00, 1)
        emu.drawString(graph_x - 18, y_60 - 3, "60", 0x00FF00)
        
        -- 30 FPS Guideline (Red, with frameCount = 1)
        emu.drawLine(graph_x, y_30, graph_x + (graph_width * 2), y_30, 0x40FF0000, 1)
        emu.drawString(graph_x - 18, y_30 - 3, "30", 0xFF0000)
    elseif gui.line then
        gui.line(graph_x, y_60, graph_x + (graph_width * 2), y_60, "#00ff0040")
        gui.text(graph_x - 18, y_60 - 3, "60")
        gui.line(graph_x, y_30, graph_x + (graph_width * 2), y_30, "#ff000040")
        gui.text(graph_x - 18, y_30 - 3, "30")
    end

    -- 3. Draw Rolling FPS Continuous Line (function representation)
    local prev_x = nil
    local prev_y = nil
    
    for i = 1, graph_width do
        local fps_val = graph_history[i]
        
        -- Clamp value
        if fps_val > 60.0 then fps_val = 60.0 end
        if fps_val < 0.0 then fps_val = 0.0 end
        
        -- Map FPS (0..60) to Y heights (0..45 pixels tall)
        local bar_h = math.floor((fps_val / 60.0) * 45)
        local curr_y = bottom_y - bar_h
        local curr_x = graph_x + (i - 1) * 2
        
        -- Determine color based on performance tier
        local color = 0x7F00FF00 -- Green (Default, safe signed positive alpha)
        local fceux_color = "#00ff00"
        
        if fps_val < 45.0 then
            color = 0x7FFF0000 -- Red
            fceux_color = "#ff0000"
        elseif fps_val < 55.0 then
            color = 0x7FFFFF00 -- Yellow
            fceux_color = "#ffff00"
        end
        
        -- Draw line segment connecting to previous frame's data
        if prev_x ~= nil then
            if emu.drawLine then
                emu.drawLine(prev_x, prev_y, curr_x, curr_y, color, 1)
            elseif gui.line then
                gui.line(prev_x, prev_y, curr_x, curr_y, fceux_color)
            end
        end
        
        prev_x = curr_x
        prev_y = curr_y
    end
end

-- Polyfill for execution loop: Mesen vs Fceux
if emu and emu.addEventCallback then
    -- Mesen callback model
    emu.addEventCallback(draw_fps_graph, emu.eventType.endFrame)
else
    -- Fceux loop model
    while true do
        draw_fps_graph()
        emu.frameadvance()
    end
end
