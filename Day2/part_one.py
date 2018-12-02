'''First Challenge of the Second day of the Advent of Code'''
TWO_TIMES = 0
THREE_TIMES = 0
with open("input.txt", 'r') as inp:
    for line in inp:
        FREQ = {}
        for letter in line:
            if letter in FREQ:
                FREQ[letter] += 1
            else:
                FREQ[letter] = 1
        if 2 in FREQ.values():
            TWO_TIMES += 1
        if 3 in FREQ.values():
            THREE_TIMES += 1
    print(TWO_TIMES * THREE_TIMES)
