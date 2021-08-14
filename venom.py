import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
sleep(3)
pygame.mixer.init()
pygame.mixer.music.load('No_mercy.mp3')
pygame.mixer.music.play()
sleep(3)
image = pygame.image.load('venom.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(3)
