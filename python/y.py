#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
import curses
import sys
import screen
global MAZE_WALLS
MAZE_WALLS = [
"""
###
#··
#·#
""",
"""
###
··#
#·#
""",
"""
#·#
··#
###
""",
"""
#·#
#··
###
""",
"""
#·#
···
#·#
""",
"""
#·#
···
###
""",
"""
###
···
#·#
""",
"""
#·#
#··
#·#
""",
"""
#·#
···
#·#
""",
"""
#·#
#·#
#·#
""",
"""
###
···
###
""",
"""
#··
···
··#
""",
"""
··#
···
#··
""",
"""
···
·#·
···
""",# other (for easy mode, they  are round abouts)
"""
·#·
###
·#·
""",
"""
#··
··#
#··
""",
"""
·#·
···
#·#
"""
]

import rng
from curses import wrapper
"""
function getCellType(x,y,seed)
{
  mix = xorShift64(x) + (xorShift64(y) << 32) + 0xCAFEBABE + seed;
  return xorShift64(mix);
}

function xorShift64( a) {
    a ^= (a << 21);
    a ^= (a >>> 35);
    a ^= (a << 4);
    return a;
}

"""
def get_cell_wall(x,y, seed=0):

  mix = xorShift64(x) + (xorShift64(y) << 32) + 0xCAFEBABE + seed
  return xorShift64(mix)
def xorShift64(a):
  a ^= (a << 21);
  a ^= (a >> 35); # unsigned right shift
  a ^= (a << 4);
  return a;
def print_maze(x,y, ratio):
# assume x and y is the absolute coordinate of the maze (0,0 is the center of the maze)
  global MAZE_WALLS
  """for i in range(x-8, x+8):
    for j in range(y-8, y+8):
      cellid = abs(get_cell_wall(i,j)) % len(MAZE_WALLS)
      print_cell(i+8, j+8, ratio, cellid)
  screen.printfxy((8 * 3 * ratio)  + 1, (8 * 3) + 1, "!")
  """
  for i in range(-8, +8):
    for j in range(-8, +8):
      cellx = x + i
      celly = y + j
      cellid = abs(get_cell_wall(cellx,celly)) % len(MAZE_WALLS)
      print_cell(i+8, j+8, ratio, cellid)
  screen.printfxy((8 * 3 * ratio)  + 1, (8 * 3) + 1, "!")
def print_cell(x,y, ratio, cellid, color=0):
# x,y are relative coordinates (0,0 is the top left cell)
  global MAZE_WALLS
  absoluteX = x * (ratio*3)
  absoluteY = y * 3
  cell_design = (MAZE_WALLS[cellid]).strip()
  for i in range(0,3*ratio, ratio):
    for j in range(0,3):
      w = cell_design[(j*4) + (i//ratio)]
      if (w == '#'): 
        c = "█"
      else:
        c = " "
      for r in range(0, ratio):
        screen.printfxyc(absoluteX + i + r, absoluteY + j, color, c)
      
def ask_for_ratio():
    screen.printfxy(0,0,"Which one look like a square ?=:")
    screen.printfxy(0,1,"1 : █     2 : ██     3 : ███")
    square = screen.promptxy(0,2, "1, 2 or 3 ?")
    if (square=="2"):
      return 2
    return 0


def main(stdscr):
  screen.init()
  if (screen.curses.LINES < 32 or screen.curses.COLS < 2*32):
    print("Your terminal must be at least 32x64")
    quit()

  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
  curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
  #ratio = ask_for_ratio()
  ratio = 2
  
  
  playerX = 0 # player position
  playerY = 0
  while(True):
    print_maze(playerX, playerY, 2)
    screen.refresh()    
    while(not screen.iskeypressed()):
      #print("in the loop...")
      time.sleep(0.1)
    k = screen.getlastkeypressed()
    if (k == screen.curses.KEY_UP):
      playerY = playerY - 1
    elif (k == screen.curses.KEY_DOWN):
      playerY = playerY + 1
    elif (k == screen.curses.KEY_LEFT):
      playerX = playerX - 1
    elif (k == screen.curses.KEY_RIGHT):
      playerX = playerX + 1
    print("You quit with ", k, "which is ", curses.keyname(k) )
  #      123456

if __name__ == "__main__":
  wrapper(main)