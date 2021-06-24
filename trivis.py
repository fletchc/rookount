from multisets import *
from math import sqrt
import drawSvg as draw

size = 1000
spread = 40
thickness = 2
dot = 5
def makeTri(spread, rows):
    triheight = sqrt(3) / 2 * spread
    points = []
    for i in range(rows):
        y = triheight * i
        for j in range(i+1):
            points.append([spread * 0.5*i - spread *j, -triheight*i, [j, i]])
    return points
    # d.append(draw.Circle(0, 0, 1, fill='black'))
    # d.append(draw.Circle(0.5 * spread, -triheight * spread, 1, fill='black'))
    # d.append(draw.Circle(-0.5 * spread, -triheight * spread, 1, fill='black'))

def pointSum(point):
    return point[2][0] + point[2][1]

def drawArcs(points, color, d, offset):
    left = 0
    right = 0
    top = 0
    matched = []
    # horrid work
    if points[0][2][1] == points[1][2][1]:
        matched = [0, 1, 2]
    elif points[0][2][1] == points[2][2][1]:
        matched = [0, 2, 1]
    elif points[1][2][1] == points[2][2][1]:
        matched = [1, 2, 0]
    top = points[matched[2]]
    if pointSum(points[matched[0]]) < pointSum(points[matched[1]]):
        left = points[matched[0]]
        right = points[matched[1]]
    elif pointSum(points[matched[0]]) < pointSum(points[matched[1]]):
        left = points[matched[1]]
        right = points[matched[0]]
    flipped = 0
    if top[1] > left[1]:
        flipped = 1
    distance = sqrt((left[0] - top[0])**2 + (left[1] - top[1])**2)
    dacolor = 'black'
    if not flipped:
        d.append(draw.ArcLine(top[0],top[1] - offset,distance,60,120,
                        stroke=color, stroke_width=thickness, fill = "none"))
        d.append(draw.ArcLine(left[0],left[1] - offset,distance,180,240,
                        stroke=color, stroke_width=thickness, fill = "none"))
        d.append(draw.ArcLine(right[0],right[1] - offset,distance,300,0,
                        stroke=color, stroke_width=thickness, fill = "none"))
    elif flipped:
        d.append(draw.ArcLine(top[0],top[1] - offset,distance,240,300,
                        stroke=color, stroke_width=thickness, fill = "none"))
        d.append(draw.ArcLine(left[0],left[1] - offset,distance,120,180,
                        stroke=color, stroke_width=thickness, fill = "none"))
        d.append(draw.ArcLine(right[0],right[1] - offset,distance,0,60,
                        stroke=color, stroke_width=thickness, fill = "none"))

def pointFromTri(point, tri):
    for item in tri:
        if point[0] == item[2][0] and point[1] == item[2][1]:
            return item

def getAttacking(point, n, tri):
    if point[2] == n - 1:
        return [pointFromTri(point[:2], tri)]
    shift = n - point[2] - 1
    return [pointFromTri(point[:2], tri), pointFromTri([point[0], point[1] + shift], tri), pointFromTri([point[0] + shift, point[1] + shift], tri)]

def getTriSize(points):
    if len(points) == 1:
        return 0
    return points[1][2][1] - points[0][2][1]

def printTri(divs, n):
    offset = int(-0.25 * n * spread * sqrt(3))
    d = draw.Drawing(size, size, origin='center', displayInline=False)
    d.append(draw.Rectangle(int(-size/2),int(-size/2),size,size, fill='white'))

    colord = ['black', 'red', 'green', 'blue', 'purple', 'pink', 'brown', 'mediumpurple', 'orange', 'aqua', 'steelblue', 'coral', 'deepink']
    sizes = []
    points = makeTri(spread, n)
    rookplacement = generatethething(divs, n)
    for rook in rookplacement:
        ah = getAttacking(rook, n, points) 
        thasize = getTriSize(ah)
        if thasize not in sizes:
            sizes.append(thasize)
        loc = sizes.index(thasize)
        if len(ah) == 3:
            drawArcs(ah, colord[loc], d, offset)
        elif len(ah) == 1:
            d.append(draw.Circle(ah[0][0], ah[0][1] - offset, dot + 5, stroke_width = thickness, fill='none', stroke='black'))
            # print(ah)
    # print(makeTri(50, 10))


    for item in points:
        d.append(draw.Circle(item[0], item[1] - offset, dot, fill='black'))
    # exit()
    # d.append(draw.ArcLine(thank[0][0],thank[0][1],150,240,300,
                    # stroke='red', stroke_width=2, fill = "none"))

    filename = "savefolder/size" + str(n) + "_with_" + str(len(rookplacement)) + "_rooks_divs"

    for item in divs:
        filename += str(item)

    d.setPixelScale(1)  # Set number of pixels per geometry unit
    # d.saveSvg('example.svg')
    d.savePng(filename + ".png")

mins = [0, 0, 0, 3, 4, 6, 7, 11, 12, 17, 19, 24, 26, 33, 35, 42, 46, 53, 57, 66, 70, 79, 85, 94, 100, 111]

for i in range(3,28):
    printTri(getTetMin(i), i)

