from typing import Tuple, Callable

import pygame

from components.label import Label


class Button(Label):

    def __init__(self, string: str = "Label",
                 x: int = 0,
                 y: int = 0,
                 action: Callable = lambda: print("No action"),
                 font_size: int = 12,
                 color: Tuple[int, int, int] = (0, 0, 0),
                 bg_color: Tuple[int, int, int] = None,
                 border_color: Tuple[int, int, int] = None,
                 border_radius: int = 5,
                 border: int = 1,
                 padding: int = 10, 
                 enable: bool = True):

        Label.__init__(self,
                       string,
                       x,
                       y,
                       True,
                       font_size,
                       color,
                       bg_color,
                       border_color,
                       border_radius,
                       border, padding,
                       enable)

        self.action = action

    def process_input(self, events, pressed_keys):

        if (self.enable):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= self.rect.x and pygame.mouse.get_pos()[1] >= self.rect.y and pygame.mouse.get_pos()[0] <= (self.rect.x + self.rect.width) and pygame.mouse.get_pos()[1] <= (self.rect.y + self.rect.height):
                    self.action()
