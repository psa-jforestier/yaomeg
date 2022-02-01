# Code name : YAOMEG
** Yet An Other Maze Escape Game

This is a draft idea for a mobile application, code named YAOMEG (definitive name not choosen yet).
The goal is to run in a 2D-up-view of a pre-defined maze, to escape from an explosion that is going to blow the maze and kill the user.

You will never escape from the maze, because it is an infinite labyrinth. You only need to run as far as possible from the center of the maze. Your score will be the distance you run from the maze (in straight line). The maze is not random, so you can compare your score with other players.

Gameplay : (still to be defined)
- Time limited game : you have 1mn and an unlimited number of move to go as far as possible
- Move limited game : you have 100 steps to go as far as possible, without time limit
- Life limited game : you have 100% life, you lose 1% every step and 1% every second if you don't move.

If it is time based, only the fastest player will have high score, which is not very fair.

Some special items are available in a maze cell :
- +time : add 10s second before the explosion
- +life : add 10 of life 
- warp : teleport to an other cell (teleportation is in both way, you are always teleported to the same cell)
- ghost : walk thru wall for 10 moves or 10s

There is 3 levels of difficulties : Easy, Medium, Hard. They have impacts on complexity of the maze and on items apparition. But a maze look almost the same whatever the difficulty is.

How the Maze works :
- You view only a window of 32x32 cells of the maze.
- A cell maze is a 3x3 matrix sub-cells. Each sub-cells is a wall (#) or not (·)
- there is 17 pre-defined maze cell type : 
```
Basic turn corridor (0..3)
###   ###   #·#   #·#
#··   ··#   ··#   #··
#·#   #·#   ###   ###

Round about, go every direction (4..7)
#·#   ···   #··   ··#
···   ·#·   ···   ···
#·#   ···   ··#   #··

T junctions (8..11)
#·#   ###   #·#   #·#
···   ···   #··   ··#
###   #·#   #·#   #·#

Straight (12, 14)
#·#   ###
#·#   ···
#·#   ###

Other (14..16)
·#·   #··   ·#·
###   ··#   ···
·#    #··   #·#

```
- in Easy mode, the `Other` type is replaced by round abouts (4, 5 and 6)

- The user start at (0,0), which is the center of the Maze
- He can go Left, Up, Down, Right if there is no wall.
- There is no limit of X and Y value. For convenience, we roll the value from -2 147 483 648 to 2 147 483 647 (32 bits signed integer)
- The cell value (one from 14 types) is computed based on the coordinate (X,Y) of the user.
  - The formula is predictible, it is not randomly based
  - It can be something simple like `(X * Y) modulo 14`
  - Or more mathematical like `md5("X.Y.hash") modulo 14`
  - Or a something like a Perlin noise (based on left and right bit rotations)

Special items are not randomized, they are also placed predictively with the same formula but with a different seed :
- X,Y formula modulo `(5+d) * 17`, where d is difficulty level (d = 1 for Easy, 2 for Medium, 3 for hard)
- if 0 : clock +10s
- if 1 : life +10%
- if 2 : warp (teleportation)
- if 3 : ghost
An item is placed at the center of the cell and must always be accessible, it must not be surround by wall. So we could not have an item on cell `Other 14`

How the Warp teleportation work : when a user arrive on a Warp cell, it is warped to an other cell. If he arrives on a Warp cell by the left of the warp, the game search for an other warp cell at the right of the current cell, in the 16 rights cols and 32 lines. If there are several warp arrival, the game choose the nearest (by computing cell distance). If there are several warp arrival with the same distance, the game select the 1st find when scanning the cells. If there is no warp arrival cell on the right of the player, the game scan the 32x32 view window and find the nearest cell as above. If there is no warp arrival in the view port, the game jump the user 2 cells at his right.
If the user arrives on a warp cell by the right of the warp, same as above but we scan on the left of the user. Same principle for up and down.