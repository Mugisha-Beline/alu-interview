#!/usr/bin/python3
"""
    Find the maximum amount of rain that the array's walls can withstand.
"""


def rain(walls):
    """
        Find the maximum amount of rain that the array's walls can withstand.
    """
    water_temp = 0
    water = 0
    size = len(walls)
    prev_wall = 0

    # If list is empty return 0.
    if size <= 0:
        return water_temp

    for a in range(size):

        if walls[a] >= walls[prev_wall]:
            prev_wall = a
            water_temp = 0
        else:
            water += walls[prev_wall] - walls[a]
            water_temp += walls[prev_wall] - walls[a]

    if prev_wall < size - 1:

        # Subtract last temp volume from total.
        water -= water_temp
        # Store last peak wall.
        prev_pass_peak = prev_wall
        prev_wall = size - 1

        for a in range(size - 1, prev_pass_peak, -1):

            if walls[a] >= walls[prev_wall]:
                prev_wall = a
            else:
                water += walls[prev_wall] - walls[a]

    return water
