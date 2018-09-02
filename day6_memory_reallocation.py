"""
Day 6: Memory Reallocation
"""
from math import ceil

def memory_reallocate(banks):
    configs = {}
    cycle = 0
    while True:
        banks_key = tuple(banks)
        if banks_key in configs:
            return (configs[banks_key], cycle)
            break
        configs[banks_key] = cycle
        mem_to_alloc = max(banks)
        i_max = banks.index(mem_to_alloc)
        share = int(ceil(mem_to_alloc/len(banks)))
        banks[i_max] = 0
        for i in range(0, len(banks)):
            index = (i_max + i + 1) % len(banks)
            if share <= mem_to_alloc:
                banks[index] += share
                mem_to_alloc -= share
            else:
                banks[index] += mem_to_alloc
        cycle += 1


banks = [0, 2, 7, 0]
begin_cycle, end_cycle = memory_reallocate(banks)
assert end_cycle == 5
assert (end_cycle - begin_cycle) == 4

if __name__ == "__main__":
    INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
    begin_cycle, end_cycle = memory_reallocate(INPUT.copy())
    print(end_cycle)
    print(end_cycle - begin_cycle)

