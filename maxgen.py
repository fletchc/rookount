from rookount import *
import random

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
