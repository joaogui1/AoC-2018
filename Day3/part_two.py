'''Second Challenge of the Third day of the Advent of Code'''
ANS = set()
MAT = [[0 for COL in range(2000)] for ROW in range(2000)]
with open("input.txt", "r") as inp:
    for line in inp:
        ID, INI_X, INI_Y, H, W \
        = line.replace(',', "@ ").replace(': ', "@ ").replace('x', "@ ").split("@ ")
        W = int(W)
        H = int(H)
        ID = int(ID[1:])
        INI_X = int(INI_X)
        INI_Y = int(INI_Y)

        ANS.add(ID)
        for i in range(H):
            for j in range(W):
                if MAT[INI_X + i][INI_Y + j] == 0:
                    MAT[INI_X + i][INI_Y + j] = ID
                else:
                    if ID in ANS:
                        ANS.remove(ID)
                    if MAT[INI_X + i][INI_Y + j] in ANS:
                        ANS.remove(MAT[INI_X + i][INI_Y + j])

print(ANS.pop())
