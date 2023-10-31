# ToDo:
- Change name to Luz y Fer
  - Luci -> Luz
- System
  - Add states and screens
    - Pause
    - Win
    - Game Over
  - Remove all magic numbers
- Bugs
  - Being Lucifer and changing to Luci Y Fer in the air
    - 2nd sprite not affected by gravity
      - Bug or feature?
  - Fix transition from L2 to L3
- Graphs
  - Make tiles according to game
  - Make proper maps
    - Don't scroll?
    - Make Arcade screens and map?
  - Make a copy of CHR with some tiles changed  
    - Change every X frames to give movement to background
- Game experience
  - Add status bar
  - Add enemies
  - Add bosses
  - Add secrets
  - Enemies
    - God?
      - Gods?
    - Devil?
    - Demons?
    - Eyes and ears
      - Act as guards
  - Stamina
    - Luci should get tired of climbing?
    - Fer should jump less when tired?

# Changes
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

## [17.102023]
- Add ladder for Luci (Not Fer)
  - Luci move ↕
- Add story screen
 - Add states
  - Story
  - Play
- START 🔘 skips STORY screen

## [12.102023]
- Prepare code skeleton based on "animation" and "platformer"
- Prepare some test levels
- Create Luci, Fer and Lucifer sprites
- Animate sprites
- Move ⬅➡
- Jump 🅰
- Change level and character with SELECT 🔘
