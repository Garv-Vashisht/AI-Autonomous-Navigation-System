from metrics_visualization import (
    generate_confusion_matrix,
    generate_path_visualization,
    generate_accuracy_graph
)
from environment import create_grid
from path_planner import astar
from visualization import show
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("outputs/images", exist_ok=True)

# Step 1: Create grid
grid = create_grid(20, 0.2)

# Save GRID IMAGE (2nd image)
plt.imshow(grid, cmap='gray')
plt.title("Grid Environment")
plt.savefig("outputs/images/grid_environment.png")
plt.close()

# Step 2: Define start and goal
start = (0, 0)
goal = (19, 19)

# Step 3: Find path
path = astar(grid, start, goal)

print("Generated Path:", path)

# Save PATH VISUALIZATION (3rd image)
plt.imshow(grid, cmap='gray')
x = [p[1] for p in path]
y = [p[0] for p in path]
plt.plot(x, y)
plt.scatter(start[1], start[0])
plt.scatter(goal[1], goal[0])
plt.title("Path Visualization")
plt.savefig("outputs/images/path_visualization.png")
plt.close()

# Final output (already existing)
show(grid, path, start, goal)


# Generate additional visuals
generate_confusion_matrix()
generate_path_visualization(grid, path, start, goal)
generate_accuracy_graph()