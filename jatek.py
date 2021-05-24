import pygame
import random


pygame.init()

#Ablak mérete
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kígyók Kígyóznak")

#Változók
cella_merete = 20
irany = 1
kigyo_frissit = 0
kaja = [0, 0]
uj_kaja = True
uj_darab = [0, 0]
pontszam = 0

#Betűtípus
betutipus = pygame.font.SysFont(None, 40)

#Színek
belso_resz = (50, 175, 25)
kulso_resz = (100, 100, 200)
fej_szine = (255, 0, 0)
hatterszin = (200, 250, 100)
kaja_szine = (200, 50, 50)


#Kigyó
kigyo_helye = [[int (screen_width / 2), int(screen_height / 2)]]
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete])
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete * 2])
kigyo_helye.append([int (screen_width / 2), int(screen_height / 2) + cella_merete * 3])

#Funkciók
def hatter_kirajzolasa():
    screen.fill(hatterszin)

def pontszam_kirajzolasa():
    pontszam_txt = "Pontszám: " + str(pontszam)
    pontszam_img = betutipus.render(pontszam_txt, True, (100, 50, 255))
    screen.blit(pontszam_img, (0,0))


run = True
while run:

    hatter_kirajzolasa()
    pontszam_kirajzolasa()

#Irányítás
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

#Kaja megcsinálása
    if uj_kaja == True:
        uj_kaja = False
        kaja[0] = cella_merete * random.randint(0, (screen_width / cella_merete) - 1)
        kaja[1] = cella_merete * random.randint(0, (screen_width / cella_merete) - 1)

#Kaja kirajzolása
    pygame.draw.rect(screen, kaja_szine, (kaja[0], kaja[1], cella_merete, cella_merete))

#Kaja ellenörzése
    if kigyo_helye[0] == kaja:
        uj_kaja = True
        #Új részt csinál a kígyó végénél
        uj_darab = list(kigyo_helye[-1])
        #Hozzáad egy új darabot a kígyóhoz
        if irany == 1:
            uj_darab[1] += cella_merete
        if irany == 2:
            uj_darab[0] += cella_merete
        if irany == 3:
            uj_darab[1] -= cella_merete
        if irany == 4:
            uj_darab[0] += cella_merete


        kigyo_helye.append(uj_darab)

        pontszam += 1

    if kigyo_frissit > 170:
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