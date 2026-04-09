import matplotlib.pyplot as plt
import os

def show(grid, path, start, goal):
    plt.imshow(grid, cmap='gray')

    x = [p[1] for p in path]
    y = [p[0] for p in path]

    plt.plot(x, y, color='red', linewidth=2)
    plt.scatter(start[1], start[0], color='green', s=100)
    plt.scatter(goal[1], goal[0], color='blue', s=100)

    plt.title("Autonomous Navigation System")

    os.makedirs("outputs/images", exist_ok=True)
    plt.savefig("outputs/images/result.png")

    plt.show()