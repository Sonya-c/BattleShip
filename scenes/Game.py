from scenes.Scene import Scene


class Game(Scene):

    def __init__(self):
        Scene.__init__(self)

    def render(self, screen):
        screen.fill((225, 0, 0))
