


class DuelingGenerator:
    DIVISOR=2147483647

    def __init__(self, factor, start, multiple=1):
        self.current = start
        self.factor = factor
        self.start = start
        self.multiple = multiple

    def __iter__(self):
        return self

    def next(self):
        while True:
            val = (self.current * self.factor) % DuelingGenerator.DIVISOR
            self.current = val
            if val % self.multiple == 0:
                return val

    def reset(self):
        self.current = self.start


MASK = 2**16 - 1
def judge(genA, genB, n):
    match_count = 0
    for i in range(n):
        if i % 100000 == 0:
            print("i =",i)
        valA = genA.next() & MASK
        valB = genB.next() & MASK
        if valA == valB:
            match_count += 1
    return match_count

test_genA = DuelingGenerator(16807, 65)
test_genB = DuelingGenerator(48271, 8921)

assert judge(test_genA, test_genB, 5) == 1

test_genA4 = DuelingGenerator(16807, 65, multiple=4)
test_genB8 = DuelingGenerator(48271, 8921, multiple=8)

assert judge(test_genA4, test_genB8, 1056) == 1


if __name__ == "__main__":
    startA = 512
    startB = 191

    genA = DuelingGenerator(16807, 512)
    genB = DuelingGenerator(48271, 191)
    # print(judge(genA, genB, 40000000))

    genA4 = DuelingGenerator(16807, 512, multiple=4)
    genB8 = DuelingGenerator(48271, 191, multiple=8)
    print(judge(genA4, genB8, 5000000))
