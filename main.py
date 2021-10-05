# -*- coding: utf-8 -*-

import pygame
import pygame_menu
import sys
import random

pygame.init()

SIZE_BLOCK = 20  # размер блока
COUNT_BLOCKS = 20  # количество блоков в рядах и колонках
MARGIN = 1  # отступ между блоками
HEADER_MARGIN = 70  # отступ шапки
WIDTH = SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS
HEIGHT = HEADER_MARGIN + 2 * SIZE_BLOCK + SIZE_BLOCK * COUNT_BLOCKS + MARGIN * COUNT_BLOCKS
WINDOW_SIZE = [WIDTH, HEIGHT]  # размер начального экрана
START_SNAKE_SPEED = 4  # Стартовая скорость змейки -  Частота обновления экрана

# цвета блоков поля
FRAME_COLOR = (0, 255, 204)  # цвет заливки окна
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (204, 255, 255)
HEADER_COLOR = (0, 204, 153)  # цвет заливки шапки
COLOR_SNAKE = (0, 102, 0)
RED_COLOR = (224, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Змейка')  # title окна


class SnakeBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color, column, row):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                                     SIZE_BLOCK,
                                     SIZE_BLOCK]
                     )


def start_the_game():
    # создание рандомной ячейки
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block

    timer = pygame.time.Clock()
    total = 0  # подсчет очков
    font = pygame.font.SysFont('Arial', 18)
    snake_speed_level = 1  # уровень скорости змейки

    snake_blocks = [SnakeBlock(8, 9), SnakeBlock(9, 9), SnakeBlock(10, 9)]
    snake_food = get_random_empty_block()  # Начальная координата змейки

    d_row = buf_row = 0  # отвечает за смену положения по вертикали
    d_col = buf_col = 1  # отвечает за смену положения по горизонтали

    while True:
        # проходим по всем событиям
        for event in pygame.event.get():
            # Если нажали на крестик, то выход
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)  # заливаем фон
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, WIDTH, HEADER_MARGIN])  # Заливаем шапку окна цветом

        # рисуем игровое поле
        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE_COLOR
                else:
                    color = WHITE_COLOR
                draw_block(color, column, row)

        # отрисовка ячейки с едой для змейки
        draw_block(RED_COLOR, snake_food.x, snake_food.y)

        # отрисовка змейки
        head = snake_blocks[-1]  # голова змейки - последний элемент списка

        # змейка столкнулась со стенкой игрового поля
        if not head.is_inside():
            print('Game Over')
            break
            # pygame.quit()
            # sys.exit()
        for block in snake_blocks:
            draw_block(COLOR_SNAKE, block.x, block.y)

        # Ячейка с едой пересекается (змейка съедаем ячейку)
        if snake_food == head:
            snake_blocks.append(snake_food)
            total += 1
            snake_speed_level = total // 5 + 1
            snake_food = get_random_empty_block()

        # Обновление статистики
        text_total = font.render(f'Score: {total}', 0, WHITE_COLOR)
        text_speed = font.render(f'Speed: {snake_speed_level}', 0, WHITE_COLOR)
        screen.blit(text_total, (5, 5))
        screen.blit(text_speed, (5, 25))

        pygame.display.flip()  # обновляем экран

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_col, head.y + d_row)  # на ее основе создаем новую голову

        # если змейка врезалась сама в себя
        if new_head in snake_blocks:
            print('Game Over')
            break
            # pygame.quit()
            # sys.exit()

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        timer.tick(START_SNAKE_SPEED + snake_speed_level)  # задаем скорость змейки - частоту обновления кадров


menu = pygame_menu.Menu('Игра Змейка', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Имя:', default='Игрок 1')
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

menu.mainloop(screen)
