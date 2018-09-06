from day10_knot_hash import knot_hash

def make_grid(prefix):

    grid = []
    for row in range(128):
        khash = knot_hash("{}-{}".format(prefix,row))
        khash_bits = ""
        for c in khash:
            i = int(c, base=16)
            khash_bits += "{:04b}".format(i)
        #print(khash_bits[0:8])
        grid.append(khash_bits)
    return grid

def used_count(memory_grid):
    count = 0
    for row in memory_grid:
        for c in row:
            if c == "1":
                count += 1
    return count


def get_adjacent(memory_grid, r, c):
    adjacent = set()
    if r > 0:
        l = memory_grid[r-1][c]
        if l == "1":
            adjacent.add((r-1, c))
    if r < len(memory_grid) - 1:
        l = memory_grid[r+1][c]
        if l == "1":
            adjacent.add((r+1, c))
    if c > 0:
        l = memory_grid[r][c-1]
        if l == "1":
            adjacent.add((r, c-1))
    if c < len(memory_grid[r]) - 1:
        l = memory_grid[r][c+1]
        if l == "1":
            adjacent.add((r, c+1))
    return adjacent


def find_regions(memory_grid):
    region_map = {}
    for r in range(len(memory_grid)):
        for c in range(len(memory_grid[r])):
            if memory_grid[r][c] == "1":
                adjacents = get_adjacent(memory_grid, r, c)
                # merge the current point and its adjacent points
                # along with the points in their regions into one set
                merge_set = set(adjacents)
                merge_set.add((r,c))
                for a in adjacents:
                    if a in region_map:
                        a_set = region_map[a]
                        merge_set.update(a_set)
                # assign all of the points in this set to the same set
                for a in merge_set:
                    region_map[a] = merge_set
    return region_map

test_input = "flqrgnkx"
test_grid = make_grid(test_input)
assert used_count(test_grid) == 8108

if __name__ == "__main__":
    input = "nbysizxe"
    memory_grid = make_grid(input)
    print(used_count(memory_grid))
    regions = find_regions(memory_grid)
    region_set = set()
    # Count unique sets in the regino hash
    for cset in regions.values():
        clist = list(cset)
        clist.sort()
        ckey = str(clist)
        region_set.add(ckey)
        
    print(len(region_set))
