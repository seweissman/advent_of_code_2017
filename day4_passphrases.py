"""
Day 4: High Entropy Passphrases
"""
import sys
from collections import defaultdict
def has_no_repeats(passphrase):
    word_list = passphrase.split(" ")
    word_counts = defaultdict(int)
    for word in word_list:
        word_counts[word] += 1
    for val in word_counts.values():
        if val > 1:
            return False
    return True

def count_valid_passphrases(pass_list, validator):
    valid_count = 0
    for passphrase in pass_list:
        passphrase = passphrase.strip()
        if passphrase == "":
            continue
        if validator(passphrase):
            valid_count += 1
    return valid_count


assert has_no_repeats("aa bb cc dd ee")
assert not has_no_repeats("aa bb cc dd aa")
assert has_no_repeats("aa bb cc dd aaa")

def has_no_anagrams(passphrase):
    word_list = passphrase.split(" ")
    word_counts = defaultdict(int)
    for word in word_list:
        split_word = list(word)
        split_word.sort()
        sort_word = "".join(split_word)
        word_counts[sort_word] += 1
    for val in word_counts.values():
        if val > 1:
            return False
    return True

assert has_no_anagrams("abcde fghij")
assert not has_no_anagrams("abcde xyz ecdab")
assert has_no_anagrams("a ab abc abd abf abj")
assert has_no_anagrams("iiii oiii ooii oooi oooo")
assert not has_no_anagrams("oiii ioii iioi iiio")


if __name__ == "__main__":
    file_in = open(sys.argv[1])
    passphrase_list = file_in.readlines()
    print(count_valid_passphrases(passphrase_list, has_no_repeats))
    print(count_valid_passphrases(passphrase_list, has_no_anagrams))
