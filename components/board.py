
from msilib.schema import tables
import random
from typing import List

import pygame

from components.Barco import Barco as Ship
from component import Component
from components.button import Button


class Board(Component):

    def __init__(self, x: int, y: int, box_w: int, box_h: int, rows: int, cols: int, ships: List[Ship], hide: bool = False) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.box_w = box_w
        self.box_h = box_h
        self.ships = ships
        self.hide = hide

        self.board_table = []
        self.buttons: List[List[Button]] = []

        box_y = y
        for row in range(0, rows):
            box_x = x

            self.buttons.append([])
            self.board_table.append([0]*cols)

            for col in range(0, cols):

                self.buttons[row].append(
                    Button(" ",
                           box_x,
                           box_y,
                           lambda row=row, col=col: self.change(row, col),
                           color=(1, 18, 38),
                           bg_color=(235, 245, 241),
                           border_color=(213, 219, 217),
                           border=1,
                           padding=20)
                )

                box_x += self.buttons[row][col].rect.width + 5
                # print(box_x, box_y)

            box_y += self.buttons[row][col].rect.height + 5
        self.generate()

    def change(self, x: int, y: int):
        # To Do logic here
        if (self.board_table[x][y] == 1):
            self.board_table[x][y] = -1
            self.buttons[x][y].bg_color = (219, 0, 37)
            self.buttons[x][y].update()

    def generate(self):
        print("board.generate len of ships", len(self.ships))
        for ship in self.ships:

            while True:
                pos = (random.randint(0, 10), random.randint(0, 10))
                direction = (random.randint(0, 1), random.randint(0, 1))

                points = self.ship_points(pos, ship.get_size(), direction)

                if (points != None):
                    for point in points:
                        self.board_table[point[0]][point[1]] = 1
                        if (not self.hide):
                            self.buttons[point[0]][point[1]
                                                   ].bg_color = (80, 174, 217)
                    break

        print(self.board_table)

    def ship_points(self, pos=(3, 3), ship_size=4, direction=(1, 0)):
        points = []
        for i in range(ship_size):
            points.append((pos[0]+i*direction[0], pos[1]+i*direction[1]))
            if points[i][0] >= 10 or points[i][1] >= 10:
                return None
        return points

    def render(self, screen) -> None:
        super().render(screen)

        for row in self.buttons:
            for button in row:
                button.render(screen)

    def process_input(self, events, pressed_keys) -> None:
        if (self.enable):
            for row in self.buttons:
                for button in row:
                    button.process_input(events, pressed_keys)
