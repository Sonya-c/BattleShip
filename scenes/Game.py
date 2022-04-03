import random
from tabnanny import check
from turtle import update

from typing import Dict, List, Tuple
from scenes.Scene import Scene

from components.Barco import Barco as Ship
from components.label import Label
from components.button import Button
from components.board import Board


class Game(Scene):


    def __init__(self, id: int, state: Dict[str, any]):
        Scene.__init__(self, id, state)

        self.game_state = {
            "play": True,
            "won": False,
            "turn": 0
        }

        self.labels: List[Label] = [
            Label(string="Battle Ship", center=True, x=400, y=50, font_size=20, color=(228, 234, 242))
        ]

        self.buttons: List[Button] = [
            Button(
                string="HOME", 
                x=50,
                y=50,
                font_size=15,
                action=lambda: self.change_scene(0), 
                bg_color=(237, 141, 31), 
                border_color=(186, 105, 13), 
                border=2, 
                padding=20)
        ]

        self.update()


    def update(self):
        self.game_state["turn"] = 1  # 0: the machine, 1: the gammer
        self.ships: List[Ship] = []

        # Genrate the ships
        for _ in range(0, self.state["ship_num"]):
            self.ships.append(Ship("Poner nombre", random.randint(0, 3)))

        # Create the boards
        self.board_machine = Board(110, 150, 30, 30, 10, 10, 
                                self.ships, 
                                enable=False, 
                                change_turn=lambda: self.change_turn(1))

        self.board_player = Board(440, 150, 30, 30, 10, 10, 
                                self.ships,
                                hide=True,
                                change_turn=lambda: self.change_turn(0))


    def change_turn(self, turn: int):
        if self.game_state["play"]:
            self.game_state["turn"] = turn

            # machine turn 
            if (turn == 0):
                self.board_machine.change(random.randint(0, 9), random.randint(0, 9))
        
    def check(self, board: Board):
        for row in board.board_table:
            for col in row:
                if col == 1:
                    return False

        return True


    def render(self, screen):
        screen.fill((1, 18, 38))  # Backgroud color

        super().render(screen)  # draw buttons and labels

        self.board_machine.render(screen)
        self.board_player.render(screen)

    def process_input(self, events, pressed_keys) -> None:
        super().process_input(events, pressed_keys)

        if self.game_state["play"]:
                self.board_player.process_input(events, pressed_keys)

        if (self.check(self.board_player)):
            self.game_state["won"] = True
            self.game_state["play"] = False

        elif (self.check(self.board_machine)):
            self.game_state["play"] = False