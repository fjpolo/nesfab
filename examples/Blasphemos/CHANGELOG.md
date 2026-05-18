# Changes

## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v830
- Try to fix scrolling garbage tiles when transitioning to previous levels. Did not work


## [18.05.2026] - v829
- Fix the issue of garbage tiles when scrolling


## [18.05.2026] - v829
- Fix the issue of garbage tiles when scrolling


## [18.05.2026] - v829
- Fix the issue of garbage tiles when scrolling


## [18.05.2026] - v829
- Fix the issue of garbage tiles when scrolling


## [18.05.2026] - v829
- Fix the issue of garbage tiles when scrolling


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v828
- Fix level indexing


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v827
- Add dead screen


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v826
- Fix some level tiles


## [18.05.2026] - v825
- level6 was split into 2 levels each


## [18.05.2026] - v825
- level6 was split into 2 levels each


## [18.05.2026] - v824
- level3 was split into 2 levels each


## [18.05.2026] - v822
- level2 and level3 were split into 2 levels each


## [18.05.2026] - v822
- level2 and level3 were split into 2 levels each


## [18.05.2026] - v821
- I don't think I could fix anything


## [18.05.2026] - v821
- I don't think I could fix anything


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [18.05.2026] - v820
- Fix enemies dissapearing after one hit


## [17.05.2026] - v819
- Add 3 hit combo


## [17.05.2026] - v825
- Fix Python-style indentation alignment of enemy death/deletion blocks inside EnragedPilgrim.fab, Crucified.fab, and Wheelbroken.fab to prevent enemies from being prematurely deleted on the very first hit

## [17.05.2026] - v824
- Uncomment CPU port $4018 hitbox/health debug exports in main.fab and introduce `damage_numbers.lua` to track and draw floating damage numbers over hit enemies in the emulator

## [17.05.2026] - v819
- Add 3 hit combo


## [17.05.2026] - v819
- Add 3 hit combo


## [17.05.2026] - v823
- Explicitly reset `swing_is_combo_hit` to `false` when resetting combo count (on swing end, player hurt, or level load) to prevent subsequent standard hits from dealing double damage

## [17.05.2026] - v822
- Change the player sword combo finisher subpalette color from sky blue ($2C) to vivid red ($15) for a more intense and matching strike aesthetic

## [17.05.2026] - v821
- Refine player sword combo subpalette timing so that the sword turns sky-blue ONLY during the 3rd swing (the combo finisher itself) instead of turning blue immediately when the 2nd hit lands

## [17.05.2026] - v820
- Fix combo hit registration during enemy/boss I-frames (invincibility flashing) to prevent hitting flashing targets from incorrectly resetting the combo count to 0

## [17.05.2026] - v819
- Implement a 3-hit player sword combo mechanic: the third hit deals double damage, and the sword dynamically turns blue when the combo is primed (after the second hit)

## [17.05.2026] - v818
- Remap background metatiles using palette 0 to palette 2 in gameplay levels to resolve HUD palette conflicts and fix broken tiles/attributes on Level 2

## [17.05.2026] - v817
- Fix game over screen


## [17.05.2026] - v817
- Fix game over screen


## [16.05.2026] - v817
- Fix game over screen


## [16.05.2026] - v816
- Some broken tiles are fixed


## [16.05.2026] - v816
- Some broken tiles are fixed


## [16.05.2026] - v816
- Some broken tiles are fixed


## [16.05.2026] - v815
- Level transitioning was broken, now fixed


## [16.05.2026] - v815
- Level transitioning was broken, now fixed


## [16.05.2026] - v815
- Level transitioning was broken, now fixed


## [16.05.2026] - v815
- Level transitioning was broken, now fixed


## [16.05.2026] - v815
- Level transitioning was broken, now fixed


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v814
- Bugfix session


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v813
- Move HUD code to hud.fab


## [16.05.2026] - v812
- Fix phantom tiles


## [16.05.2026] - v812
- Fix phantom tiles


## [16.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v811
- Let player climb topmost C_WALL


## [15.05.2026] - v809
- Fix some tile issues


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v808
- I think HUB now works properly with mMC3 scanline IRQ


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v807
- Fix scroll attributes and force HUD palette


## [15.05.2026] - v806
- Restore scanline IRQ HUD implementation


## [15.05.2026] - v806
- Restore scanline IRQ HUD implementation


## [15.05.2026] - v804
- HUD kind of working


## [15.05.2026] - v804
- HUD kind of working


## [15.05.2026] - v804
- HUD kind of working


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v803
- Implement Map System fixes and Robust Sprite Rotation


## [15.05.2026] - v802
- Map is kind of working


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [15.05.2026] - v801
- Start working on a MAP :D


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v800
- Prie Dieus now refill heaslth and bile vessels


## [14.05.2026] - v799
- Update manual


## [14.05.2026] - v799
- Update manual


## [14.05.2026] - v798
- docs: Fix broken seal image with a custom local Southpole Seal


## [14.05.2026] - v798
- docs: Fix broken seal image with a custom local Southpole Seal


## [14.05.2026] - v798
- docs: Fix broken seal image with a custom local Southpole Seal


## [14.05.2026] - v798
- docs: Fix broken seal image with a custom local Southpole Seal


## [14.05.2026] - v794
- Crucified now attack, but inverted, but fuck it


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [13.05.2026] - v793
- Start working on Damned enemy


## [12.05.2026] - v791
- Add crucified, not attacking yet


## [12.05.2026] - v791
- Add crucified, not attacking yet


## [12.05.2026] - v791
- Add crucified, not attacking yet


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v790
- Fix item_bone persistence and expand level flags capacity


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v789
- Add new levels l8, l9, l9sub1, l9over1, l9over2, l10, l10sub1 and implement connections


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v788
- Fix Warden arena walls and transition bug


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [12.05.2026] - v787
- Fix Warden not hittable


## [11.05.2026] - v786
- Fix C_WALL collisions


## [11.05.2026] - v786
- Fix C_WALL collisions


## [11.05.2026] - v786
- Fix C_WALL collisions


## [11.05.2026] - v786
- Fix C_WALL collisions


## [11.05.2026] - v785
- Add new tiles from Castlevania3


## [11.05.2026] - v785
- Add new tiles from Castlevania3


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v783
- Clean up title screen


## [11.05.2026] - v782
- Add Title Screen


## [11.05.2026] - v782
- Add Title Screen


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v781
- Start working on Wasteland


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v780
- Integrated Level l6 and improved analyzeROM.py with RAM variable list


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [11.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [08.05.2026] - v779
- Preserve Y coordinate in l4 <-> l5 transitions


## [08.05.2026] - v778
- Add level transitions for l4, l4sub1, l5 and implement Mea Culpa altar with improved RAM analysis


## [08.05.2026] - v778
- Add level transitions for l4, l4sub1, l5 and implement Mea Culpa altar with improved RAM analysis


## [08.05.2026] - v777
- Implement very rough mea culpa altar


## [08.05.2026] - v777
- Implement very rough mea culpa altar


## [08.05.2026] - v777
- Implement very rough mea culpa altar


## [08.05.2026] - v777
- Implement very rough mea culpa altar


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [08.05.2026] - v776
- tart working on ladder climbing


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v775
- Fix broken collision


## [07.05.2026] - v774
- Implemented Konami mode health doubling, restored and improved enemy health debug bars.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v773
- Refactored level numbering, fixed Warden death logic, and automated BlasNESmous versioning.


## [07.05.2026] - v772
- Fix enemy placement


## [07.05.2026] - v772
- Fix enemy placement


## [07.05.2026] - v772
- Fix enemy placement


## [07.05.2026] - v771
- Rename Blasphemous to BlasNESmous in title screen


## [07.05.2026] - v770
- - Stop shaking after Warden is defeated

- Add arrow when Warden is defeated
- Rename level fab files
- Improve title_screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v769
- - Clean up a bit

- Add title screen


## [07.05.2026] - v768
- Update Player Sprite palette for details


## [07.05.2026] - v768
- Update Player Sprite palette for details


## [07.05.2026] - v768
- Update Player Sprite palette for details


## [07.05.2026] - v768
- Update Player Sprite palette for details


## [07.05.2026] - v768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.768
- Update Player Sprite palette for details


## [07.05.2026] - v0.0.1.767
- I just discovered I can add more palettes in MapFab :D


## [07.05.2026] - v0.0.1.766
- Fix sword hitbox when facing left


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.765
- Fix Pilgrim's hitboxes


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.764
- - Add Attack Power in HUD

- Add bones collected in HUD


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.763
- Do some more art


## [07.05.2026] - v0.0.1.762
- IMprove levels 1 and 2


## [07.05.2026] - v0.0.1.762
- IMprove levels 1 and 2


## [07.05.2026] - v0.0.1.761
- Add some trees xD


## [07.05.2026] - v0.0.1.761
- Add some trees xD


## [07.05.2026] - v0.0.1.761
- Add some trees xD


## [07.05.2026] - v0.0.1.760
- Refine sword hitboxes and adjust player attack power


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.759
- "Improve" level0 tiles


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.758
- Add sprite count debug script and update screens


## [07.05.2026] - v0.0.1.757
- Fix one pitfall


## [07.05.2026] - v0.0.1.757
- Fix one pitfall


## [07.05.2026] - v0.0.1.757
- Fix one pitfall


## [07.05.2026] - v0.0.1.757
- Fix one pitfall


## [07.05.2026] - v0.0.1.757
- Fix one pitfall


## [06.05.2026] - v0.0.1.757
- Fix one pitfall


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.755
- Implement persistent Warden boss death


## [06.05.2026] - v0.0.1.754
- Differentiate Prie-Dieu save points and allow switching


## [06.05.2026] - v0.0.1.754
- Differentiate Prie-Dieu save points and allow switching


## [06.05.2026] - v0.0.1.754
- Differentiate Prie-Dieu save points and allow switching


## [06.05.2026] - v0.0.1.753
- Implement healing flash effect and fix level transition spawning issues


## [06.05.2026] - v0.0.1.753
- Implement healing flash effect and fix level transition spawning issues


## [06.05.2026] - v0.0.1.753
- Implement healing flash effect and fix level transition spawning issues


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.752
- Penitent one flashes when healing


## [06.05.2026] - v0.0.1.751
- Fix sprite cycling and OAM indexing, split player rendering for flickering priority


## [06.05.2026] - v0.0.1.751
- Fix sprite cycling and OAM indexing, split player rendering for flickering priority


## [06.05.2026] - v0.0.1.751
- Fix sprite cycling and OAM indexing, split player rendering for flickering priority


## [06.05.2026] - v0.0.1.750
- Implement Bile Vessel healing system with HUD display


## [06.05.2026] - v0.0.1.750
- Implement Bile Vessel healing system with HUD display


## [06.05.2026] - v0.0.1.750
- Implement Bile Vessel healing system with HUD display


## [06.05.2026] - v0.0.1.750
- Implement Bile Vessel healing system with HUD display


## [06.05.2026] - v0.0.1.750
- Implement Bile Vessel healing system with HUD display


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.749
- Fix transparent


## [06.05.2026] - v0.0.1.747
- Fix macOS build scripts and update version


## [06.05.2026] - v0.0.1.747
- Fix macOS build scripts and update version


## [06.05.2026] - v0.0.1.746
- Add explicit make target for MacBook Pro 2019 Intel i5


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.744
- Make Wheelbroken attack with a wheel


## [06.05.2026] - v0.0.1.743
- Platforms now are on perspective xD


## [06.05.2026] - v0.0.1.743
- Platforms now are on perspective xD


## [06.05.2026] - v0.0.1.742
- Implement Level 3 Prie Dieu, bi-directional transitions, and enemy persistence


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [06.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.741
- fix: update debug shortcuts, add respawn logging, and implement Level 2->3 transition


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.740
- feat: implement automatic pogo bounce mechanic with 2-hit limit


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.739
- feat: implement ledge grab, cross-level Prie Dieu respawn, and Level 1->2 bounds transition


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.738
- fix: Optimized sprite cycling logic and fixed crash


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.737
- feat: Implement ItemBone collectibles and enemy hit flash effects


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.736
- Fix enemy health bar synchronization using robust hardware-port export protocol


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [05.05.2026] - v0.0.1.735
- Fix: All enemies and level elements now correctly respawn upon player death, including pit deaths in Level 1.


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.734
- Update todo


## [04.05.2026] - v0.0.1.733
- Implement level navigation cheats and fix player hitbox alignment. Fixes graphical glitches and state inconsistencies during level transitions. Sets starting level to level0.


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.732
- Fix player facing left hitboxes


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.731
- Implement dual hitboxes and parry mechanics for Wheelbroken, with universal parry response across all enemies


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [02.05.2026] - v0.0.1.730
- Improve Pilgrim's aggro


## [30.04.2026] - v0.0.1.729
- IMprove pilgrim sprite


## [30.04.2026] - v0.0.1.729
- IMprove pilgrim sprite


## [30.04.2026] - v0.0.1.728
- Refined Pilgrim hitboxes, increased player immunity to 2s, and added flickering effect


## [30.04.2026] - v0.0.1.728
- Refined Pilgrim hitboxes, increased player immunity to 2s, and added flickering effect


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.727
- Adjust player health and parry knockback, update version


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.726
- Make Warden slightly easier


## [30.04.2026] - v0.0.1.725
- - Fix dash (in-the-air-dash)

- Improve warden
- Add very rudimentary parry


## [30.04.2026] - v0.0.1.725
- - Fix dash (in-the-air-dash)

- Improve warden
- Add very rudimentary parry


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [30.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.724
- Improve warden


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.723
- When warden gets hit, make the world shake


## [29.04.2026] - v0.0.1.722
- Add dash mechanic (no slide :( )


## [29.04.2026] - v0.0.1.722
- Add dash mechanic (no slide :( )


## [29.04.2026] - v0.0.1.721
- Add changelog


## [29.04.2026] - v0.0.1.720
- Warden hitbox improved


## [14.12.2025]
- Player splits when colliding with following_eye
- Update some tiles
- Fer doesn't loop into an infinite loop of C_EXIT
- Following exe actually follows Lucifer!
- Following eye enemy now saves its state
- Luci can drop when climbing
- Fixed Lucifer flying animation
- Fix l10 infinite loop @C_EXIT

## [29.11.2023]
- Add PAUSE with Start button
  - Make it grayscale!!!! 😍

## [21.11.2023]
- Fix compiler warnings

## [20.11.2023]
- Add enemy_following_eye
  - Add Object Class logic
    - Add enemies_following_Eye
    - Add logic to `enemies.fab`
      - Add animations
        - Add logic to change sprite
    - Add logic to `level.macrofab`
    - Add logic to `level.fab`
    - Add logic to `main.fab`
  - Make following_eye initial state seudo-random
  - Start working on following_eye proyectile (pupil)

## [7.11.2023]
- Clean player.fab
  - Add more functions
  - Move center_x, center_y to player struct

## [31.10.2023]
- Add enemies as objects

## [30.10.2023]
- Start working on enemy eye

## [29.10.2023]
- Add stamina bar graphs and functionality
- Level0...15 makes more sense than start being 0
- Add key sprite, collision and functionality
- Don't render key when collected
- Add door sprite, collision and functionality
- Don't render door when key was collected
- Key [x,y] saved from player's [x,y]
- Added tutorial

## [25.10.2023]
- Add states and screens
  - Start
- Fix START state
    - Fix transition to STORY
- Fix transition from STORY to PLAY
    - Only when starting at START
- Clean NMI code
- [BugFix] Lucifer fly breaks sometimes after splitting to Luci Y Fer
- [BugFix] Luci climbing animation works
- Clean story and tips screen code


## [24.10.2023]
- Lucifer can split ⬅⬇➡
- Improve start screen

## [23.10.2023]
- Add NESDev Compo support (Multicart Action53 mapper)
- Update magic number to FIRST_LEVEL_INDEX
- Add Tips screen after story (if SELECT is pressed)
- 

## [20.10.2023]
- Fixed Luci's height
- Fixed Luci's animations
- Fixed Luci's collitions going up
- Fixed Luci's collitions going down
- Fixed animations when Lucifer splits
- Tested CHR ROM Bank swap every 30 frames
  - Not working correctly on tile collisions
  - Might be too slow
- Luci can climb ceiling thingies

## [19.10.2023]
- Store Player data somewhere, instead of creating them all the time
  - level index
  - current x,y
  - camera_x
- Change Fer back to palette 0
- Improve Luci and Fer's walk/run animation
- Add LuciFer fusion to Lucifer
  - Added animation
    - Improved animations
- Improved LuciYFer fusion to Lucifer
- Lucifer flies
  - Doesn't fly over the top limit
- Unique abilities
  - Luci climbs
  - Fer jumps and runs
  - Lucifer flies
- Fixed Lucifer flying timer
  - Can fly up to 1[S]
    - If the whole 1[s] isn't wasted, a counter decrements
      - When 0, can fly again
    - If whole 1[s] is used, punishment is 3[s] not flying
- Luci now climbs ladder with animation

## [18.10.2023]
- Cleaning:
  - Move player variables and functions to player.fab
  - Move story screen variables and functions to story_screen.fab
  - Move start screen function to start_screen.fab
- Use CHR bank switching for `bg.png` and `font.png` (with `MapFab`)
- Fer can run

## [17.10.2023]
- Add ladder for Luci (Not Fer)
  - Luci move ↕
- Add story screen
 - Add states
  - Story
  - Play
- START 🔘 skips STORY screen

## [12.10.2023]
- Prepare code skeleton based on "animation" and "platformer"
- Prepare some test levels
- Create Luci, Fer and Lucifer sprites
- Animate sprites
- Move ⬅➡
- Jump 🅰
- Change level and character with SELECT 🔘
