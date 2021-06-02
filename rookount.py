import itertools

def create(n):
    return [[[False for x in range(n)] for y in range(n)] for z in range(n)]

def build(old):
    n = len(old)
    new = create(n + 1)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                new[x][y][z] = old[x][y][z]
    return new

def copyBoard(board):
    newboard = create(len(board))
    return [[[board[x][y][z] for x in range(len(board))] for y in range(len(board))] for z in range(len(board))]
    

def isAttacked(board, x, y, z):
    for i in range(len(board)):
        if board[i][y][z] or board[x][i][z] or board[x][y][i]:
            return True
    return False

def twoAttacking(tup1, tup2):
    if tup1[0] != tup2[0]:
        if tup1[1] == tup2[1] and tup1[2] == tup2[2]:
            return True
        else:
            return False
    elif tup1[1] == tup2[1]:
        return True
    elif tup1[2] == tup2[2]:
        return True
    return False

def generateAttackList(poslist):
    powset = []
    for i in range(0,len(poslist)+1):
        for element in itertools.combinations(poslist,i):
            powset.append(element)

    for setup in powset:
        for i in range(len(setup)):
            for j in range(i + 1, len(setup)):
                if twoAttacking(setup[i], setup[j]):
                    print(setup)
                    # print(powset)
                    powset.remove(setup)
                    break

def generateLarger(board):
    boardlist = []
    newboard = build(board)
    n = len(newboard)
    boardlist.append(newboard)
    newpositions = []
    newpositions.append((n - 1, n - 1, n - 1))
    for i in range(n):
        for j in range(n - 1):
            if not isAttacked(newboard, n - 1, j, i):
                newpositions.append((n - 1, j, i))
            if not isAttacked(newboard, i, n - 1, j):
                newpositions.append((i, n - 1, j))
            if not isAttacked(newboard, j, i, n - 1):
                newpositions.append((j, i, n - 1))

    setups = generateAttackList(newpositions)
    for setup in setups:
        workingboard = copyBoard(newboard)
        for position in setup:
            workingboard[position[0]][position[1]][position[2]] = True
        boardlist.append(workingboard)

    return boardlist






# def countArrangements(n):


board = create(1)

for b in generateLarger(board):
    print(b)

# board[1][1][1] = True

# newboard = copyBoard(board)
# board[0][0][1] = True

# print(board == newboard)
# print(isAttacked(board, 1, 2, 2))


