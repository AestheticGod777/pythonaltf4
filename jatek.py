import pgzrun
import pygame
import time

pygame.init()
dis=pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("kigyok kigyoznak jatekxdxd")
game_over= False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over= True
        print(event)


pygame.quit()
quit()