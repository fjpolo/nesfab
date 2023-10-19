# ToDo:
- Change name to Luz y Fer
  - Luci -> Luz
- System
  - Add states and screens
    - Start
    - Pause
    - Win
    - Game Over
- Bugs
  - Lucifer animation bugs with height = 23px
  - Fix START state
    - Fix transition to STORY
  - Fix transition from STORY to PLAY
    - Only when starting at START
  - Lucifer glitches when changing direction
  - Lucifer collision is not working properly
    - Mostly flying upwards
  - Convert to Lucifer and then split
    - There are two Lucifer sprites instead of one for Luci and one for Fer
    - Convert again
      - Flying is glitched
- Graphs
  - Make tiles according to game
  - Make proper maps
    - Don't scroll
    - Make Arcade screens and map
  - Improve animations
- Game experience
  - Lucifer should get tired of flying
  - Improve story
  - Add enemies
  - Add bosses
  - Add secrets
  - Add doors/keys/buttons
  - Characters
    - Luci
      - Improve climbing
        - Animation
        - Climbing up it's a few pixels too high when reaching solid
      - Make it climb horizontally
        - If surface allows
    - Fer
      - Maybe fly a bit?
    - Lucifer
      - Flies
      - Summons something?
  - Enemies
    - God?
      - Gods?
    - Devil?

# Changes

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

## [18.10.2023]
- Cleaning:
  - Move player variables and functions to player.fab
  - Move story screen variables and functions to story_screen.fab
  - Move start screen function to start_screen.fab
- Use CHR bank switching for `bg.png` and `font.png` (with `MapFab`)
- Fer can run
- Lucifer can run for certain amount of time 
  - Flies ~2,5s
  - After that, ~5

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
