-- ============================================================
-- level5_debug.lua — Blasphemos L4→L5 transition debugger
-- Load in Mesen: Script Window → Open Script
-- ============================================================

-- RAM addresses (from BlasNESmous.mlb / ram_variables.txt)
local ADDR = {
    -- Player struct (p)
    px_lo           = 0x0219,  -- p.x  low  byte (SS)
    px_hi           = 0x021A,  -- p.x  high byte
    py_lo           = 0x021B,  -- p.y  low  int byte  (SSF)
    py_hi           = 0x0013,  -- p.y  high int byte  (scattered to zero-page!)
    py_frac         = 0x021C,  -- p.y  fractional byte
    xspeed_lo       = 0x022D,  -- p.xspeed int  (SF)
    xspeed_frac     = 0x022E,  -- p.xspeed frac
    yspeed_lo       = 0x022F,  -- p.yspeed int  (SF)  ← signed: 0xFF = -1, 0x04 = +4
    yspeed_frac     = 0x0230,  -- p.yspeed frac
    movement        = 0x0231,  -- p.movement
    is_initialised  = 0x0236,  -- p.is_initialised (Bool, ~p@31 area; verify if wrong)

    -- Level / spawn flags
    current_level_index = 0x031D,
    spawn_from_right    = 0x0258,
    spawn_from_top      = 0x0259,
    spawn_from_bottom   = 0x025A,
    load_level_counter  = 0x024C,
}

-- Level index constants
local LEVEL_L4 = 6
local LEVEL_L5 = 8

-- --------------------------------------------------------
-- Helpers
-- --------------------------------------------------------
local function readByte(addr)
    return emu.read(addr, emu.memType.nesDebug)
end

local function signedByte(v)
    if v >= 0x80 then return v - 0x256 end
    return v
end

local function readSS(lo, hi)
    local raw = readByte(lo) + readByte(hi) * 256
    if raw >= 0x8000 then return raw - 0x10000 end
    return raw
end

-- SF: 8.8 signed fixed-point (int byte is signed, frac byte is unsigned fraction)
local function readSF(int_addr, frac_addr)
    local int_part  = signedByte(readByte(int_addr))
    local frac_part = readByte(frac_addr) / 256.0
    if int_part >= 0 then
        return int_part + frac_part
    else
        return int_part - frac_part
    end
end

-- SSF: 16.8 signed fixed-point  (int = SS, frac byte)
local function readSSF(lo, hi, frac_addr)
    local int_part  = readSS(lo, hi)
    local frac_part = readByte(frac_addr) / 256.0
    if int_part >= 0 then
        return int_part + frac_part
    else
        return int_part - frac_part
    end
end

-- --------------------------------------------------------
-- State
-- --------------------------------------------------------
local prev_level     = -1
local prev_llc       = -1   -- load_level_counter
local frame          = 0
local was_in_l5      = false
local void_logged    = false

-- --------------------------------------------------------
-- Per-frame callback
-- --------------------------------------------------------
local function onFrame()
    frame = frame + 1

    local lvl  = readByte(ADDR.current_level_index)
    local llc  = readByte(ADDR.load_level_counter)
    local in_l5 = (lvl == LEVEL_L5)

    -- Detect level transition (load_level_counter bumped)
    if llc ~= prev_llc then
        local sfr = readByte(ADDR.spawn_from_right)
        local sft = readByte(ADDR.spawn_from_top)
        local sfb = readByte(ADDR.spawn_from_bottom)
        local px  = readSS(ADDR.px_lo, ADDR.px_hi)
        local py  = readSSF(ADDR.py_lo, ADDR.py_hi, ADDR.py_frac)
        local ysp = readSF(ADDR.yspeed_lo, ADDR.yspeed_frac)
        local init = readByte(ADDR.is_initialised)
        emu.log(string.format(
            "[L5DBG] LEVEL LOAD  frame=%d  level=%d->%d  llc=%d->%d",
            frame, prev_level, lvl, prev_llc, llc))
        emu.log(string.format(
            "[L5DBG]   px=%d  py=%.2f  yspeed=%.3f  sfr=%d sft=%d sfb=%d  is_init=%d",
            px, py, ysp, sfr, sft, sfb, init))
        void_logged = false
        prev_llc    = llc
    end

    -- Track every frame while in L5 (or first few frames after entry)
    if in_l5 then
        local px  = readSS(ADDR.px_lo, ADDR.px_hi)
        local py  = readSSF(ADDR.py_lo, ADDR.py_hi, ADDR.py_frac)
        local ysp = readSF(ADDR.yspeed_lo, ADDR.yspeed_frac)
        local mov = readByte(ADDR.movement)

        -- Draw HUD overlay on screen
        emu.drawString(2, 10, string.format("LVL:%d  X:%d  Y:%.1f", lvl, px, py),
                       0xFFFFFF, 0xAA000000)
        emu.drawString(2, 20, string.format("yspeed:%.3f  mov:%d", ysp, mov),
                       0xFFFFFF, 0xAA000000)

        -- Warn if player falling fast
        if ysp > 2.5 then
            emu.drawString(2, 30, "!! HIGH YSPEED !!",
                           0xFF0000, 0xAA000000)
        end

        -- Detect void fall (y > 240)
        if py > 240 and not void_logged then
            emu.log(string.format(
                "[L5DBG] !! VOID FALL !!  frame=%d  px=%d  py=%.2f  yspeed=%.3f  mov=%d",
                frame, px, py, ysp, mov))
            void_logged = true
        end

        -- Log every 15 frames so we can trace the fall
        if frame % 15 == 0 then
            emu.log(string.format(
                "[L5DBG] f=%d  px=%d  py=%.2f  yspeed=%.3f  mov=%d",
                frame, px, py, ysp, mov))
        end

        was_in_l5 = true
    elseif was_in_l5 then
        -- Just left L5 — log final state
        local px  = readSS(ADDR.px_lo, ADDR.px_hi)
        local py  = readSSF(ADDR.py_lo, ADDR.py_hi, ADDR.py_frac)
        emu.log(string.format(
            "[L5DBG] Left L5 — final px=%d py=%.2f  new_level=%d", px, py, lvl))
        was_in_l5  = false
        void_logged = false
    end

    prev_level = lvl
end

-- --------------------------------------------------------
-- Register callbacks
-- --------------------------------------------------------
emu.addEventCallback(onFrame, emu.eventType.endFrame)
emu.log("[L5DBG] level5_debug.lua loaded — watching L4→L5 transition")
