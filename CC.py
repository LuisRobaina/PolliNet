
# Pollinator base.
# wait few seconds get the first reading of Lon Lat.
BASE = (0,0)

# Tasks Queue.
taskQueue = []

# Notification queue.
# Once a pollinator is done it should send a notification to the CC.


class Task:
    def __init__(self, taskType, lat, lon):
        self.type = taskType
        self.lat = lat
        self.lon = lon


# Use matplot lib for a real time graph of the drones positions.
# while there is no notifications to take care of.

# Rule Based drone control system for large drone.
# -----------------------
# Decision Tree.
# define Max distance from base in x and y.
# set and keep a steady high.

# Loop thruogh the tasks and figure out closest pollinator to this task.
# If no task then return pollinators to base.
# Should pollinators talk to the CC ? Should we calculate time to next task using physics.

# If the control center fails (time out). Pollinators should return home.

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

for t in range(10):
    if t == 0:
        points, = ax.plot(x, y, marker='o', linestyle='None')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
    else:
        new_x = np.random.randint(10, size=5)
        new_y = np.random.randint(10, size=5)
        points.set_data(new_x, new_y)
    plt.pause(0.5)