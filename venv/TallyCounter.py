from collections import Counter

def count_tally(string):
    chars = list(string)
    tally_count = Counter()
    for char in chars:
        tally_count[char.lower()] += -1 if (char.isupper()) else 1
    return tally_count

count = count_tally("EbAAdbBEaBaaBBdAccbeebaec")
print(count)