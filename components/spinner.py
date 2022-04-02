import pygame

from math import inf
from typing import Tuple
from component import Component

from components.button import Button
from components.label import Label


class Spinner(Component):

    def __init__(self,
                 x: int,
                 y: int,
                 start: int = 0,
                 min: int = -inf,
                 max: int = inf,
                 step=1,
                 color: Tuple[int, int, int] = (1, 18, 38),
                 bg_color: Tuple[int, int, int] = (228, 234, 242),
                 border_color: Tuple[int, int, int] = (188, 194, 202)
                 ) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.value = start
        self.min = min
        self.max = max
        self.step = step
        self.bg_color = bg_color
        self.border_color = border_color

        self.button_down = Button(
            "<", x, y, lambda: self.spin(-step), color=color, padding=10)

        self.label: Label = Label(
            str(start), x + self.button_down.rect.width, y, True, color=color, font_size=20, padding=10)

        self.button_up = Button(">", x + self.button_down.rect.width +
                                self.label.rect.width, y, lambda: self.spin(step), color=color, padding=10)

        self.w = self.button_down.rect.w + self.label.rect.w + self.button_up.rect.w

    def spin(self, delta: int = 0):
        if (self.value + delta <= self.max and self.value + delta >= self.min):
            self.value += delta
            self.label.string = str(self.value)
            self.label.update()

    def render(self, screen) -> None:
        super().render(screen)

        # Background color
        pygame.draw.rect(screen,
                         self.bg_color,
                         pygame.Rect(self.x - 15,
                                     self.y - 15,
                                     self.w + 10,
                                     self.button_down.rect.h + 10),
                         0, 10)

        # Border
        pygame.draw.rect(screen,
                         self.border_color,
                         pygame.Rect(self.x - 15,
                                     self.y - 15,
                                     self.w + 10,
                                     self.button_down.rect.h + 10),
                         2, 10)

        self.button_down.render(screen)
        self.label.render(screen)
        self.button_up.render(screen)

    def process_input(self, events, pressed_keys) -> None:
        if (self.enable):
            self.button_down.process_input(events, pressed_keys)
            self.button_up.process_input(events, pressed_keys)
