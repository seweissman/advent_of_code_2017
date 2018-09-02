"""
Day 3: Spiral Memory
"""

from math import sqrt
from math import floor
from collections import defaultdict

def nearest_odd_lte_sqrt(n):
    f = floor(sqrt(n))
    if f%2 == 0:
        return f - 1
    return f

def num_to_x_y(n):
    """
    Map a number in the grid to its x, y coordinate
    """
    ring = nearest_odd_lte_sqrt(n)
    diff = (n - ring ** 2) - 1
    side = diff//(ring+1)
    offset = (diff % (ring + 1)) + 1
    # Special case for a perfect square
    if diff == -1:
        return (int(ring//2), -int(ring//2))
    # We are on the right
    if side == 0:
        x = int((ring + 1)//2)
        y = int(-(ring + 1)//2 + offset)
        return (x, y)
    # We are on the top
    if side == 1:
        y = int((ring + 1)//2)
        x = int((ring + 1)//2 - offset)
        return (x,y)
    # We are on the left
    if side == 2:
        x = int(-(ring + 1)//2)
        y = int((ring + 1)//2 - offset)
        return (x, y)
    # We are on the bottom
    if side == 3:
        y = int(-(ring + 1)//2)
        x = int(-(ring + 1)//2 + offset)
        return (x, y)
    # We are in a maze of twisty passages
    else:
        raise ValueError("Found side=%d, but side cannot be larger than 3",
                         side)
#print(num_to_x_y(1))


#    3^2 + 4*4 = 5^2
#    5^2 + 6*4 = 7^2

# (n + 2)^2 = n^2 + 4(n+1)

# n^2 = (n-2)^2 + 4(n-1)

# m find the two odd numbers its square root is between
# 24 is between 3^2 and 5^2
# 24 - 9 = 15
# 15//4 = 3 --> y = -2
# 15%4 = 3 --> x = -2 + 3

# 12 is between 9 and 25
# 12 - 9 = 3
# 3//4 = 0 --> x = 2
# 3%4 = 3 --> y = -2 + 3

# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49
def manhattan_distance(p1, p2):
    d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return d

def memory_distance(n):
    return manhattan_distance((0,0), num_to_x_y(n))

assert(memory_distance(1) == 0)
assert(memory_distance(12) == 3)
assert(memory_distance(23) == 2)
assert(memory_distance(1024) == 31)

# Surrounding points
# p1 p2 p3
# p4 c  p5
# p6 p7 p8
def get_surrounding_points(coord):
    p1 = (coord[0]-1, coord[1]-1)
    p2 = (coord[0], coord[1]-1)
    p3 = (coord[0]+1, coord[1]-1)
    p4 = (coord[0]-1, coord[1])
    p5 = (coord[0]+1, coord[1])
    p6 = (coord[0]-1, coord[1]+1)
    p7 = (coord[0], coord[1]+1)
    p8 = (coord[0]+1, coord[1]+1)
    return [p1, p2, p3, p4, p5, p6, p7, p8]

def spiral_sum(stop_number):
    grid = defaultdict(int)
    grid_sum = 1
    i = 1
    coord = num_to_x_y(i)
    grid[coord] = 1
    while grid_sum <= stop_number:
        i += 1
        coord = num_to_x_y(i)
        points = get_surrounding_points(coord)
        grid_values = [grid[p] for p in points]
        grid_sum = sum(grid_values)
        grid[coord] = grid_sum
    return grid_sum


#147  142  133  122   59
#304    5    4    2   57
#330   10    1    1   54
#351   11   23   25   26
#362  747  806--->   ...

assert(spiral_sum(1) == 2)
assert(spiral_sum(2) == 4)
assert(spiral_sum(4) == 5)
assert(spiral_sum(5) == 10)
assert(spiral_sum(10) == 11)
assert(spiral_sum(11) == 23)
assert(spiral_sum(23) == 25)
assert(spiral_sum(25) == 26)
assert(spiral_sum(26) == 54)
assert(spiral_sum(26) == 54)
assert(spiral_sum(54) == 57)
assert(spiral_sum(57) == 59)
assert(spiral_sum(59) == 122)
assert(spiral_sum(122) == 133)
assert(spiral_sum(142) == 147)
assert(spiral_sum(147) == 304)
assert(spiral_sum(304) == 330)
assert(spiral_sum(351) == 362)
assert(spiral_sum(362) == 747)
assert(spiral_sum(747) == 806)

if __name__ == "__main__":
    print(memory_distance(325489))
    print(spiral_sum(325489))


