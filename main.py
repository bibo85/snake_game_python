# -*- coding: utf-8 -*-

import pygame

SIZE_BLOCK = 20  # размер блоке
COUNT_BLOCKS = 20  # количество блоков в ряду и колонках
WINDOW_SIZE = [500, 600]  # размер начального экрана
FRAME_COLOR = (0, 255, 204)  # цвет заливки окна
MARGIN = 1  # отступ между блоками

# цвета блоков поля
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (204, 255, 255)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Змейка')  # title окна

while True:
    # проходим по всем событиям
    for event in pygame.event.get():
        # Если нажали на крестик, то выход
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)  # заливаем фон

    # рисуем игровой блок на поле
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE_COLOR
            else:
                color = WHITE_COLOR
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * column,
                                             20 + row * SIZE_BLOCK + MARGIN * row,
                                             SIZE_BLOCK,
                                             SIZE_BLOCK]
                             )

    pygame.display.flip()  # обновляем экран
