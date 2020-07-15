import pygame

pygame.init()

loop = True

screen = pygame.display.set_mode((450,450))

walls = []

mousedown = 0

while loop:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               loop = False
          if event.type == pygame.MOUSEBUTTONDOWN:
               mousedown = 1
          if event.type == pygame.MOUSEBUTTONUP:
               mousedown = 0
     if(mousedown):
          pos = pygame.mouse.get_pos()
          pygame.draw.circle(screen,(0,0,255),pos,5,0)
          print(pos)
          pygame.display.flip()
          walls.append((int(pos[0]/4),int(pos[1]/4)))


def AstarAlgo(loop):
    for x in range(150):
        for y in range(150):
          if(check(x,y)):
            Dist.put((miniDist[x][y]+Distance[x][y],(x,y)))
    done = 0
    while done < 22500:
        drawBoxes()
        drawLines()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                break
        if not(loop):
            return loop
        temp = Dist.get()
        i = temp[1][0]
        j = temp[1][1]
        if (i == Xend and j == Yend):
            while (not(prevNode[i][j] == (-1,-1))):
                if(i == Xstart and j == Ystart):
                    eventsDone = 0
                    break
                pg.draw.rect(screen, (255, 255, 0), (prevNode[i][j][0] * 4, 4 * prevNode[i][j][1], 4, 4), 0)
                x = prevNode[i][j][0]
                y = prevNode[i][j][1]
                i = x
                j = y
                pg.display.update()
            break
        if(Done[i][j] == 0):
            Done[i][j] = 1
            done += 1
        else:
            continue
        if (i - 1 >= 0 and check(i - 1,j)):
            if (miniDist[i - 1][j] > miniDist[i][j] + 1):
                miniDist[i - 1][j] = miniDist[i][j] + 1
                Dist.put((miniDist[i - 1][j]+Distance[i-1][j],(i - 1, j)))
                prevNode[i - 1][j] = (i, j)
        if (i + 1 < 150 and check(i + 1,j)):
            if (miniDist[i + 1][j] > miniDist[i][j] + 1):
                miniDist[i + 1][j] = miniDist[i][j] + 1
                Dist.put((miniDist[i + 1][j] + Distance[i+1][j],(i + 1, j)))
                prevNode[i + 1][j] = (i, j)
        if (j + 1 < 150 and check(i,j + 1)):
            if (miniDist[i][j + 1] > miniDist[i][j] + 1):
                miniDist[i][j + 1] = miniDist[i][j] + 1
                Dist.put((miniDist[i][j + 1]+ Distance[i][j+1],(i,j + 1)))
                prevNode[i][j + 1] = (i, j)
        if (j - 1 >= 0 and check(i,j - 1)):
            if (miniDist[i][j - 1] > miniDist[i][j] + 1):
                miniDist[i][j - 1] = miniDist[i][j] + 1
                Dist.put((miniDist[i][j - 1]+Distance[i][j-1],(i, j-1)))
                prevNode[i][j - 1] = (i, j)
        pg.draw.rect(screen, (0, 0, 255), (i * 4, 4 * j, 4, 4), 0)
        pg.display.update()
    return True