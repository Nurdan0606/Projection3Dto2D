import math
import pygame
import numpy as np

W, H = 600, 600

dis = pygame.display.set_mode((W, H))

# W, H - forward, backward
# UP, DOWN, RIGHT - rotation by (x, y, z)

displayWidth, displayHeight = 600, 600
FPS = 240
cameraDistance = 400

displayX, displayY, displayZ = 0, 0, 0
displayPoints = [-displayWidth / 2, displayHeight / 2]

x, y, z = 0, 0, 0
a = 100

coords = [[a/2+x, a/2+y, a/2+z], [-a/2+x, a/2+y, a/2+z], [-a/2+x, a/2+y, -a/2+z], [a/2+x, a/2+y, -a/2+z],
          [a/2+x, -a/2+y, a/2+z], [-a/2+x, -a/2+y, a/2+z], [-a/2+x, -a/2+y, -a/2+z], [a/2+x, -a/2+y, -a/2+z]]

coords2 = [[a/2+x, a/2+y, a/2+z+a], [-a/2+x, a/2+y, a/2+z+a], [-a/2+x, a/2+y, -a/2+z+a], [a/2+x, a/2+y, -a/2+z+a],
          [a/2+x, -a/2+y, a/2+z+a], [-a/2+x, -a/2+y, a/2+z+a], [-a/2+x, -a/2+y, -a/2+z+a], [a/2+x, -a/2+y, -a/2+z+a]]

while True:
    pygame.time.Clock().tick(FPS)
    dis.fill("black")
    coordsInDisplay = []

    for xx, yy, zz in coords:
        try:
            dotX = cameraDistance * zz / (xx - displayX + cameraDistance) - displayPoints[0]
            dotY = displayPoints[1] + displayY - cameraDistance * yy / (xx - displayX + cameraDistance)

            coordsInDisplay.append((dotX, dotY))
        except:
            pass

    for xx, yy, zz in coords2:
        try:
            dotX = cameraDistance * zz / (xx - displayX + cameraDistance) - displayPoints[0]
            dotY = displayPoints[1] + displayY - cameraDistance * yy / (xx - displayX + cameraDistance)

            coordsInDisplay.append((dotX, dotY))
        except:
            pass

    for i in range(4):
        try:
            pygame.draw.line(dis, "white", coordsInDisplay[i], coordsInDisplay[(i+1)%4], 2)
            pygame.draw.line(dis, "white", coordsInDisplay[i+4], coordsInDisplay[(i + 1) % 4 + 4], 2)
            pygame.draw.line(dis, "white", coordsInDisplay[i], coordsInDisplay[i + 4], 2)
            pygame.draw.line(dis, "white", coordsInDisplay[i+8], coordsInDisplay[(i + 1) % 4+8], 2)
            pygame.draw.line(dis, "white", coordsInDisplay[i + 4+8], coordsInDisplay[(i + 1) % 4 + 4+8], 2)
            pygame.draw.line(dis, "white", coordsInDisplay[i+8], coordsInDisplay[i + 4+8], 2)
        except:
            pass

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        if displayX < 200:
            displayX += 0.5
    if key[pygame.K_s]:
        displayX -= 0.5

    if key[pygame.K_UP]:
        for i, j in enumerate(coords):
            alpha = math.radians(0.2)
            Rx = [[1, 0, 0],
                  [0, math.cos(alpha), -math.sin(alpha)],
                  [0, math.sin(alpha), math.cos(alpha)]]

            res = np.dot(j, Rx)
            coords[i] = res

        for i, j in enumerate(coords2):
            alpha = math.radians(0.2)
            Rx = [[1, 0, 0],
                  [0, math.cos(alpha), -math.sin(alpha)],
                  [0, math.sin(alpha), math.cos(alpha)]]

            res = np.dot(j, Rx)
            coords2[i] = res

    if key[pygame.K_DOWN]:
        for i, j in enumerate(coords):
            alpha = math.radians(0.2)
            Ry = [[math.cos(alpha), 0, math.sin(alpha)],
                  [0, 1, 0],
                  [-math.sin(alpha), 0, math.cos(alpha)]]

            res = np.dot(j, Ry)
            coords[i] = res

        for i, j in enumerate(coords2):
            alpha = math.radians(0.2)
            Ry = [[math.cos(alpha), 0, math.sin(alpha)],
                  [0, 1, 0],
                  [-math.sin(alpha), 0, math.cos(alpha)]]

            res = np.dot(j, Ry)
            coords2[i] = res

    if key[pygame.K_RIGHT]:
        for i, j in enumerate(coords):
            alpha = math.radians(0.2)
            Rz = [[math.cos(alpha), -math.sin(alpha), 0],
                  [math.sin(alpha), math.cos(alpha), 0],
                  [0, 0, 1]]

            res = np.dot(j, Rz)
            coords[i] = res

        for i, j in enumerate(coords2):
            alpha = math.radians(0.2)
            Rz = [[math.cos(alpha), -math.sin(alpha), 0],
                  [math.sin(alpha), math.cos(alpha), 0],
                  [0, 0, 1]]

            res = np.dot(j, Rz)
            coords2[i] = res

    pygame.display.update()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()