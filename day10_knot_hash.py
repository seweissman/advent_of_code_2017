"""
Day 10: Knot Hash
"""
from math import ceil
def reverse_list_slice(l, i, length):
    #print("reverse_list_slice", i, length)
    for k in range(0, length//2):
        #print("l begin",l)
        #print("swap values", l[(i+k)%len(l)], l[(i + length - k - 1)%len(l)])
        x = l[(i+k)%len(l)]
        l[(i+k)%len(l)] = l[(i + length - k - 1)%len(l)]
        l[(i + length - k - 1)%len(l)] = x
        #print("l end",l)

def knot_hash_round(knot, lengths, position=0, skip=0):
    skip_size = skip
    current = position
    for length in lengths:
        #print("knot ", knot)
        #print(length, skip_size, current)
        reverse_list_slice(knot, current, length)
        current += length + skip_size
        skip_size += 1
    return(current, skip_size)

knot1 = [x for x in range(0,5)]
lengths1 = [3, 4, 1, 5]
knot_hash_round(knot1, lengths1)
assert knot1 == [3, 4, 2, 1, 0]

STANDARD_LENGTH_SUFFIX = [17, 31, 73, 47, 23]

def str_to_lengths(s):
    lengths = []
    s_ascii = s.encode("ASCII")
    for i in range(0,len(s_ascii)):
        lengths.append(s_ascii[i])
    return lengths

assert str_to_lengths("1,2,3") == [49,44,50,44,51]

def knot_hash(s):
    knot = [x for x in range(0,256)]
    lengths = str_to_lengths(s)
    lengths.extend(STANDARD_LENGTH_SUFFIX)

    position = 0
    skip = 0
    for round in range(0,64):
        # print(knot)
        position, skip = knot_hash_round(knot, lengths,
                                         position=position,
                                         skip=skip)
    hex_hash = ""
    for i in range(0,16):
        xor = 0
        for j in range(i*16,(i+1)*16):
            xor ^= knot[j]
        hex_string = '{:02x}'.format(xor)
        hex_hash += hex_string
    return hex_hash


assert knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

if __name__ == "__main__":
    KNOT = [x for x in range(0,256)]
    LENGTHS = [147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70]
    knot_hash_round(KNOT, LENGTHS)
    # print(KNOT)
    print(KNOT[0]*KNOT[1])
    INPUT = "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70"
    print(knot_hash(INPUT))



