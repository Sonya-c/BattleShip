from scenes.Scene import Scene


class Menu(Scene):

    def __init__(self):
        Scene.__init__(self)

    def render(self, screen):
        screen.fill((48, 105, 152))
