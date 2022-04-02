from scenes.Scene import Scene

from components.label import Label 
from components.button import Button

class Help(Scene):

    def __init__(self, id: int):
        Scene.__init__(self, id)

        self.labels = [
            Label(string="Help: How to play BatlleShip", center=True, x=400, y=50,
                  font_size=20, color=(228, 234, 242)),
        ]

        self.buttons = [
            Button(string="PLAY", x=50, y=50, font_size=15, action=lambda: self.change(2), bg_color=(237, 141, 31), border_color=(186, 105, 13), border=2, padding=20),
            Button(string="HOME", x=150, y=50, font_size=15, action=lambda: self.change(0), bg_color=(237, 141, 31), border_color=(186, 105, 13), border=2, padding=20)
        ]

    def render(self, screen):
        screen.fill((1, 18, 38))  # Backgroud color
        
        super().render(screen)  # draw buttons and labels