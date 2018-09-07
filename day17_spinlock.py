
def spinlock(step, num_spins):
    buffer = [0]
    curr_pos = 0
    curr_val = 0
    for c in range(num_spins):
        if c % 100000 == 0:
            print("c =", c)
        curr_val += 1
        spin_pos = (curr_pos + step) % len(buffer)
        # print("spin_pos =", spin_pos)
        buffer.insert((spin_pos + 1) % (len(buffer) + 1), curr_val)
        curr_pos = spin_pos + 1
    return buffer[(curr_pos + 1) % len(buffer)]

assert spinlock(3, 2017) == 638

if __name__ == "__main__":
    print(spinlock(337, 2017))
    # print(spinlock(337, 50000000))
