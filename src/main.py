from environment import create_grid
from path_planner import astar
from visualization import show
from navigator import move_agent

grid = create_grid(20, 0.2)

start = (0, 0)
goal = (19, 19)

path = astar(grid, start, goal)

print("Generated Path:")
print(path)

move_agent(path)

show(grid, path, start, goal)