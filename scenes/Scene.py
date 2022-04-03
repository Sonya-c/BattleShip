from typing import Dict, Union, List, Sequence
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


    def __init__(self, id: int, state: Dict[str, any]):
        """This is the template of a Scenne

        Args:
            id (int): Id of the scene
            state (Dict[str, any]): global data of the game
        """
        self.id: int = id
        self.state = state
        self.labels: List[Label] = []
        self.buttons: List[Button] = []


    def change_scene(self, scene_id: int):
        """Change the scene 

        Args:
            scene_index (int): id of the scene 
        """
        self.state["scene_id"] = scene_id


    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]) -> None:
        for button in self.buttons:
            button.process_input(events, pressed_keys)


    def render(self, screen: Union[Surface, SurfaceType]) -> None:
        for label in self.labels:
            label.render(screen)

        for button in self.buttons:
            button.render(screen)

            