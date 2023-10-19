# ToDo:
- System
  - Add states and screens
    - Start
    - Pause
    - Win
    - Game Over
- Bugs
  - Fix START state
    - Fix transition to STORY
- Fix transition from STORY to PLAY
  - Only when starting at START
- Graphs
  - Make tiles according to game
  - Make proper maps
    - Don't scroll
    - Make Arcade screens and map
  - Improve animations
- Data handling
  - Store Player data somewhere, instead of creating them all the time
- Game experience
  - Improve story
  - Add enemies
  - Add bosses

# Changes

## [18.10.2023]
- Move player variables and functions to player.fab
- Move story screen variables and functions to story_screen.fab
- Move start screen function to start_screen.fab
- Use bank switching for bg.png and font.png (with MapFab)

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
