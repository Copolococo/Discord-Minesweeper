import numpy as np
import random

def generate_level(levelHeight=14, levelWidth=14, numMines=50):
    level = [[0 for j in range(levelWidth)] for i in range(levelHeight)]

    available_pos = list(range((levelWidth) * (levelHeight)))
    random.shuffle(available_pos)
    mines = available_pos[:numMines]
    
    for mine in mines:
        x, y = mine % levelWidth, mine // levelWidth
        level[y][x] = 'X'
        
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                posX, posY = x+i, y+j
                if 0 <= posX < levelWidth and 0 <= posY < levelHeight:
                    if level[posY][posX] != 'X':
                        level[posY][posX] += 1
    return level
