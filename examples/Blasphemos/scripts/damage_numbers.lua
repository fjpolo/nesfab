-- damage_numbers.lua v1.0
-- Renders floating damage numbers above enemies in Mesen/FCEUX
-- Captures data packets from the NES on CPU port $4018

local hitbox_data = {}
local current_frame_data = nil
local PACKET_SIZE = 120
local frames_since_data = 0
local data_index = 0
local total_writes = 0
local header_window = {0,0,0,0}

-- Damage number entities
local damage_numbers = {} -- each entry: {x, y, amount, timer, max_timer, color, is_crit}

-- Previous frame enemy health cache to detect drops
local prev_warden_hp = nil
local prev_pilgrim_hp = {}
local prev_wheelbroken_hp = {}

local function to_signed(lo, hi)
    if not lo or not hi then return 0 end
    local val = (lo or 0) | ((hi or 0) << 8)
    if val >= 0x8000 then val = val - 0x10000 end
    return val
end

-- Hook debug writes on $4018
function on_debug_write(address, value)
    total_writes = total_writes + 1
    
    header_window[1] = header_window[2]
    header_window[2] = header_window[3]
    header_window[3] = header_window[4]
    header_window[4] = value
    
    -- Header packet sync: 77 88 99 AA
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

-- Spawn a damage number
local function spawn_damage_number(x, y, amount)
    if amount <= 0 then return end
    
    local is_crit = (amount >= 16)
    local color = 0xFFFFFF -- Default White
    if is_crit then
        color = 0xFF0000 -- Vivid Red for CRIT/COMBO!
    end
    
    table.insert(damage_numbers, {
        x = x,
        y = y,
        amount = amount,
        timer = 45, -- duration in frames
        max_timer = 45,
        color = color,
        is_crit = is_crit
    })
end

-- Update and render damage numbers
local function update_and_draw_damage_numbers()
    local i = 1
    while i <= #damage_numbers do
        local dn = damage_numbers[i]
        dn.timer = dn.timer - 1
        
        if dn.timer <= 0 then
            table.remove(damage_numbers, i)
        else
            -- Float upward
            local progress = (dn.max_timer - dn.timer) / dn.max_timer
            local draw_y = dn.y - (progress * 25)
            
            -- Render text
            local text = tostring(dn.amount)
            if dn.is_crit then
                text = text .. " CRIT!"
                -- Draw drop shadow for CRIT
                emu.drawString(dn.x + 1, draw_y + 1, text, 0x000000, 0xFFFFFF)
                emu.drawString(dn.x, draw_y, text, dn.color, 0x000000)
            else
                emu.drawString(dn.x, draw_y, text, dn.color, 0x000000)
            end
            
            i = i + 1
        end
    end
end

function on_frame()
    if current_frame_data then
        local d = current_frame_data
        local cam_x = to_signed(d[22], d[23])
        
        -------------------------------------------------------------
        -- 1. WARDEN BOSS
        -------------------------------------------------------------
        local warden_active = d[21]
        if warden_active ~= 0 then
            local curr_hp = d[33]
            local wx = to_signed(d[13], d[14])
            local wy = to_signed(d[15], d[16])
            local ww = to_signed(d[17], d[18])
            
            if prev_warden_hp and curr_hp < prev_warden_hp then
                local dmg = prev_warden_hp - curr_hp
                local sx = wx - cam_x + (ww / 2) - 10
                local sy = wy - 15
                spawn_damage_number(sx, sy, dmg)
            end
            prev_warden_hp = curr_hp
        else
            prev_warden_hp = nil
        end
        
        -------------------------------------------------------------
        -- 2. ENRAGED PILGRIMS
        -------------------------------------------------------------
        local p_num = d[34] or 0
        local next_pilgrim_hp = {}
        for i = 0, 7 do
            if i < p_num then
                local b = 35 + (i * 5)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                local curr_hp = d[b+4]
                
                -- We use the pilgrim's index i as cache key
                local prev_hp = prev_pilgrim_hp[i]
                if prev_hp and curr_hp < prev_hp then
                    local dmg = prev_hp - curr_hp
                    local sx = ex - cam_x - 5
                    local sy = ey - 30
                    spawn_damage_number(sx, sy, dmg)
                end
                next_pilgrim_hp[i] = curr_hp
            end
        end
        prev_pilgrim_hp = next_pilgrim_hp
        
        -------------------------------------------------------------
        -- 3. WHEELBROKENS
        -------------------------------------------------------------
        local w_num = d[75] or 0
        local next_wheelbroken_hp = {}
        for i = 0, 7 do
            if i < w_num then
                local b = 76 + (i * 5)
                local ex = to_signed(d[b], d[b+1])
                local ey = to_signed(d[b+2], d[b+3])
                local curr_hp = d[b+4]
                
                -- We use the wheelbroken's index i as cache key
                local prev_hp = prev_wheelbroken_hp[i]
                if prev_hp and curr_hp < prev_hp then
                    local dmg = prev_hp - curr_hp
                    local sx = ex - cam_x - 5
                    local sy = ey - 30
                    spawn_damage_number(sx, sy, dmg)
                end
                next_wheelbroken_hp[i] = curr_hp
            end
        end
        prev_wheelbroken_hp = next_wheelbroken_hp
    end

    -- Draw active damage numbers
    update_and_draw_damage_numbers()

    frames_since_data = frames_since_data + 1
    if frames_since_data > 10 then
        emu.drawString(8, 8, "DAMAGE OVERLAY: WAITING ON DATA...", 0xFF0000, 0x000000)
    else
        emu.drawString(8, 8, "DAMAGE OVERLAY: ACTIVE", 0x00FF00, 0x000000)
    end
end

local writeCallbackType = (emu.callbackType and emu.callbackType.write) or (emu.memCallbackType and emu.memCallbackType.cpuWrite) or 1
emu.addMemoryCallback(on_debug_write, writeCallbackType, 0x4018)
emu.addEventCallback(on_frame, emu.eventType.endFrame)
emu.log("Damage Number script loaded successfully!")
