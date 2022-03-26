from scenes.Scene import Scene

import pygame


class Menu(Scene):
    """This is the fist scene that the user will see. It's contains two options:
    - Help: a user guide of the game
    - Game: the main game
    """

    def render(self, screen) -> None:
        screen.fill((48, 105, 152))

    def process_input(self, events, pressed_keys) -> None:
        if pressed_keys[pygame.K_1]:
            self.next = 1
