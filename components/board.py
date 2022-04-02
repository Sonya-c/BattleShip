
from typing import List

import pygame

from component import Component
from components.button import Button


class Board(Component):

    def __init__(self, x: int, y: int, box_w: int, box_h: int, rows: int, cols: int) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.box_w = box_w
        self.box_h = box_h

        self.board_table = []
        self.buttons: List[List[Button]] = []

        box_y = y
        for row in range(0, rows):
            box_x = x

            self.buttons.append([])

            for col in range(0, cols):

                self.buttons[row].append(
                    Button(" ",
                           box_x,
                           box_y,
                           lambda row = row, col = col: self.change(row, col),
                           color=(1, 18, 38),
                           bg_color=(235, 245, 241),
                           border_color=(213, 219, 217),
                           border=1,
                           padding=20)
                )

                box_x += self.buttons[row][col].rect.width + 5
                # print(box_x, box_y)

            box_y += self.buttons[row][col].rect.height + 5

    def change(self, x: int, y: int):
        # To Do logic here
        self.buttons[x][y].string = "x"
        self.buttons[x][y].update()

    def render(self, screen) -> None:
        super().render(screen)

        for row in self.buttons:
            for button in row:
                button.render(screen)

    def process_input(self, events, pressed_keys) -> None:
        for row in self.buttons:
            for button in row:
                button.process_input(events, pressed_keys)
