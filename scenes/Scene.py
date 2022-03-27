from typing import Union, List, Sequence
from pygame.event import Event
from pygame.surface import Surface, SurfaceType

from component import Component
from components.button import Button
from components.label import Label

class Scene(Component):
    """This class defines the basic components of a Scene:
    - Each scene must have and id
    - The next artribute define the next scene to draw
    Also, a secene must be able of:
    - procees_input: given a list of events and pressed keys, procees that input
    - render: draw 
    - get_next: return the next secen
    """

    def __init__(self, id: int):
        self.id: int = id
        self.next: int = id
        self.labels: List[Label] = []
        self.buttons: List[Buttons] = []

    def change(self, id: int):
        self.next = id
        
    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]) -> None:
        for button in self.buttons:
            button.process_input(events, pressed_keys)

    def render(self, screen: Union[Surface, SurfaceType]) -> None:
        for label in self.labels:
            label.render(screen)

        for button in self.buttons:
            button.render(screen)

    def get_next(self) -> int:
        """This method return the id of the next scene to draw. 
        By default, it's the same id of the current scene.
        But it can change after processing input

        Returns:
            int: the id of the next scene 
        """
        return self.next