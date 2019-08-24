# Simulation of a Randomized Rule Base Nav System.

import matplotlib.pyplot as plt
import time
import random

# Home coordinates.
LAT, LONG = [25.5308], [80.1834]

fig, ax = plt.subplots()

# Drone should no fly more than (5) meters in any direction from home
LAT_MAX, LAT_MIN = LAT[0] + 0.00018, LAT[0] - 0.00018
LONG_MAX, LONG_MIN = LONG[0] + 0.00018, LONG[0] - 0.00018

print('Pre-processing done.')

lat_num, long_num, q = 0, 0, 0
last_dir = 0

while (True):
    if q == 0:
        # Initial position.
        points, = ax.plot(LAT, LONG, marker='o', linestyle='None')
        ax.set_xlim(LAT_MIN , LAT_MAX)
        ax.set_ylim(LONG_MIN, LONG_MAX)
        ax.ticklabel_format(useOffset=False)

    else:
        nav_start = time.time()
        dir = random.randint(0, 3)

        if (q != 0):
            while (abs(dir - last_dir) == 2): dir = random.randint(0, 3)

        while time.time() - nav_start <= 0.5:
            last_dir = dir
            if dir == 0:
                if (LONG[0] + 0.0000005) <= LONG_MAX - 0.00002:
                    LONG[0] = (LONG[long_num] + 0.000005)
            elif dir == 1:
                if (LAT[lat_num] + 0.0000005) <= LAT_MAX  - 0.00002:
                    LAT[0] = (LAT[lat_num] + 0.0000005)

            elif (dir == 2):
                if (LONG[0] - 0.0000005) >= LONG_MIN + 0.00002:
                    LONG[0] = (LONG[long_num] - 0.0000005)

            else:
                if (LAT[0] - 0.0000005) >= LAT_MIN + 0.00002:
                    LAT[0]= (LAT[lat_num] - 0.0000005)

            points.set_data(LAT, LONG)
            plt.pause(0.001)
    q += 1
