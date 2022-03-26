from typing import List, Tuple, Dict
from pygame.event import Event

import pygame

from scenes.Scene import Scene
from scenes.Menu import Menu
from scenes.Help import Help
from scenes.Game import Game

pygame.init()  # Initialize pygame

# Create and configurate the screen
SIZE: Tuple[int, int] = 500, 500
NAME: str = "BattleShip"
ICON = pygame.image.load("icon.png")

screen = pygame.display.set_mode(SIZE)  # Scream Size
pygame.display.set_caption(NAME)  # Scream Title
pygame.display.set_icon(ICON)  # Scream icon (32x32px)


def main() -> None:
    """Game Loop
    """
    scene_index: int = 0

    scenes: Dict[int, Scene] = {
        0: Menu(0),
        1: Help(1),
        2: Game(2)
    }

    run: bool = True

    while run:
        pressed_keys = pygame.key.get_pressed()
        events: List[Event] = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                events.append(event)

        scenes[scene_index].process_input(events, pressed_keys)
        scenes[scene_index].render(screen)

        # Get the next scene
        scene_index = scenes[scene_index].get_next()

        pygame.display.update()  # Display the changes


if __name__ == '__main__':
    main()
