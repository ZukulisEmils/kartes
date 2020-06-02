import pygame
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
import getCords
pygame.init()

WinWidth = 1000
WinHeight = 1000
win = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption('pH')

run = True

showr = 2
showg = 3
showb = 4
y = 0
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
while i <= 10000:
    key = i
    if x == 100:
        x = 0
        y += 10
    point = Point(x * 10, y)
    polygon = Polygon(cord)
    if polygon.contains(point):
        punkti[key] = [[x * 10], [y], [0], [0], [0], [0], [0], [0]]
    i += 1
    x += 1

# ielade punktus no csv
i = 1
while i <= len(punkti) + 1:
    for key in punkti:
        with open('hello.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            next(reader)
            for row in reader:
                if int(row[0]) == key:
                    pH = float(row[1])
                    raza = float(row[2])
                    punkti[key][6][0] = pH
                    value2 = pH
                    value2 = ((value2 - 3.5) / 3.3) * 100
                    if value2 == 0:
                        punkti[key][2][0] = 255
                        punkti[key][3][0] = 0
                        punkti[key][4][0] = 0
                        punkti[key][7][0] = raza
                    elif 0 < value2 < 50:
                        punkti[key][2][0] = 255
                        punkti[key][3][0] = int(value2 * 5.1)
                        punkti[key][4][0] = 0
                        punkti[key][7][0] = raza
                    elif value2 == 50:
                        punkti[key][2][0] = 255
                        punkti[key][3][0] = 255
                        punkti[key][4][0] = 0
                        punkti[key][7][0] = raza
                    elif 50 < value2 < 100:
                        punkti[key][2][0] = int((100 - value2) * 5.1)
                        punkti[key][3][0] = 255
                        punkti[key][4][0] = 0
                        punkti[key][7][0] = raza
                    elif value2 == 100:
                        punkti[key][2][0] = 0
                        punkti[key][3][0] = 255
                        punkti[key][4][0] = 0
                        punkti[key][7][0] = raza
                    elif 100 < value2 < 150:
                        punkti[key][2][0] = 0
                        punkti[key][3][0] = 255
                        punkti[key][4][0] = int((value2 - 100) * 5.1)
                        punkti[key][7][0] = raza
                    elif value2 == 150:
                        punkti[key][2][0] = 0
                        punkti[key][3][0] = 255
                        punkti[key][4][0] = 255
                        punkti[key][7][0] = raza
                    elif 150 < value2 < 200:
                        punkti[key][2][0] = 0
                        punkti[key][3][0] = int((200 - value2) * 5.1)
                        punkti[key][4][0] = 255
                        punkti[key][7][0] = raza
                    elif value2 == 200:
                        punkti[key][2][0] = 0
                        punkti[key][3][0] = 0
                        punkti[key][4][0] = 255
                        punkti[key][7][0] = raza
            i += 1

value = 3.5

while run:
    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        move_ticker = 0
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_MINUS:
                value -= 0.1
                print('pH',value)
            if event.key == pygame.K_KP_PLUS:
                value += 0.1
                print('pH',value)
            if event.key == pygame.K_KP1:
                showr = 2
                print('RED on')
            if event.key == pygame.K_KP2:
                showg = 3
                print('GREEN on')
            if event.key == pygame.K_KP3:
                showb = 4
                print('BLUE on')
            if event.key == pygame.K_KP4:
                showr = 5
                print('RED off')
            if event.key == pygame.K_KP5:
                showg = 5
                print('GREEN off')
            if event.key == pygame.K_KP6:
                showb = 5
                print('BLUE off')

        # atrod id no koordinaatem
        if pygame.mouse.get_pressed()[0]:
            try:
                atlX = event.pos[0] % 10
                altY = event.pos[1] % 10
                cubeX = event.pos[0] - atlX
                cubeY = event.pos[1] - altY

                cubeY *= 10
                cubeX /= 10
                id = cubeY + cubeX

                # nosaka krasu no vertibas
                if id in punkti:
                    value2 = ((value - 3.5) / 3.3) * 100
                    if value2 == 0:
                        punkti[id][2][0] = 255
                        punkti[id][3][0] = 0
                        punkti[id][4][0] = 0
                        punkti[id][6][0] = value
                    elif value2 > 0 and value2 < 50:
                        punkti[id][2][0] = 255
                        punkti[id][3][0] = int(value2 * 5.1)
                        punkti[id][4][0] = 0
                        punkti[id][6][0] = value
                    elif value2 == 50:
                        punkti[id][2][0] = 255
                        punkti[id][3][0] = 255
                        punkti[id][4][0] = 0
                        punkti[id][6][0] = value
                    elif value2 > 50 and value2 < 100:
                        punkti[id][2][0] = int((100 - value2) * 5.1)
                        punkti[id][3][0] = 255
                        punkti[id][4][0] = 0
                        punkti[id][6][0] = value
                    elif value2 == 100:
                        punkti[id][2][0] = 0
                        punkti[id][3][0] = 255
                        punkti[id][4][0] = 0
                        punkti[id][6][0] = value
                    elif value2 > 100 and value2 < 150:
                        punkti[id][2][0] = 0
                        punkti[id][3][0] = 255
                        punkti[id][4][0] = int((value2 - 100) * 5.1)
                        punkti[id][6][0] = value
                    elif value2 == 150:
                        punkti[id][2][0] = 0
                        punkti[id][3][0] = 255
                        punkti[id][4][0] = 255
                        punkti[id][6][0] = value
                    elif value2 > 150 and value2 < 200:
                        punkti[id][2][0] = 0
                        punkti[id][3][0] = int((200 - value2) * 5.1)
                        punkti[id][4][0] = 255
                        punkti[id][6][0] = value
                    elif value2 == 200:
                        punkti[id][2][0] = 0
                        punkti[id][3][0] = 0
                        punkti[id][4][0] = 255
                        punkti[id][6][0] = value
            except AttributeError:
                pass

    # ziimee punktus
    for key in punkti:
        pygame.draw.rect(win, (punkti[key][showr][0], punkti[key][showg][0], punkti[key][showb][0]),
                         (punkti[key][0][0], punkti[key][1][0], 10, 10))

    # lauka kontura
    i = 0
    while i < len(cord) - 1:
        pygame.draw.line(win, (255, 255, 255), (cord[i][0] + 5, cord[i][1] + 5),
                         (cord[i + 1][0] + 5, cord[i + 1][1] + 5))
        i += 1

    pygame.display.update()

# saglabaa

r = csv.reader(open('hello.csv'))
lines = list(r)
i = 1
for key in punkti:
    lines[i][1] = punkti[key][6][0]
    i += 1
writer = csv.writer(open('hello.csv', 'w', newline=''))
writer.writerows(lines)
pygame.quit()
