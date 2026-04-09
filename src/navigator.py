import time

def move_agent(path):
    for step in path:
        print("Moving to:", step)
        time.sleep(0.1)