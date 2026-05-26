-- debug_all.lua v1.1
-- Integrated Health Bars and Hitboxes for entities
-- Listens to $4018 memory protocol from main.fab export_hitboxes()

local hitbox_data = {}
local current_packet = nil
local PACKET_SIZE = 161
local frames_since_data = 0
local data_index = 0
local total_writes = 0
local header_window = {0,0,0,0}

local function to_signed(lo, hi)
    if not lo or not hi then return 0 end
    local val = (lo or 0) | ((hi or 0) << 8)
    if val >= 0x8000 then val = val - 0x10000 end
    return val
end

local function draw_rect(x, y, w, h, color, fill)
    if x + w < 0 or x > 256 or y + h < 0 or y > 240 then return end
    emu.drawRectangle(x, y, w, h, color, fill or false, 1)
end

local function draw_health_bar(x, y, w, current, max_val, color)
    if not current or current <= 0 then return end
    if x + w < 0 or x > 256 or y < -20 or y > 240 then return end
    
    local bar_h, bar_w = 4, w
    local fill_w = math.floor((current / max_val) * bar_w)
    if fill_w > bar_w then fill_w = bar_w end
    if fill_w < 0 then fill_w = 0 end
    
    -- Background
    emu.drawRectangle(x, y, bar_w, bar_h, 0x000000, true, 1)
    -- Fill
    if fill_w > 0 then 
        emu.drawRectangle(x, y, fill_w, bar_h, color, true, 1) 
    end
    -- Border
    emu.drawRectangle(x, y, bar_w, bar_h, 0xFFFFFF, false, 1)
    
    -- Label
    emu.drawString(x, y - 8, "HP:" .. current, 0xFFFFFF, 0x000000)
end

function on_debug_write(address, value)
    total_writes = total_writes + 1
    header_window[1] = header_window[2]
    header_window[2] = header_window[3]
    header_window[3] = header_window[4]
    header_window[4] = value
    
    -- Header: 77 88 99 AA
    if header_window[1] == 0x77 and header_window[2] == 0x88 and header_window[3] == 0x99 and header_window[4] == 0xAA then
        hitbox_data = { 0x77, 0x88, 0x99, 0xAA }
        data_index = 5
        return
    end
    
    if data_index > 0 then
        hitbox_data[data_index] = value
        data_index = data_index + 1
        if data_index > PACKET_SIZE then
            current_packet = {}
            for i=1, PACKET_SIZE do current_packet[i] = hitbox_data[i] end
            frames_since_data = 0
            data_index = 0
        end
    end
end

function on_frame()
    if current_packet then
        local d = current_packet
        local cam_x = to_signed(d[22], d[23])
        local is_konami = d[157] == 1
        
        -- 1. Player
        local px = to_signed(d[5], d[6])
        local py = to_signed(d[7], d[8])
        local pw = to_signed(d[9], d[10])
        local ph = to_signed(d[11], d[12])
        draw_rect(px - cam_x, py, pw, ph, 0x00FF00, false) -- Green Outline
        emu.drawString(px - cam_x + pw/2, py - 10, string.format("P: (%d,%d)", px, py), 0x00FF00, 0x000000)
        
        -- 2. Sword
        if d[32] ~= 0 then
            local sx, sy = to_signed(d[24], d[25]), to_signed(d[26], d[27])
            local sw, sh = to_signed(d[28], d[29]), to_signed(d[30], d[31])
            draw_rect(sx - cam_x, sy, sw, sh, 0x00FFFF, false) -- Cyan Outline
        end
        
        -- 3. Warden
        if d[21] ~= 0 then
            local wx, wy = to_signed(d[13], d[14]), to_signed(d[15], d[16])
            local ww, wh = to_signed(d[17], d[18]), to_signed(d[19], d[20])
            local max_hp = is_konami and 255 or 140
            draw_rect(wx - cam_x, wy, ww, wh, 0xFF0000, false) -- Red Outline
            draw_health_bar(wx - cam_x + (ww/2) - 16, wy - 12, 32, d[33], max_hp, 0xFF0000)
        end
        
        -- 4. Enraged Pilgrims
        local p_num = d[34] or 0
        for i = 0, 7 do
            if i < p_num then
                local b = 35 + (i * 5)
                local ex, ey = to_signed(d[b], d[b+1]), to_signed(d[b+2], d[b+3])
                local hp = d[b+4]
                local max_hp = is_konami and 60 or 30
                draw_rect(ex - cam_x - 12, ey - 16, 16, 16, 0xFFA500, false) -- Orange
                draw_health_bar(ex - cam_x - 12, ey - 36, 24, hp, max_hp, 0xFFA500)
                emu.drawString(ex - cam_x + 6, ey - 10, string.format("(%d,%d)", ex, ey), 0xFFA500, 0x000000)
            end
        end
        
        -- 5. Wheelbrokens
        local w_num = d[75] or 0
        for i = 0, 7 do
            if i < w_num then
                local b = 76 + (i * 5)
                local ex, ey = to_signed(d[b], d[b+1]), to_signed(d[b+2], d[b+3])
                local hp = d[b+4]
                local max_hp = is_konami and 80 or 40
                draw_rect(ex - cam_x - 8, ey - 24, 16, 24, 0xFFFF00, false) -- Yellow
                draw_health_bar(ex - cam_x - 12, ey - 44, 24, hp, max_hp, 0xFFFF00)
                emu.drawString(ex - cam_x + 10, ey - 15, string.format("(%d,%d)", ex, ey), 0xFFFF00, 0x000000)
            end
        end

        -- 6. Crucifieds
        local c_num = d[116] or 0
        for i = 0, 7 do
            if i < c_num then
                local b = 117 + (i * 5)
                local ex, ey = to_signed(d[b], d[b+1]), to_signed(d[b+2], d[b+3])
                local hp = d[b+4]
                local max_hp = is_konami and 90 or 45
                draw_rect(ex - cam_x - 4, ey - 16, 16, 16, 0xFF00FF, false) -- Magenta
                draw_health_bar(ex - cam_x - 12, ey - 36, 24, hp, max_hp, 0xFF00FF)
                emu.drawString(ex - cam_x + 6, ey - 10, string.format("(%d,%d)", ex, ey), 0xFF00FF, 0x000000)
            end
        end
    end

    frames_since_data = frames_since_data + 1
    if frames_since_data > 10 then
        emu.drawString(8, 8, "WAITING ON $4018... Writes: " .. total_writes, 0xFF0000, 0x000000)
    else
        emu.drawString(8, 8, "DEBUG DATA ACTIVE", 0x00FF00, 0x000000)
    end
end

local cbType = (emu.callbackType and emu.callbackType.write) or (emu.memCallbackType and emu.memCallbackType.cpuWrite) or 1
emu.addMemoryCallback(on_debug_write, cbType, 0x4018)
emu.addEventCallback(on_frame, emu.eventType.endFrame)
emu.log("Integrated Debug script Loaded.")
