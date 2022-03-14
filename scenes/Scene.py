from typing import Union
from pygame.surface import Surface, SurfaceType


class Scene:

    def __init__(self):
        pass

    def process_input(self, events, pressed_keys) -> None:
        pass

    def update(self):
        pass

    def render(self, screen: Union[Surface, SurfaceType]) -> None:
        pass
