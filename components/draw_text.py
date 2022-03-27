from typing import Tuple
import pygame


def draw_text(string: str = "", x: int = 0, y: int = 0, font: str = 'freesansbold.ttf', font_size: int = 12, color: Tuple[int, int, int] = (0, 0, 0)):
    """Draw some text on the string

    Args:
        string (str): Text to draw
        x (int): x position
        y (int): y position_
        font_size (int): font size

    Returns:
        _type_: use screen.blit(return[0], return[1])
    """

    font = pygame.font.Font(font, font_size)

    text = font.render(string, True, color)

    text_rect = text.get_rect()
    text_rect.center = (x, y)

    return (text, text_rect)
