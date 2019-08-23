import matplotlib.pyplot as plt
import time
import random

# Pick a direction at random.
# Out of bounds ?
# Move for t seconds,

# Home coordinates.
LAT, LONG = [25.5308, 25.53095 ], [80.1834, 80.18355]

fig, ax = plt.subplots()

# Drone should no fly more than $(5) meters in any direction from home
LAT_MAX, LAT_MIN = LAT[0] + 0.00018, LAT[0] - 0.00018
LONG_MAX, LONG_MIN = LONG[0] + 0.00018, LONG[0] - 0.00018

print('Pre-processing done.')

lat_num, long_num, q = 0, 0, 0
last_dir = 0

while (True):
    if q == 0:
        # Initital position.
        points, = ax.plot(LAT, LONG, marker='o', linestyle='None')
        ax.set_xlim(LAT_MIN, LAT_MAX)
        ax.set_ylim(LONG_MIN, LONG_MAX)
        ax.ticklabel_format(useOffset=False)

    else:
        nav_start = time.time()
        dir = random.randint(0, 3)

        if (q != 0):
            while (abs(dir - last_dir) == 2): dir = random.randint(0, 3)

        while time.time() - nav_start <= 1:
            last_dir = dir
            if dir == 0:
                if (LONG[0] + 0.0000045) <= LONG_MAX:
                    LONG[0] = (LONG[long_num] + 0.0000045)

            elif dir == 1:
                if (LAT[lat_num] + 0.0000045) <= LAT_MAX:
                    LAT[0] = (LAT[lat_num] + 0.0000045)

            elif (dir == 2):
                if (LONG[0] - 0.0000045) >= LONG_MIN:
                    LONG[0] = (LONG[long_num] - 0.0000045)

            else:
                if (LAT[0] - 0.0000045) >= LAT_MIN:
                    LAT[0]= (LAT[lat_num] - 0.0000045)

            points.set_data(LAT, LONG)
            plt.pause(0.001)
    q += 1
