import numpy as np
import random

def create_grid(size=20, obstacle_prob=0.2):
    grid = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_prob:
                grid[i][j] = 1

    return grid