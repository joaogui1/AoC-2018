'''First Challenge of the Fourth day of the Advent of Code'''
FREQ = {}
with open("input.txt", "r") as inp:
    for line in inp:
        _, INI_X, INI_Y, H, W \
        = line.replace(',', "@ ").replace(': ', "@ ").replace('x', "@ ").split("@ ")
        W = int(W)
        H = int(H)
        INI_X = int(INI_X)
        INI_Y = int(INI_Y)
        for i in range(H):
            for j in range(W):
                if (INI_X + i, INI_Y + j) in FREQ:
                    FREQ[(INI_X + i, INI_Y + j)] += 1
                else:
                    FREQ[(INI_X + i, INI_Y + j)] = 1
RESULT = len([KEY for KEY in list(FREQ.keys()) if FREQ[KEY] > 1])
print(RESULT)
