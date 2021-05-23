import pygame
from pygame.locals import *

pygame.init()

#Ablak mérete
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kígyók Kígyóznak")

#Változók
cella_merete = 15
irany = 1
kigyo_frissit = 0


#Színek
belso_resz = (50, 175, 25)
kulso_resz = (100, 100, 200)
fej_szine = (255, 0, 0)
hatterszin = (200, 250, 100)

#Kigyó
kigyo_helye = [[int (screen_width / 2), int(screen_height / 2)]]
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete])
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete * 2])
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete * 3])

def hatter():
    screen.fill(hatterszin)

run = True
while run:
    hatter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and irany != 3:
                irany = 1
            if event.key == pygame.K_RIGHT and irany != 4:
                irany = 2
            if event.key == pygame.K_DOWN and irany != 1:
                irany = 3
            if event.key == pygame.K_LEFT and irany != 2:
                irany = 4




    if kigyo_frissit > 99:
        kigyo_frissit = 0
        kigyo_helye = kigyo_helye[-1:] + kigyo_helye[:-1]
        #fel
        if irany == 1:
            kigyo_helye[0][0] = kigyo_helye[1][0]
            kigyo_helye[0][1] = kigyo_helye[1][1] - cella_merete
        #jobbra
        if irany == 2:
            kigyo_helye[0][1] = kigyo_helye[1][1]
            kigyo_helye[0][0] = kigyo_helye[1][0] + cella_merete
        #le
        if irany == 3:
            kigyo_helye[0][0] = kigyo_helye[1][0]
            kigyo_helye[0][1] = kigyo_helye[1][1] + cella_merete
        #balra
        if irany == 4:
            kigyo_helye[0][1] = kigyo_helye[1][1]
            kigyo_helye[0][0] = kigyo_helye[1][0] - cella_merete

#Kígyó megcsinálása
    fej = 1
    for x in kigyo_helye:

        if fej == 0:
            pygame.draw.rect(screen, kulso_resz, (x[0], x[1], cella_merete, cella_merete))
            pygame.draw.rect(screen, belso_resz, (x[0] + 1, x[1] + 1, cella_merete - 2, cella_merete - 2))
        if fej == 1:
            pygame.draw.rect(screen, kulso_resz, (x[0], x[1], cella_merete, cella_merete))
            pygame.draw.rect(screen, fej_szine, (x[0] + 1, x[1] + 1, cella_merete - 2, cella_merete - 2))
            fej = 0


    pygame.display.update()

    kigyo_frissit += 1

pygame.quit()