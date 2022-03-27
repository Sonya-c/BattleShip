from typing import Tuple
import pygame

from component import Component


class Label(Component):

    def __init__(self, string: str = "Label",
                 x: int = 0,
                 y: int = 0,
                 center: bool = False,
                 font: str = "freesansbold.ttf",
                 font_size: int = 12,
                 color: Tuple[int, int, int] = (0, 0, 0),
                 bg_color: Tuple[int, int, int] = None):

        self.string = string
        self.x = x
        self.y = y
        self.center = center
        self.font = pygame.font.Font(font, font_size)
        self.font_size = font_size
        self.color = color

        self.text = self.font.render(self.string, True, self.color)
        self.text_rect = self.text.get_rect()

    def render(self, screen):
        self.text = self.font.render(self.string, True, self.color)
        self.text_rect = self.text.get_rect()

        if (self.center):
            self.text_rect.center = (self.x, self.y)
        else:
            self.text_rect.left = self.x
            self.text_rect.top = self.y

        screen.blit(self.text, self.text_rect)
