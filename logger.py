from ship import Ship
import json
import pandas as pd
import os
import numpy as np
from datetime import datetime

class Logger():
    def __init__(self, size, ship, resultPath, simPath):
        self.size = size
        self.ship = ship
        self.resultPath = resultPath
        self.simPath = simPath
        self.bot_start = (0,0)
        self.ship_list = self.createShipList()

    def createShipList(self):
        ship_list = np.zeros((30,30))
        for row in range(self.size):
            for col in range(self.size):
                val = self.ship.get_cellval(row,col)
                if val=='o':
                    ship_list[row][col] = 1
                else:
                    ship_list[row][col] =0
        return ship_list.tolist()
                    
    def log_metadata(self):
        
        with open(self.resultPath, "w") as file:
            file.write(f"Grid Size: {self.size}x{self.size}\n")
            bot_row, bot_col = self.ship.getStartBotLoc()
            rat_row, rat_col = self.ship.getRatloc()
            file.write(f"Initial Bot Location: ({bot_row}, {bot_col})\n")
            file.write(f"Rat Location: ({rat_row}, {rat_col})\n")
            file.write("-" * 40 + "\n")
            
    def log_grid_state(self, timestep, bot, rat, loc_find = 0):
        with open(self.resultPath, "a") as file:
            file.write(f"Timestep: {timestep}\n")
            for row in range(self.size):
                for col in range(self.size):
                    v = self.ship.get_cellval(row, col)
                    file.write(f"{v} ")
                file.write("\n")
            
            if isinstance(loc_find, tuple) and len(loc_find) == 2 and all(isinstance(i, int) for i in loc_find):
                self.bot_start = loc_find
            
            file.write(f"Bot start: {self.bot_start}\n")
            file.write(f"Bot: {bot}\n")
            file.write(f"Rat: {rat}\n")
            file.write("-" * 40 + "\n")      
            
            
    def log_belief(self, belief_list, step_list , tot_steps,bot_loc, output_folder):
        data = []
        remaining_steps = list(reversed(step_list))
        (r, c)= bot_loc
        self.ship_list[r][c] = -1
        for belief, steps, r_steps in zip(belief_list, step_list, remaining_steps):
            belief_as_list = belief.tolist()  
            
            data.append([belief_as_list,self.ship_list,steps, r_steps]) 
        df = pd.DataFrame(data, columns=["belief",
                                         "ship",
                                         "steps",
                                         "remain"])
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        csv_file = os.path.join(output_folder, f"{timestamp}.csv")

        df.to_csv(csv_file, index=False)

        print(f"Data saved to {csv_file}")
        return csv_file
    
    def log_botposition(self,  timestep, bot_count):
        with open(self.resultPath, "a") as file:
            file.write(f"Timestep: {timestep}\n")
            for i in range(bot_count):
                bot_row, bot_col = self.ship.getBotLoc(i)
                file.write(f"({i}, {i})",end = ",")
            rat_row, rat_col = self.ship.getRatloc()
            file.write(f"({rat_row}, {rat_col})")
            file.write("-" * 40 + "\n")
            
    