"""
Day 1: Inverse Captcha
"""

def sum_match_next(digit_str):
    digits = [int(c) for c in digit_str]
    sum = 0
    for i, c in enumerate(digits):
        if c == digits[(i+1)%len(digits)]:
            sum = sum + c
    return sum


assert(sum_match_next("1122") == 3)
assert(sum_match_next("1111") == 4)
assert(sum_match_next("1234") == 0)
assert(sum_match_next("91212129") == 9)

def sum_halfway(digit_str):
    digits = [int(c) for c in digit_str]
    sum = 0
    for i, c in enumerate(digits):
        if c == digits[(i + len(digits)//2) % len(digits)]:
            sum = sum + c
    return sum


assert(sum_halfway("1212") == 6)
assert(sum_halfway("1221") == 0)
assert(sum_halfway("123425") == 4)
assert(sum_halfway("123123") == 12)
assert(sum_halfway("12131415") == 4)

f = open("day1.input.txt")
INPUT = f.read()
INPUT = INPUT.strip()
if __name__ == "__main__":
    print(sum_match_next(INPUT))
    print(sum_halfway(INPUT))
