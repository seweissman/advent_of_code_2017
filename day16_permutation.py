from collections import deque

import re

def spin(d, n):
    for i in range(n):
        v = d.pop()
        d.appendleft(v)
    return d

TEST = deque("abcde")
assert spin(TEST, 3) == deque("cdeab")

def exchange(d, n, m):
    val = d[n]
    d[n] = d[m]
    d[m] = val
    return d

TEST = deque("abcde")
assert exchange(TEST, 1, 2) == deque("acbde")

def partner(d, a, b):
    i = d.index(a)
    j = d.index(b)
    return exchange(d, i, j)

TEST = deque("abcde")
assert partner(TEST, "b", "c") == deque("acbde")

def dance(d, instructions):
    for instruction in instructions:
        m = re.match("s(\d+)", instruction)
        if m:
            i = int(m.group(1))
            d = spin(d, i)
        m = re.match("x(\d+)/(\d+)", instruction)
        if m:
            i = int(m.group(1))
            j = int(m.group(2))
            d = exchange(d, i, j)
        m = re.match("p([a-z])/([a-z])", instruction)
        if m:
            a = m.group(1)
            b = m.group(2)
            d = partner(d, a, b)
    return d

TEST = deque("abcde")
TEST_DANCE = "s1,x3/4,pe/b"
TEST_INSTRUCTIONS = TEST_DANCE.split(",")
assert dance(TEST, TEST_INSTRUCTIONS) == deque("baedc")

def find_cycle(d, instructions):
    dcopy = d.copy()
    i = 0
    while True:
        i += 1
        if i % 100000 == 0:
            print("i =", i)
        d = dance(d, instructions)
        if d == dcopy:
            return i

#TEST = deque("abcde")
#print(find_cycle(TEST, TEST_INSTRUCTIONS))

if __name__ == "__main__":
    with open("day16.input.txt") as f:
        input = f.read()
        instructions = input.split(",")
        d = deque("abcdefghijklmnop")
        assert len(d) == 16
        print("".join(dance(d, instructions)))
        d = deque("abcdefghijklmnop")
        c = find_cycle(d, instructions)
        # one billion steps mod cycle size
        n = 1000000000 % c
        d = deque("abcdefghijklmnop")
        for i in range(n):
            d = dance(d, instructions)
        print("".join(d))
