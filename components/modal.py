import pygame

from typing import Callable, List, Tuple

from component import Component

from components.label import Label
from components.button import Button

class Modal(Component):


    def __init__(self, 
            msg: str,
            x: int, 
            y: int,
            w: int,
            h: int,
            bg_color: Tuple[int, int, int] = (228, 237, 242),
            action: Callable = lambda: print("No action"),
            enable: bool = True) -> None:

        super().__init__(enable)

        self.msg = msg
        self.bg_color = bg_color
        self.visible = True
        
        self.buttons: List[Button] = [
            Button("x", x + 10, y + 10, lambda: self.close(), font_size=20,color=(232, 232, 232), bg_color=(219, 0, 37)),
            Button("Jugar de nuevo", x + w//2, y + h//2 + 30, bg_color=(20, 144, 163), font_size=20, action=action)
        ]

        self.labels: List[Label] = [
            Label("Fin de la partida", x + w//2, y + 10, center=True, font_size=15),
            Label(msg, x + w//2, y + h//2, center=True, font_size=15)
        ]

        self.container = pygame.Rect(x, y, w, h,)


    def close(self):
        self.visible = False


    def set_msg(self, msg: str):
        self.labels[1].string = msg
        self.labels[1].update()


    def render(self, screen) -> None:

        if (self.visible):
            pygame.draw.rect(screen, self.bg_color, self.container, 0, 10)  # background color
            pygame.draw.rect(screen, (224, 31, 60), self.container, 1, 10)  # border

            for button in self.buttons:
                button.render(screen)
            
            for label in self.labels:
                label.render(screen)

            super().render(screen)


    def process_input(self, events, pressed_keys) -> None:

        if (self.visible):
            super().process_input(events, pressed_keys)    
        
            for button in self.buttons:
                button.process_input(events, pressed_keys)

