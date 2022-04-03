import random

from typing import Dict, Tuple
from scenes.Scene import Scene

from components.Barco import Barco as Ship
from components.label import Label
from components.button import Button
from components.board import Board


class Game(Scene):

    def __init__(self, id: int, state: Dict[str, any]):
        Scene.__init__(self, id)

        self.state = state

        self.labels = [
            Label(string="BattleShip", center=True, x=400, y=50,
                  font_size=20, color=(228, 234, 242)),
        ]

        self.buttons = [
            Button(string="HOME", x=50, y=50, font_size=15, action=lambda: self.change(
                0), bg_color=(237, 141, 31), border_color=(186, 105, 13), border=2, padding=20),

            Button(string="HELP", x=150, y=50, font_size=15, action=lambda: self.change(
                1), bg_color=(237, 141, 31), border_color=(186, 105, 13), border=2, padding=20)
        ]

        self.ships = []
        for _ in range(0, self.state["ship_num"]):
            self.ships.append(Ship("Poner nombre", random.randint(0, 3)))

        self.board1 = Board(110, 150, 30, 30, 10, 10, self.ships)
        self.board2 = Board(440, 150, 30, 30, 10, 10, self.ships)

    def render(self, screen):
        screen.fill((1, 18, 38))  # Backgroud color

        super().render(screen)  # draw buttons and labels

        self.board1.render(screen)
        self.board2.render(screen)

    def process_input(self, events, pressed_keys) -> None:
        super().process_input(events, pressed_keys)

        self.board1.process_input(events, pressed_keys)
        self.board2.process_input(events, pressed_keys)
