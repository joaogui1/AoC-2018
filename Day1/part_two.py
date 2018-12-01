'''Second Challenge of Advent of Code'''
FREQ = set()
RESULT = 0
FOUND_DUPLICATE = 0
with open("input.txt", 'r') as inp:
    while not FOUND_DUPLICATE:
        inp.seek(0)
        for line in inp:
            if line[0] == '+':
                RESULT += int(line[1:])
            else:
                RESULT -= int(line[1:])
            if RESULT in FREQ:
                FOUND_DUPLICATE = 1
                break
            else:
                FREQ.add(RESULT)
    print(RESULT)
