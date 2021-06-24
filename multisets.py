from rookount import powerset, twoAttacking

def generateMultisets(size, elements, internal=False):
    # divs = min(size, len(elements))
    # print(divs)
    divlist = [[]]
    for divider in range(size):
        for i in range(len(divlist)):
            if divider > len(divlist[i]):
                continue
            if len(divlist[i]) == 0:
                start = 0
            else:
                start = divlist[i][-1]
            for j in range(start, elements):
                # print(divlist[i] + [j])
                divlist.append(divlist[i] + [j])
    final = []
    for item in divlist:
        if len(item) == size:
            final.append(item)
    return final

def multiDistance(set1, set2):
    distance = 0
    for i in range(len(set1)):
        if set1[i] != set2[i]:
            distance += 1
    return distance

def genDistance(setlist):
    mindistance = 0
    for i in range(len(setlist)):
        for j in range(i + 1, len(setlist)):
            mindistance = max(mindistance, multiDistance(setlist[i], setlist[j]))
    return mindistance

def simpToCubic(simp):
    cubic = []
    cubic.append(simp[2] - simp[1])
    cubic.append(simp[0])
    cubic.append(simp[2])
    return cubic

def simpToCubicConnor(simp):
    cubic = []
    cubic.append(simp[2] - simp[1])
    cubic.append(simp[1] - simp[0])
    cubic.append(simp[2])
    return cubic

# poo poo garbage
# def generatePositions(n, poslist):
    # positions = []
    # for i in range(len(poslist) - n + 1):
        # # positions.append([poslist[i]])
        # for j in range(i + 1, len(poslist) - n + 2):
            # if n > 2:
                # for k in generatePositions(n - 1, poslist[j + 1:]):
                    # # nogood = 0
                    # # for item in k:
                        # # # if twoAttacking(simpToCubic(poslist[i]), simpToCubic(item)):
                        # # if connorAttacking(poslist[i], item):
                            # # nogood = 1
                            # # break
                    # # if nogood:
                        # # continue
                    # positions.append([poslist[i]] + k)
            # # elif not twoAttacking(simpToCubic(poslist[i]), simpToCubic(poslist[j])):
            # # elif not connorAttacking(poslist[i], poslist[j]):
            # positions.append([poslist[i], poslist[j]])
    # return positions

def connorAttacking(pos1, pos2):
    if pos1[2] - pos2[2] == 0:
        return False
    else:
        diff = pos1[2] - pos2[2]
    if pos1[1] - pos2[1] == 0 and pos1[0] - pos2[0] == 0:
        return True
    elif pos1[1] - pos2[1] != diff:
        return False
    if pos1[0] - pos2[0] == diff or pos1[0] - pos2[0] == 0:
        return True

def setsToLatin(rooks, n):
    square = []
    for x in range(n):
        square.append([])
        for y in range(n):
            square[x].append(0)
    for rook in rooks:
        convert = simpToCubicConnor(rook)
        print(convert)
        square[convert[0]][convert[1]] = convert[2] + 1
    return square

def generateDiagonal(n):
    diag = []
    for i in range(n + 1):
        for j in range(i+1):
            diag.append([j,i,n])
    return diag

def mergeRooks(list1, list2):
    rooks = list2
    lenrooks = len(rooks)
    for rook1 in list1:
        bad = 0
        for rook2 in list2:
            if connorAttacking(rook1, rook2):
                bad = 1
                break
        if not bad:
            rooks.append(rook1)
    return rooks

def generatethething(places, n):
    rooks = []
    for pos in places:
        rooks = mergeRooks(generateDiagonal(pos), rooks)
        # print(rooks)
        # lenrooks = len(rooks)
        # for rook1 in generateDiagonal(pos):
            # bad = 0
            # for rook2 in rooks[:lenrooks]:
                # if connorAttacking(rook1, rook2):
                    # bad = 1
                    # break
            # if not bad:
                # rooks.append(rook1)

    for i in range(n):
        if i in places:
            continue
        rooks = mergeRooks(generateDiagonal(i), rooks)
    return rooks

def printTetSlices(rooks, n):
    for x in range(n):
        for y in range(x+1):
            print(" "*(n - y), end="")
            for z in range(y+1):
                found = 0
                for rook in rooks:
                    if rook == [z, y, x]:
                        found = 1
                        print("x",end="")
                        break
                if not found: print("0", end="")
                print(" ", end="")
                # if not found: print([x, y, z])
            print()
        print()

def getCountsByInitialSlice(n):
    counts = []

    rooks = []
    for m in range(n):
        count = 0
        counts.append([])
        # rooks = []
        for i in range(m):
            counts[m].append(0)
        for i in range(m,n):
            for j in range(i+1):
                for k in range(j+1):
                    # print(i,j,k)
                    working = [k,j,i]
                    attacked = 0
                    for place in rooks:
                        if connorAttacking(place, working):
                            # print(place)
                            attacked = 1
                            break
                    if not attacked:
                        rooks.append(working)
                        count += 1
            counts[m].append(count)
    return counts

def getAllOfSize(n, num):
    # minimum = 999
    out = []
    for i in range(n):
        for j in range(i+1):
            for k in range(j+1):
                working = generatethething([k, j, i], n)
                if len(working) == num:
                    out.append([k, j, i])
    return out

def getTetMin(n):
    minimum = 999
    smol = []
    for i in range(n):
        for j in range(i+1):
            for k in range(j+1):
                working = generatethething([k, j, i], n)
                if len(working) < minimum:
                    smol = [k, j, i]
                    minimum = len(working)
    return smol


if __name__ == '__main__':
    print(getAllOfSize(7,10))
    # printTetSlices(generatethething([5,9,18], 32), 32)
    # n = 18
    # minimum = 999
    # smol = []
    # for i in range(n):
        # for j in range(i+1):
            # for k in range(j+1):
                # working = generatethething([k, j, i], n)
                # if len(working) == 57:
                    # print(k, j, i)
                # if len(working) < minimum:
                    # smol = [k, j, i]
                    # minimum = len(working)
    # print(smol)
    # print(minimum)
