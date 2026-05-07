-- sprite_count.lua
-- Shows the total number of sprites currently being drawn

local oam_base = nil
local scan_ticks = 0

local function update()
    scan_ticks = scan_ticks + 1
    
    -- In Mesen 2, memory types are enums. We try to be compatible.
    local cpuMem = emu.memType.nesMemory or emu.memType.cpu or 0
    local oamMem = emu.memType.oam or 2
    
    -- Periodic scan to find the OAM buffer
    if not oam_base or scan_ticks % 60 == 0 then
        -- Search for the hearts pattern (Y=8, Tile=$0B) in RAM
        for addr = 0x0000, 0x07FC, 1 do
            local y = emu.read(addr, cpuMem)
            local tile = emu.read(addr + 1, cpuMem)
            
            -- Hearts are at Y=8, Tile=$0B
            if (y == 8 or y == 7) and tile == 0x0B then
                oam_base = addr
                break
            end
        end
    end
    
    local sprite_count = 0
    -- Use detected address, fallback to $0400 (from .mlb) or $0200
    local base = oam_base or 0x0400
    
    for i = 0, 63 do
        local y = emu.read(base + i * 4, cpuMem)
        if y < 240 then
            sprite_count = sprite_count + 1
        end
    end
    
    -- Display
    local x, y_pos = 8, 45
    local text = string.format("Sprites: %d/64", sprite_count)
    local source = oam_base and string.format("RAM $%04X", oam_base) or string.format("RAM $%04X (Default)", base)
    
    -- Show first 4 bytes of the chosen base
    local b0 = emu.read(base + 0, cpuMem)
    local b1 = emu.read(base + 1, cpuMem)
    local b2 = emu.read(base + 2, cpuMem)
    local b3 = emu.read(base + 3, cpuMem)
    local debug_text = string.format("S0: %02X %02X %02X %02X", b0, b1, b2, b3)
    
    local color = 0xFFFFFF
    if sprite_count > 50 then color = 0xFF4444 
    elseif sprite_count > 32 then color = 0xFFFF44 end
    
    emu.drawRectangle(x, y_pos, 105, 30, 0xCC000000, true)
    emu.drawRectangle(x, y_pos, 105, 30, 0xFFFFFFFF, false)
    emu.drawString(x + 4, y_pos + 3, text, color, 0x000000)
    emu.drawString(x + 4, y_pos + 12, debug_text, 0xAAAAAA, 0x000000)
    emu.drawString(x + 4, y_pos + 21, source, 0x888888, 0x000000)
    
    -- Also try to read from PPU OAM directly and show in log once
    if scan_ticks == 1 then
        local p0 = emu.read(0, oamMem)
        emu.log(string.format("PPU OAM[0] is %d", p0))
    end
end

emu.addEventCallback(update, emu.eventType.endFrame)
emu.log("Sprite Count script v5 loaded.")
