from rookount import *
import random

# def generateMaximal(board):
    # newboard = copyBoard(board)
    # n = len(board)
    # for x in range(n):
        # for y in range(n):
            # for z in range(n):
                # if isAttacked(newboard, x, y, z):
                    # continue
                # newboard[x][y][z] = 1
    # return(newboard)

def generateMaximal(n):
    # print("eh")
    board = createBoard(n)
    unattacked = []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                unattacked.append((x, y, z))
    while not isMaximal(board):
        new = random.choice(unattacked)
        # print("adding", new)
        board[new[0]][new[1]][new[2]] = 1
        for item in unattacked:
            if isAttacked(board, item[0], item[1], item[2]):
                # print("removing ", item)
                unattacked.remove(item)
    if isNonattackingPosition(board):
        return board
    else:
        return generateMaximal(n)



rookNumbers = []
rookCounts = []

def insertBoard(board):
    count = getRookCount(board)
    if count in rookNumbers:
        rookCounts[rookNumbers.index(count)] += 1
    else:
        rookNumbers.append(count)
        rookCounts.append(1)

for i in range(1,10):
    found = 0
    targetnum = 0
    # for j in range(10000):
    while not found:
        if i % 2:
            targetnum = 2*(3**(int((i - 1) / 2))) - 1
        else:
            targetnum = (3**(int(i / 2))) - 1
        working = generateMaximal(i)
        if getRookCount(working) == targetnum:
            found = 1
            print(targetnum, "rooks found for size", i)
    # if not found:
        # print("WARNING:", targetnum, "rooks not found for size", i)
    


    # print("size:", i)
    # rookNumbers.sort()
    # print(rookNumbers)

    # rookNumbers.clear()
    # rookCounts.clear()
