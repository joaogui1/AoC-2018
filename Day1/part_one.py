'''First Challenge of Advent of Code'''
RESULT = 0
with open("input.txt", 'r') as inp:
    for line in inp:
        if line[0] == '+':
            RESULT += int(line[1:])
        else:
            RESULT -= int(line[1:])
    print(RESULT)
