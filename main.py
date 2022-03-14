import pygame

from scenes.Menu import Menu
from scenes.Help import Help
from scenes.Game import Game

pygame.init()  # Initialize pygame

# Create and configurate the screen
SIZE: (int, int) = 500, 500
NAME: str = "PygameTutorial"
ICON = pygame.image.load("icon.png")

screen = pygame.display.set_mode(SIZE)  # Scream Size
pygame.display.set_caption(NAME)  # Scream Title
pygame.display.set_icon(ICON)  # Scream icon (32x32px)


sceneIndex: int = 0
scenes = {
    0: Menu(),
    1: Help(),
    2: Game()
}


def main() -> None:
    """Game Loop
    """

    run: bool = True

    while run:
        pressed_keys = pygame.key.get_pressed()
        events = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                events.append(event)

        scenes[sceneIndex].process_input(events, pressed_keys)
        scenes[sceneIndex].render(screen)

        pygame.display.update()  # Display the changes


if __name__ == '__main__':
    main()
