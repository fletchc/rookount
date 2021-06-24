import itertools
import random

# https://www.technomancy.org/python/powerset-generator-python/
# returns the powerset of the list seq
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

# prints out a given board in a formatted manner
def printBoard(board):
    n = len(board)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                print(board[x][z][y], end='')
            print(" ", end='')
        print("\n", end='')

# returns an 3d list of size n filled with 0's
def createBoard(n):
    return [[[0 for x in range(n)] for y in range(n)] for z in range(n)]

# returns a board one larger than old with the
def build(old):
    n = len(old)
    new = createBoard(n + 1)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                new[x][y][z] = old[x][y][z]
    return new

# returns a list that is identical to the input board.
# I don't actually know how python allocates and manages memory with respect to lists so I wrote this function and it does what I want.
def copyBoard(board):
    n = len(board)
    newboard = createBoard(n)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                newboard[x][y][z] = board[x][y][z]
    return newboard
    # return [[[board[x][y][z] for x in range(len(board))] for y in range(len(board))] for z in range(len(board))]
    
# tells whether a positions at indices x, y, z is attacked. Note that if there is a rook at x, y, z then the position will be treated as attacked. Whether this is the right decision to have made is debatable.
def isAttacked(board, x, y, z):
    for i in range(len(board)):
        if board[i][y][z] or board[x][i][z] or board[x][y][i]:
            return True
    return False

# tup1 and tup2 store indices of two rooks. This logical structure is pretty horrid.
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

# returns a random board of size n completely filled with nonattacking rooks.
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

# given a list of 3-tuples containing the coordinates of rooks, returns whether any are attacking each other
def areAttackingTups(tuplist, board):
    for tup1 in tuplist:
        if isAttacked(board, tup1[0], tup1[1], tup1[2]):
            return True
        for tup2 in tuplist:
            if twoAttacking(tup1, tup2) and tup1 != tup2:
                return True
    return False


def generateAttackList(poslist):
    # powset = []
    # for i in range(1,len(poslist)+1):
        # for element in itertools.combinations(poslist,i):
            # powset.append(list(element))
    powset = list(powerset(poslist))

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

# probably broken
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

# returns true if the rook placement on board has no nonattacked squares
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

# broken function that was supposed to recursively compute all rook positions up to size n
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

# returns the number of rooks in board
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
    n = 3
    for i in range(1, n + 1):
        thinglist = countAllRooks(i)
        count = 0
        for thing in thinglist:
            if isMaximal(thing):
                count += 1
        print(count)
