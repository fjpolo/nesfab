-- hitbox.lua for Mesen (Updated for $4018 protocol)
-- Shows hitboxes for player, sword, and enemies
-- Listens to memory writes on 0x4018

local hitbox_data = {}
local current_packet = nil
local PACKET_SIZE = 207
local data_index = 0
local header_window = {0,0,0,0}

local function to_signed(lo, hi)
    if not lo or not hi then return 0 end
    local val = lo | (hi << 8)
    if val >= 0x8000 then val = val - 0x10000 end
    return val
end

function draw_hitbox(x, y, w, h, color)
    if x + w < 0 or x > 256 or y + h < 0 or y > 240 then return end
    emu.drawRectangle(x, y, w, h, color, false)
end

function process_packet()
    if not current_packet then return end
    local d = current_packet
    
    -- Offsets based on main.fab export_hitboxes()
    -- Header: 1-4
    local px = to_signed(d[5], d[6])
    local py = to_signed(d[7], d[8])
    local pw = to_signed(d[9], d[10])
    local ph = to_signed(d[11], d[12])
    
    local wx = to_signed(d[13], d[14])
    local wy = to_signed(d[15], d[16])
    local ww = to_signed(d[17], d[18])
    local wh = to_signed(d[19], d[20])
    local warden_active = d[21]
    
    local cam_x = to_signed(d[22], d[23])
    
    local sx = to_signed(d[24], d[25])
    local sy = to_signed(d[26], d[27])
    local sw = to_signed(d[28], d[29])
    local sh = to_signed(d[30], d[31])
    local sword_active = d[32]
    
    -- Draw Player
    draw_hitbox(px - cam_x, py, pw, ph, 0x00FF00)
    
    -- Draw Sword
    if sword_active ~= 0 then
        draw_hitbox(sx - cam_x, sy, sw, sh, 0x00FFFF)
    end
    
    -- Draw Warden (Boss)
    if warden_active ~= 0 then
        draw_hitbox(wx - cam_x, wy, ww, wh, 0xFF0000)
    end
    
    -- Draw Enraged Pilgrims
    local pilgrim_num = d[34] or 0
    for i = 0, 7 do
        if i < pilgrim_num then
            local b = 35 + (i * 5)
            local ex = to_signed(d[b], d[b+1])
            local ey = to_signed(d[b+2], d[b+3])
            -- Enraged Pilgrims have: off_x=-12, off_y=-16, w=16, h=16
            draw_hitbox(ex - cam_x - 12, ey - 16, 16, 16, 0xFFA500)
        end
    end
    
    -- Draw Wheelbrokens
    local wheel_num = d[75] or 0
    for i = 0, 7 do
        if i < wheel_num then
            local b = 76 + (i * 5)
            local ex = to_signed(d[b], d[b+1])
            local ey = to_signed(d[b+2], d[b+3])
            -- Wheelbrokens have: off_x=-8, off_y=-24, w=16, h=24
            draw_hitbox(ex - cam_x - 8, ey - 24, 16, 24, 0xFFFF00)
        end
    end

    -- Draw Crucifieds
    local crucified_num = d[116] or 0
    for i = 0, 7 do
        if i < crucified_num then
            local b = 117 + (i * 5)
            local ex = to_signed(d[b], d[b+1])
            local ey = to_signed(d[b+2], d[b+3])
            -- Crucifieds have: off_x=-4, off_y=-16, w=16, h=16
            draw_hitbox(ex - cam_x - 4, ey - 16, 16, 16, 0x9400D3)
        end
    end

    -- Draw Spikes (Pinchos & Pinchos Invertidos)
    local pinchos_state = d[157] or 0
    if pinchos_state > 0 then
        local color = 0x808080 -- Dim grey default
        if pinchos_state == 1 then
            color = 0xFFA500 -- Orange for Warning state
        elseif pinchos_state == 2 then
            color = 0xFF00FF -- Fuchsia/Magenta for Danger state
        end
        
        -- Normal Pinchos
        local pinchos_num = d[158] or 0
        for i = 0, 8 do
            if i < pinchos_num then
                local b = 159 + (i * 4)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                draw_hitbox(ex - cam_x - 8, ey - 16, 16, 16, color)
            end
        end

        -- Inverted Pinchos
        local pinchos_inv_num = d[195] or 0
        for i = 0, 0 do
            if i < pinchos_inv_num then
                local b = 196 + (i * 4)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                draw_hitbox(ex - cam_x - 8, ey, 16, 16, color)
            end
        end
    end
end


function on_write(address, value)
    header_window[1] = header_window[2]
    header_window[2] = header_window[3]
    header_window[3] = header_window[4]
    header_window[4] = value
    
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
            data_index = 0
            -- We can process immediately or wait for on_frame
        end
    end
end

function on_frame()
    process_packet()
end

emu.addMemoryCallback(on_write, emu.callbackType.write, 0x4018)
emu.addEventCallback(on_frame, emu.eventType.endFrame)

emu.log("Hitbox script v3.0 ($4018) loaded.")
