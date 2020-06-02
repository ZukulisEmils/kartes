import csv
import getCords
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from koordinates import LKSToLatLon

cord = getCords.cords

# atrod mazākās x, y koordinates
i = 0
minx = cord[1][0]
miny = cord[0][1]
while i < len(cord):
    if minx > cord[i][0]:
        minx = cord[i][0]
    if miny > cord[i][1]:
        miny = cord[i][1]

    i += 1

# koordinates pareikina uz pikseļiem
i = 0
while i < len(cord):
    cord[i][0] -= (minx)
    cord[i][1] -= (miny)
    cord[i][1] = 1000 - cord[i][1]  # apgriez otradi

    cord[i][0] += 200
    cord[i][1] -= 200
    i += 1

# atrod visus punktus poligonaa
punkti = {}
i = 0
x = 0
y = 0
while i <= 10000:
    key = i
    if x == 100:
        x = 0
        y += 10
    point = Point(x * 10, y)
    polygon = Polygon(cord)
    if polygon.contains(point):
        punkti[key] = [[x * 10], [y], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    i += 1
    x += 1

for key in punkti:
    punkti[key][9][0] = punkti[key][0][0] + minx - 200
    punkti[key][10][0] = punkti[key][1][0] + miny +1200
    punkti[key][9] = LKSToLatLon(punkti[key][9][0], punkti[key][10][0])
    punkti[key][11][0] = punkti[key][0][0] + minx - 200 + 10
    punkti[key][12][0] = punkti[key][1][0] + miny + 1200 + 10
    punkti[key][11] = LKSToLatLon(punkti[key][11][0], punkti[key][12][0])

i = 1

# saglabaa
r = csv.reader(open('hello.csv'))
lines = list(r)
lines[0][0] = 'ID'
lines[0][1] = 'pH'
lines[0][2] = 'raza'
lines[0][3] = 'kalkis'
lines[0][4] = 'lat'
lines[0][5] = 'lon'
lines[0][6] = 'lat1'
lines[0][7] = 'lon1'
i = 1
for key in punkti:
    lines[i][0] = key
    lines[i][1] = 0
    lines[i][2] = 0
    lines[i][3] = 0
    lines[i][4] = punkti[key][9][0]
    lines[i][5] = punkti[key][9][1]
    lines[i][6] = punkti[key][11][0]
    lines[i][7] = punkti[key][11][1]
    i += 1
writer = csv.writer(open('hello.csv', 'w', newline=''))
writer.writerows(lines)