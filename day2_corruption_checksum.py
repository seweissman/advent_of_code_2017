"""
Day 2: Corruption Checksum
"""

def string_to_spreadsheet(s):
    rows = [[int(s) for s in row.split()] for row in s.split("\n")]
    return rows

def checksum(ss):
    rows = string_to_spreadsheet(ss)
    checksum = sum(max(row) - min(row) for row in rows)
    return checksum

s1 = """5 1 9 5
7 5 3
2 4 6 8"""

# print(string_to_spreadsheet(s1))
assert(checksum(s1) == 18)

def checksum_dividend(ss):
    rows = string_to_spreadsheet(ss)
    checksum = 0
    for row in rows:
        for i, val in enumerate(row):
            for val2 in row[i+1:]:
                if val % val2 == 0:
                    checksum = checksum + val//val2
                if val2 % val == 0:
                    checksum = checksum + val2//val
    return checksum

s2 = """5 9 2 8
9 4 7 3
3 8 6 5"""

assert(checksum_dividend(s2) == 9)

file = open("day2.input.txt")
INPUT = file.read()
INPUT = INPUT.strip()

if __name__ == "__main__":
    print(checksum(INPUT))
    print(checksum_dividend(INPUT))
