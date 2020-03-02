from itertools import combinations
from math import sqrt

def slope(x1, y1, x2, y2):
    try:
        return (y2-y1)/(x2-x1)
    except:
        return "undefined"

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

inputData = open("triangles.in", "r")
outputData = open("triangles.out", "w")
n = inputData.readline()
n = int(n)
points = []

for i in range(n):
    points.append(list(map(int,inputData.readline().split())))

combos = [i for i in combinations(points, 3)]
areas = []
for i in range(len(combos)):
    slopes = []
    x1, y1 = combos[i][1]
    x2, y2 = combos[i][0]
    slopes.append(slope(x1, y1, x2, y2))
    x1, y1 = combos[i][2]
    x2, y2 = combos[i][0]
    slopes.append(slope(x1, y1, x2, y2))
    x1, y1 = combos[i][2]
    x2, y2 = combos[i][1]
    slopes.append(slope(x1, y1, x2, y2))
    if 0 in slopes and "undefined" in slopes:
        x1, y1 = combos[i][1]
        x2, y2 = combos[i][0]
        a = distance(x1, y1, x2, y2)
        x1, y1 = combos[i][2]
        x2, y2 = combos[i][0]
        b = distance(x1, y1, x2, y2)
        x1, y1 = combos[i][2]
        x2, y2 = combos[i][1]
        c = distance (x1, y1, x2, y2)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        areas.append(round(area,2))

outputData.write("{}\n".format(int(max(areas)*2)))
outputData.close()
inputData.close()