# -*- coding: utf-8 -*-

import pygame

WINDOW_SIZE = [400, 600]  # размер начального экрана
FRAME_COLOR = (0, 255, 204)  # цвет заливки окна

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Змейка')  # title окна

while True:
    # проходим по всем событиям
    for event in pygame.event.get():
        # Если нажали на крестик, то выход
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.display.flip()
