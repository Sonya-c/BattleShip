from typing import Dict, List
import pygame

from scenes.Scene import Scene

from components.label import Label
from components.button import Button
from components.spinner import Spinner


class Menu(Scene):
    """This is the fist scene that the user will see. It's contains two options:
    - Help: a user guide of the game
    - Game: the main game
    """


    def __init__(self, id: int, state: Dict[str, any]):
        Scene.__init__(self, id, state)

        # Load image and change the size
        self.banner = pygame.transform.scale(
            pygame.image.load('./assets/img/banner.jpg'), (800, 400))

        self.labels = [
            Label(string="BATTLESHIP", center=True, x=400, y=50,
                  font_size=50, color=(228, 234, 242)),
            Label(string="AGE * EDAD * IDADE 7+",
                  x=10, y=490, font_size=12, color=(228, 234, 242)),
            Label(string="2 player * 2 joueurs * 2 jugadores * 2 jogadores",
                  x=10, y=510, font_size=10, color=(228, 234, 242)),
            Label(string="Sonya Castro * Natalia Mendoza * Yuli Meza",
                  x=10, y=525, font_size=10, color=(228, 234, 242)),
            Label(string="Número de barcos", x=260,
                  y=186, font_size=20, bg_color=(1, 18, 38), padding=10, color=(228, 234, 242)),
            Label(string="Número de filas", x=260, y=226, font_size=20, bg_color=(1, 18, 38), padding=10, color=(228, 234, 242)),
            Label(string="Número de columnas", x=260, y=266, font_size=20, bg_color=(1, 18, 38), padding=10, color=(228, 234, 242))
        ]

        self.buttons = [
            Button(string="PLAY", 
                x=400,
                y=350,
                font_size=20,
                action=lambda: self.change_scene(1),
                bg_color=(237, 141, 31),
                border_color=(186, 105, 13),
                border=2,
                padding=30)
        ]

        self.spinners: Dict[str, Spinner] = {
            "ship_num": Spinner(490, 200, start= int(state["ship_num"]),min=1, max=10),
            "row_num": Spinner(490, 240, start= int(state["row_num"]),min=5, max=10),
            "col_num": Spinner(490, 280, start= int(state["col_num"]),min=5, max=10)
        }


    def render(self, screen) -> None:
        screen.fill((1, 18, 38))  # Backgroud color

        screen.blit(self.banner, (0, 80))  # Image

        super().render(screen)  # draw buttons and labels

        for _, spinner in self.spinners.items():
            spinner.render(screen)


    def process_input(self, events, pressed_keys) -> None:
        super().process_input(events, pressed_keys)

        
        for spinner_name, spinner in self.spinners.items():
            spinner.process_input(events, pressed_keys)
            
            if (spinner.value != self.state[spinner_name]):
                self.state[spinner_name] = spinner.value
                self.state["update"] = True 
        

        