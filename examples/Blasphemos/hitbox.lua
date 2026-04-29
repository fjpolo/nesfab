-- hitbox.lua for Mesen
-- Listens to memory writes on 0x00FE to receive hitbox coordinates

local hitbox_data = {}
local data_index = 1

function process_hitboxes()
    -- Ensure we have exactly 28 bytes
    if #hitbox_data ~= 28 then return end

    local px_lo = hitbox_data[1]
    local px_hi = hitbox_data[2]
    local py_lo = hitbox_data[3]
    local py_hi = hitbox_data[4]
    local pw_lo = hitbox_data[5]
    local pw_hi = hitbox_data[6]
    local ph_lo = hitbox_data[7]
    local ph_hi = hitbox_data[8]

    local wx_lo = hitbox_data[9]
    local wx_hi = hitbox_data[10]
    local wy_lo = hitbox_data[11]
    local wy_hi = hitbox_data[12]
    local ww_lo = hitbox_data[13]
    local ww_hi = hitbox_data[14]
    local wh_lo = hitbox_data[15]
    local wh_hi = hitbox_data[16]

    local warden_active = hitbox_data[17]

    local cam_x_lo = hitbox_data[18]
    local cam_x_hi = hitbox_data[19]
    
    local sx_lo = hitbox_data[20]
    local sx_hi = hitbox_data[21]
    local sy_lo = hitbox_data[22]
    local sy_hi = hitbox_data[23]
    local sw_lo = hitbox_data[24]
    local sw_hi = hitbox_data[25]
    local sh_lo = hitbox_data[26]
    local sh_hi = hitbox_data[27]
    
    local sword_active = hitbox_data[28]

    -- Convert to 16-bit signed integers
    local function to_signed(lo, hi)
        local val = lo | (hi << 8)
        if val >= 0x8000 then val = val - 0x10000 end
        return val
    end

    local px = to_signed(px_lo, px_hi)
    local py = to_signed(py_lo, py_hi)
    local pw = to_signed(pw_lo, pw_hi)
    local ph = to_signed(ph_lo, ph_hi)
    
    local wx = to_signed(wx_lo, wx_hi)
    local wy = to_signed(wy_lo, wy_hi)
    local ww = to_signed(ww_lo, ww_hi)
    local wh = to_signed(wh_lo, wh_hi)
    
    local sx = to_signed(sx_lo, sx_hi)
    local sy = to_signed(sy_lo, sy_hi)
    local sw = to_signed(sw_lo, sw_hi)
    local sh = to_signed(sh_lo, sh_hi)

    local cam_x = to_signed(cam_x_lo, cam_x_hi)

    -- Draw Player Hitbox (always drawn)
    local p_screen_x = px - cam_x
    local p_screen_y = py
    emu.drawRectangle(p_screen_x, p_screen_y, pw, ph, 0x00FF00, false)

    -- Draw Sword Hitbox (if active)
    if sword_active ~= 0 then
        local s_screen_x = sx - cam_x
        local s_screen_y = sy
        emu.drawRectangle(s_screen_x, s_screen_y, sw, sh, 0x00A0FF, false)
    end

    -- Draw Warden Hitbox (if active)
    if warden_active ~= 0 then
        local w_screen_x = wx - cam_x
        local w_screen_y = wy
        -- Only draw if partially visible
        if w_screen_x + ww >= 0 and w_screen_x < 256 then
            emu.drawRectangle(w_screen_x, w_screen_y, ww, wh, 0xFF0000, false)
        end
    end
end

-- Intercept CPU writes to our designated hook address
function on_hitbox_write(address, value)
    hitbox_data[data_index] = value
    data_index = data_index + 1
    
    -- Once 28 bytes are written, process and draw!
    if data_index > 28 then
        process_hitboxes()
        data_index = 1
    end
end

-- Register the callback
emu.addMemoryCallback(on_hitbox_write, emu.callbackType.write, 0x00FE)

emu.log("Hitbox script loaded! Waiting for game data...")
