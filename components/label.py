from typing import Tuple

import pygame

from component import Component


class Label(Component):

    def __init__(self, string: str = "Label",
                 x: int = 0,
                 y: int = 0,
                 center: bool = False,
                 font_size: int = 12,
                 color: Tuple[int, int, int] = (0, 0, 0),
                 bg_color: Tuple[int, int, int] = None,
                 border_color: Tuple[int, int, int] = None,
                 border_radius: int = 5,
                 border: int = 1,
                 padding: int = 0):
        """Create a label component that display some text

        Args:
            string (str, optional): The text to display. Defaults to "Label".
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordiante. Defaults to 0.
            center (bool, optional): if it's True, the text will be centered. Defaults to False.Defaults to "freesansbold.ttf".
            font_size (int, optional): font type. Defaults to 12.
            color (Tuple[int, int, int], optional): Text color. Defaults to (0, 0, 0).
            bg_color (Tuple[int, int, int], optional): Background color. Defaults to None.
            border_color (Tuple[int, int, int], optional): Border color. Defaults to None.
            border_radius (int, optional): Border radius. Defaults to 5.
            botder (int, optional): Boder size. Defaults to 1
            padding (int, optional): padding. Defaults to 0.
        """
        super().__init__()
        self.string = string
        self.x = x
        self.y = y
        self.center = center
        self.font_size = font_size
        self.color = color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_radius = border_radius
        self.border = border
        self.padding = padding

        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.getRect()

    def getRect(self):
        self.text = self.font.render(self.string, True, self.color)

        # this is the box that contains the text
        text_rect = self.text.get_rect()

        # this is the box that contains the text, the position and the padding
        self.rect = pygame.Rect(
            self.x,
            self.y,
            text_rect.width + self.padding,
            text_rect.height + self.padding)

        # text align
        if (self.center):
            self.rect.center = (self.x, self.y)
        else:
            # align left
            self.rect.topleft = (self.x, self.y)

    def update(self):
        self.getRect()

    def render(self, screen):

        # self.getRect()

        # background color
        if (self.bg_color != None):
            # screen.fill(self.bg_color, rect = self.rect)
            pygame.draw.rect(screen,
                             self.bg_color,
                             self.rect, 0, self.border_radius)

        # border
        if (self.border_color != None and self.border > 0):
            pygame.draw.rect(screen,
                             self.border_color,
                             self.rect,
                             self.border,
                             self.border_radius)

        # display text
        screen.blit(self.text,
                    (self.rect.x + int(self.padding/2),
                     self.rect.y + int(self.padding/2))
                    )
