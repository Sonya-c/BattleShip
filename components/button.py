from typing import Tuple, Callable

import pygame
from components.label import Label


class Button(Label):

    def __init__(self, string: str = "Label",
                 x: int = 0,
                 y: int = 0,
                 action: Callable = print("No action"),
                 center: bool = True,
                 font: str = "freesansbold.ttf",
                 font_size: int = 12,
                 color: Tuple[int, int, int] = (0, 0, 0),
                 bg_color: Tuple[int, int, int]  = None):

        Label.__init__(self, string, x, y, center, font, font_size, color, bg_color)
        self.action = action

    def process_input(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pos()[0] >= self.text_rect.x and pygame.mouse.get_pos()[1] >= self.text_rect.y:
                    if pygame.mouse.get_pos()[0] <= (self.text_rect.x + self.text_rect.width) and pygame.mouse.get_pos()[1] <= (self.text_rect.y + self.text_rect.height):
                        self.action()
