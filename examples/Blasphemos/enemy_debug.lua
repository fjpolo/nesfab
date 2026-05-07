-- enemy_debug.lua v2.3 (Port $4018)
-- Shows health bars for on-screen enemies
-- Listens to memory writes on 0x4018

local hitbox_data = {}
local current_frame_data = nil
local PACKET_SIZE = 120
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
    local text = "HP:" .. current
    emu.drawString(x, y - 8, text, 0xFFFFFF, 0x000000)
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
            current_frame_data = {}
            for i=1, PACKET_SIZE do current_frame_data[i] = hitbox_data[i] end
            frames_since_data = 0
            data_index = 0
        end
    end
end

function on_frame()
    if current_frame_data then
        local d = current_frame_data
        local cam_x = to_signed(d[22], d[23])
        
        local is_konami = d[116] == 1 -- GAME_MODE_KONAMI
        
        -- Warden (Warden health at d[33])
        local warden_active = d[21]
        if warden_active ~= 0 then
            local wx = to_signed(d[13], d[14])
            local wy = to_signed(d[15], d[16])
            local ww = to_signed(d[17], d[18])
            local max_hp = 140
            if is_konami then max_hp = 255 end
            draw_health_bar(wx - cam_x + (ww/2) - 16, wy - 12, 32, d[33], max_hp, 0xFF0000)
        end
        
        -- Enraged Pilgrims (Max 8, starts at d[35], count at d[34])
        local p_num = d[34] or 0
        for i = 0, 7 do
            if i < p_num then
                local b = 35 + (i * 5)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                local hp = d[b+4]
                local max_hp = 30
                if is_konami then max_hp = 60 end
                draw_health_bar(ex - cam_x - 12, ey - 36, 24, hp, max_hp, 0xFFA500)
            end
        end
        
        -- Wheelbrokens (Max 8, starts at d[76], count at d[75])
        local w_num = d[75] or 0
        for i = 0, 7 do
            if i < w_num then
                local b = 76 + (i * 5)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                local hp = d[b+4]
                local max_hp = 40
                if is_konami then max_hp = 80 end
                draw_health_bar(ex - cam_x - 12, ey - 36, 24, hp, max_hp, 0xFFFF00)
            end
        end
    end

    frames_since_data = frames_since_data + 1
    if frames_since_data > 10 then
        emu.drawString(8, 8, "WAITING ON $4018... Writes: " .. total_writes, 0xFF0000, 0x000000)
        local h_str = ""
        for i=1,4 do h_str = h_str .. string.format("%02X ", header_window[i]) end
        emu.drawString(8, 20, "Hdr: " .. h_str, 0xFFFFFF, 0x000000)
    else
        emu.drawString(8, 8, "DEBUG DATA ACTIVE", 0x00FF00, 0x000000)
    end
end

local writeCallbackType = (emu.callbackType and emu.callbackType.write) or (emu.memCallbackType and emu.memCallbackType.cpuWrite) or 1
emu.addMemoryCallback(on_debug_write, writeCallbackType, 0x4018)
emu.addEventCallback(on_frame, emu.eventType.endFrame)
emu.log("Enemy Debug script v2.3 (Port $4018) Loaded.")
