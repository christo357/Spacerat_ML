""" Main python file used to run code and get the results in terminal.
"""

import os
import random

from ship import Ship
import bot2 as bot2s

# Constants
SIZE = 30
ALPHA = .1
CELL_SIZE = 15
RANDOM_SEED = random.randint(0, 10000)
GRID_WIDTH = SIZE
GRID_HEIGHT = SIZE
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FIRE_COLOR = (255, 69, 0)

resultFolder = "results"
        
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


my_ship = Ship(SIZE, RANDOM_SEED)
my_ship.createShip()
r_b, c_b = random.choice(my_ship.getOpenCells())
print(f"initial bot loc : {r_b, c_b}")
my_ship.start_botloc =  (r_b, c_b)
rat_init = my_ship.getRatloc()


## Bot  2 with stationary rat
my_ship.setRatloc(rat_init)
b_resultPath = resultFolder+"/b"
b_simPath = resultFolder+"/sims"
create_folder_if_not_exists(b_resultPath)
create_folder_if_not_exists(b_simPath)
b_path = f"{b_resultPath}/{SIZE}_{ALPHA}"
my_bot2s = bot2s.Bot(my_ship, r_b, c_b,alpha=ALPHA, seed=RANDOM_SEED, resultPath = b_path, simPath=b_simPath)
getPos = my_bot2s.findPosition()
steps = my_bot2s.findRat()
bot_rat = my_ship.getRatPositions()
    
 

print()
print("Improved bot (moving  rat)")
print("------------------------------")
print(f"Steps for localization: {getPos}")
print(f"Total steps: bot2s: {steps}, rat found at: {bot_rat}")


