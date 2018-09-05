from collections import defaultdict

# The order of the steps doesn't matter, so the distance
# function is very simple
def dist(counts):
    n = abs(counts["n"] - counts["s"])
    nw = abs(counts["nw"] - counts["se"])
    ne = abs(counts["ne"] - counts["sw"])
    return n + max(ne,nw)

if __name__ == "__main__":
    counts = defaultdict(int)
    with open("day11.input.txt") as f:
        INPUT = f.read().strip()
        dir_list = INPUT.split(",")
        # The order of the steps doesn't matter so we just need
        # to count each type of step
        for dir in dir_list:
            counts[dir] += 1

    print(dist(counts))

    counts = defaultdict(int)
    with open("day11.input.txt") as f:
        INPUT = f.read().strip()
        dir_list = INPUT.split(",")
        # print(dir_list)
        max_d = -1
        for dir in dir_list:
            # Keep running counts and check for distance at every
            # step to find max
            counts[dir] += 1
            max_d = max(max_d,dist(counts))
        print("max=", max_d)
    
