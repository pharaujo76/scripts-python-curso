import pygame;

pygame.init() ## Inicializando biblioteca 
pygame.mixer.music.load("desafio21.mp3"); ## Carregando a música
pygame.mixer.music.play() ## Dar play na música
input()
pygame.event.wait() ## Esperar a música acabar