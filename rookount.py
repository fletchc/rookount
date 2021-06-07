import itertools

def printBoard(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                print(board[x][y][z], end='')
            print(" ", end='')
        print("\n", end='')

def createBoard(n):
    return [[[0 for x in range(n)] for y in range(n)] for z in range(n)]

def createLatinSquare(board):
    if not isMaximal(board):
        return -1



def build(old):
    n = len(old)
    new = createBoard(n + 1)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                new[x][y][z] = old[x][y][z]
    return new

def copyBoard(board):
    newboard = createBoard(len(board))
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
    for i in range(1,len(poslist)+1):
        for element in itertools.combinations(poslist,i):
            powset.append(list(element))

    removelist = []
    for setup in powset:
        attacking = False
        for i in range(len(setup)):
            for j in range(i + 1, len(setup)):
                if twoAttacking(setup[i], setup[j]):
                    removelist.append(setup)
                    attacking = True
                    break
            if attacking:
                break
    for setup in removelist:
        powset.remove(setup)

    return powset

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
            workingboard[position[0]][position[1]][position[2]] = 1
        boardlist.append(workingboard)

    return boardlist

def isMaximal(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if board[x][y][z]:
                    continue
                if not isAttacked(board, x, y, z):
                    return False
    return True

# def countArrangements(n):

def countAllRooks(n):
    if n == 1:
        first = createBoard(n)
        second = createBoard(n)
        second[0][0][0] = 1
        return [first, second]
    else:
        boardlist = []
        for pos in countAllRooks(n - 1):
            boardlist += generateLarger(pos)
        return boardlist

def getRookCount(board):
    n = len(board)
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if board[x][y][z]:
                    count += 1
    return count

def isNonattackingPosition(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if not board[x][y][z]:
                    continue
                board[x][y][z] = 0
                if isAttacked(board, x, y, z):
                    return False
                board[x][y][z] = 1
    return True

if __name__ == '__main__':

    n = 2
    counts = countAllRooks(n)

    fo = open("rook3.txt", "w")
    for position in counts:
        if not isNonattackingPosition(position):
            counts.remove(position)
            print("WARN: attacking position found")
            continue
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    fo.write(str(position[x][y][z]))
        fo.write("\n")

    fo.close()


    maxinfo = []

    for position in counts:
        if not isMaximal(position):
            continue
        found = 0
        for item in maxinfo:
            found = 0
            if item[0] == getRookCount(position):
                item[1].append(position)
                found = 1
                break
        if not found:
            maxinfo.append([])
            maxinfo[-1].append(getRookCount(position))
            maxinfo[-1].append([])
            maxinfo[-1][1].append(position)

    # print(maxinfo)

    fo = open("maxrook3.txt", "w")
    for count in maxinfo:
        fo.write(str(count[0]))
        fo.write("\n")
        for position in count[1]:
            for x in range(n):
                for y in range(n):
                    for z in range(n):
                        fo.write(str(position[x][y][z]))
                    fo.write(" ")
                fo.write("\n")
            fo.write("\n")


    fo.close()

    aha = createBoard(3)

    aha[1][2][0] = 1

    print(isAttacked(aha, 1, 0, 0))

    # board[1][1][1] = True

    # newboard = copyBoard(board)
    # board[0][0][1] = True

    # print(board == newboard)
    # print(isAttacked(board, 1, 2, 2))


