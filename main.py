# -*- coding: utf-8 -*-

import pygame

SIZE_BLOCK = 20  # размер блока
COUNT_BLOCKS = 20  # количество блоков в рядах и колонках
MARGIN = 1  # отступ между блоками
HEADER_MARGIN = 70  # отступ шапки
WIDTH = SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS
HEIGHT = HEADER_MARGIN + 2 * SIZE_BLOCK + SIZE_BLOCK * COUNT_BLOCKS + MARGIN * COUNT_BLOCKS
WINDOW_SIZE = [WIDTH, HEIGHT]  # размер начального экрана

# цвета блоков поля
FRAME_COLOR = (0, 255, 204)  # цвет заливки окна
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (204, 255, 255)
HEADER_COLOR = (0, 204, 153)  # цвет заливки шапки
COLOR_SNAKE = (0, 102, 0)


class SnakeBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_block(color, column, row):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                                     SIZE_BLOCK,
                                     SIZE_BLOCK]
                     )


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Змейка')  # title окна

snake_block = [SnakeBlock(9, 9)]

while True:
    # проходим по всем событиям
    for event in pygame.event.get():
        # Если нажали на крестик, то выход
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)  # заливаем фон

    # Заливаем шапку окна цветом
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, WIDTH, HEADER_MARGIN])

    # рисуем игровое поле
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE_COLOR
            else:
                color = WHITE_COLOR
            draw_block(color, column, row)

    for block in snake_block:
        draw_block(COLOR_SNAKE, block.x, block.y)

    pygame.display.flip()  # обновляем экран
