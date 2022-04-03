from typing import List, Tuple, Dict
from pygame.event import Event

import pygame

from scenes.Scene import Scene
from scenes.Menu import Menu
from scenes.Game import Game

pygame.init()  # Initialize pygame

# Create and configurate the screen
SIZE: Tuple[int, int] = 800, 550
NAME: str = "Battle Ship"
ICON = pygame.image.load("icon.png")

screen = pygame.display.set_mode(SIZE)  # Scream Size
pygame.display.set_caption(NAME)  # Scream Title
pygame.display.set_icon(ICON)  # Scream icon (32x32px)


def main() -> None:
    run: bool = True

    state: Dict[str, any] = {
        "ship_num": 5, 
        "scene_id": 0
    }

    scenes: Dict[int, Scene] = {
        0: Menu(0, state),
        2: Game(1, state)
    }

    while run:
        pressed_keys = pygame.key.get_pressed()  # List of pressed keys
        events: List[Event] = []  # List of events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            else:
                events.append(event)

        scenes[state["scene_id"]].process_input(events, pressed_keys)
        scenes[state["scene_id"]].render(screen)
        
        pygame.display.update()  # Display the changes


if __name__ == '__main__':
    main()
