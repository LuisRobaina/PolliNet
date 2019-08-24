
# Pollinator base.
# wait few seconds get the first reading of Lon Lat.
BASE = (0,0)

# Tasks Queue.
taskQueue = []

# Notification queue.
# Once a pollinator is done it should send a notification to the CC.

# Defines a Task.
class Task:
    def __init__(self, taskType, lat, lon):
        self.type = taskType
        self.lat = lat
        self.lon = lon


# Use matplot lib for a real time graph of the drones positions.


# Rule Based drone control system for scout drone.
# -----------------------
# define Max distance from base in x and y.
# set and keep a steady high.

# Loop through the tasks and figure out closest pollinator to this task.
# If no task then return pollinators to base.
# Should pollinators talk to the CC ? Should we calculate time to next task using physics.

# If the control center fails (time out). Pollinators should return home.
