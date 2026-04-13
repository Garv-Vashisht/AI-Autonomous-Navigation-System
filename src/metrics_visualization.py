import numpy as np
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("outputs/images", exist_ok=True)


# 🔹 1. CONFUSION MATRIX (DEMO)
def generate_confusion_matrix():
    cm = np.array([[45, 5],
                   [3, 47]])

    plt.figure()
    plt.imshow(cm)
    
    # Add numbers inside matrix
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j], ha='center', va='center')

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig("outputs/images/confusion_matrix.png")
    plt.close()

    print("✅ Confusion matrix saved!")


# 🔹 2. PATH VISUALIZATION (FROM YOUR PROJECT)
def generate_path_visualization(grid, path, start, goal):
    plt.figure()
    plt.imshow(grid, cmap='gray')

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y)
    
    plt.scatter(start[1], start[0])
    plt.scatter(goal[1], goal[0])

    plt.title("Path Visualization")

    plt.savefig("outputs/images/path_visualization.png")
    plt.close()

    print("✅ Path visualization saved!")


# 🔹 3. ACCURACY GRAPH (DEMO)
def generate_accuracy_graph():
    epochs = np.arange(1, 11)
    accuracy = np.linspace(0.6, 0.95, 10)

    plt.figure()
    plt.plot(epochs, accuracy)

    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.title("Model Accuracy")

    plt.savefig("outputs/images/accuracy_graph.png")
    plt.close()

    print("✅ Accuracy graph saved!")