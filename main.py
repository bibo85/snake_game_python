# -*- coding: utf-8 -*-

import pygame

WINDOW_SIZE = [400, 600]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Змейка')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
