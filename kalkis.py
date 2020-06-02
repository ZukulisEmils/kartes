import pygame
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
import getCords

pygame.init()

WinWidth = 1000
WinHeight = 1000
win = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption('Kalķis')
run = True

cord = getCords.cords

minx = cord[1][0]
miny = cord[0][1]
i = 0
while i < len(cord):
    if minx > cord[i][0]:
        minx = cord[i][0]

    if miny > cord[i][1]:
        miny = cord[i][1]

    i += 1
i = 0
while i < len(cord):
    cord[i][0] -= (minx)
    cord[i][1] -= (miny)
    cord[i][1] = 1000 - cord[i][1]

    cord[i][0] += 200
    cord[i][1] -= 200
    i += 1

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
        punkti[key] = [[x * 10], [y], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    i += 1
    x += 1


while i <= len(punkti) + 1:

    for key in punkti:
        with open('hello.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            next(reader)
            for row in reader:
                if int(row[0]) == key:
                    raza = float(row[5])
                    pH = float(row[4])
                    kalkis = float(row[6])
                    punkti[key][7][0] = raza
                    value2 = raza
                    value2 = (value2 / 6) * 100

                    punkti[key][6][0] = pH
                    punkti[key][7][0] = raza
                    punkti[key][8][0] = (punkti[key][6][0] * punkti[key][7][0]) + 30
                    maxK = punkti[key][8][0]
                    minK = punkti[key][8][0]

            i += 1
value = 3.5

for key in punkti:
    if maxK < punkti[key][8][0]:
        maxK = punkti[key][8][0]

for key in punkti:
    krasa = int((punkti[key][8][0] / maxK) * 255)
    punkti[key][2][0] = krasa
while run:
    e = 0
    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for key in punkti:
        pygame.draw.rect(win, (punkti[key][2][0], punkti[key][2][0], punkti[key][2][0]),
                         (punkti[key][0][0], punkti[key][1][0], 10, 10))
    i = 0
    while i < len(cord) - 1:
        pygame.draw.line(win, (255, 255, 255), (cord[i][0]+5, cord[i][1]+5), (cord[i + 1][0]+5, cord[i + 1][1]+5))
        i += 1

    pygame.display.update()

# saglabaa

r = csv.reader(open('hello.csv'))
lines = list(r)
i = 1
for key in punkti:
    lines[i][6] = punkti[key][8][0]
    i += 1
writer = csv.writer(open('hello.csv', 'w', newline=''))
writer.writerows(lines)

pygame.quit()
