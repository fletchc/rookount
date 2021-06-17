from rookount import *

def isTet(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if not (y > x + (n - 1 - z)) and board[x][y][z]:
                    # print(x,y,z)
                    return False
    return True

def buildTet(board):
    n = len(board)
    newb = build(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                newb[x][y + 1][z] = board[x][y][z]
    return newb

def generateTetPositions(board, limit):
    base = buildTet(board)
    n = len(base)
    freesquares = []

    div = 0
    for x in range(div, n):
        div += 1
        for y in range(div, n):
            freesquares.append((x, y, n - 1))
    powset = list(powerset(freesquares))
    boardlist = []
    for position in powset:
        if areAttackingTups(position, base):
            continue
        workingboard = copyBoard(base)
        for tup in position:
            workingboard[tup[0]][tup[1]][tup[2]] = 1
        if getRookCount(workingboard) <= limit:
            boardlist.append(workingboard)
    return boardlist

def cringe(board):
    base = buildTet(board)
    n = len(base)
    freesquares = []

    div = 0
    for x in range(div, n):
        div += 1
        for y in range(div, n):
            freesquares.append((x, y, n - 1))

    boardlist = []
    for position in powset:
        if areAttackingTups(position, base):
            continue
        workingboard = copyBoard(base)
        for tup in position:
            workingboard[tup[0]][tup[1]][tup[2]] = 1
        if getRookCount(workingboard) <= limit:
            boardlist.append(workingboard)
    return boardlist

def generateAllUpToN(n, limit):
    if n == 1:
        return [createBoard(1)]
    else:
        workinglist = []
        for board in generateAllUpToN(n - 1, limit):
            workinglist += generateTetPositions(board, limit)
        # print(len(workinglist))
        return workinglist

for i in range(1,10):
    count = 0
    for item in generateAllUpToN(i, 2):
        if(getRookCount(item) == 2):
            count += 1
    print(count)
    # print(len(generateAllUpToN(i, 2)))

exit()
n = 6
# for i in range(1, n + 1):
    # workinglist = generateAllUpToN(i)
    # for j in range(int((i*(i-1))/2)+1):
        # count = 0
        # for item in workinglist:
            # if getRookCount(item) == j:
                # count += 1
        # print(count, end=" ")
    # print()
