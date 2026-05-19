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
    -- Player coordinates (0x023A is px, 0x023C is py fraction, 0x023D is py integer)
    local px = read_s16(0x023A)
    local py = read_s16(0x023D)
    
    -- Camera coordinate
    local cam_x = read_s16(0x025B)
    
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
        -- Mesen API
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
