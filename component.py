from typing import Union, List, Sequence
from pygame.event import Event
from pygame.surface import Surface, SurfaceType


class Component:
    def __init__(self, enable: bool = True) -> None:
        self.enable = enable

    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]) -> None:
        pass  # Ovewrite this

    def render(self, screen: Union[Surface, SurfaceType]) -> None:
        """Draw someting on the screen
        """
        pass  # Overwrite this
