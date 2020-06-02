import pygame
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
from koordinates import LKSToLatLon
import getCords

pygame.init()

WinWidth = 1000
WinHeight = 1000
win = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption('Kalķis')
run = True
Pi = 3.14
i = 0
j = 0
f = 0
e = 0
color = 2
showr = 5
showg = 5
showb = 5
y = 0
cord = getCords.cords

minx = cord[1][0]
miny = cord[0][1]

while i < len(cord):
    if minx > cord[i][0]:
        minx = cord[i][0]

    if miny > cord[i][1]:
        miny = cord[i][1]

    i += 1

while j < len(cord):
    cord[j][0] -= (minx)
    cord[j][1] -= (miny)
    cord[j][1] = 1000 - cord[j][1]
    print(cord[j][0], 'x', cord[j][1], 'y')

    cord[j][0] += 200
    cord[j][1] -= 200
    j += 1

punkti = {}

k = 0
x = 0
while k <= 10000:
    key = k
    if x == 100:
        x = 0
        y += 10
    point = Point(x * 10, y)
    polygon = Polygon(cord)
    if polygon.contains(point):
        punkti[key] = [[x * 10], [y], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    k += 1
    x += 1

for key in punkti:
    punkti[key][9][0] = punkti[key][0][0] + minx - 200
    punkti[key][10][0] = punkti[key][1][0] + miny +1200
    punkti[key][9] = LKSToLatLon(punkti[key][9][0], punkti[key][10][0])

q = 1
while q <= len(punkti) + 1:

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
                    print(q)
            q += 1
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
        move_ticker = 0
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = 2
                print(color)
            if event.key == pygame.K_g:
                color = 3
                print(color)

            if event.key == pygame.K_b:
                color = 4
                print(color)
            if event.key == pygame.K_KP_MINUS:
                value -= 0.1
                print(value)
            if event.key == pygame.K_KP_PLUS:
                value += 0.1
                print(value)
            if event.key == pygame.K_KP1:
                showr = 2
                print('RED on')
                print(showr)
            if event.key == pygame.K_KP2:
                showg = 3
                print('GREEN on')
                print(showg)
            if event.key == pygame.K_KP3:
                showb = 4
                print('BLUE on')
                print(showb)
            if event.key == pygame.K_KP4:
                showr = 5
                print('RED off')
                print(showr)
            if event.key == pygame.K_KP5:
                showg = 5
                print('GREEN off')
                print(showg)
            if event.key == pygame.K_KP6:
                showb = 5
                print('BLUE off')
                print(showb)

        if pygame.mouse.get_pressed()[0]:
            try:

                atlX = event.pos[0] % 10
                altY = event.pos[1] % 10
                cubeX = event.pos[0] - atlX
                cubeY = event.pos[1] - altY

                cubeY *= 10
                cubeX /= 10
                id = cubeY + cubeX

                if id in punkti:
                    print('in')

                else:
                    print('Out')


            except AttributeError:
                pass

    for key in punkti:
        pygame.draw.rect(win, (punkti[key][2][0], punkti[key][2][0], punkti[key][2][0]),
                         (punkti[key][0][0], punkti[key][1][0], 10, 10))

    while e < len(cord) - 1:
        pygame.draw.line(win, (255, 255, 255), (cord[e][0], cord[e][1]), (cord[e + 1][0], cord[e + 1][1]))
        e += 1

    pygame.display.update()

# saglabaa

r = csv.reader(open('hello.csv'))
lines = list(r)
i = 1
for key in punkti:
    lines[i][6] = punkti[key][8][0]
    lines[i][7] = punkti[key][9][0]
    lines[i][8] = punkti[key][9][1]
    print(punkti[key])
    i += 1
writer = csv.writer(open('hello.csv', 'w', newline=''))
writer.writerows(lines)

pygame.quit()
