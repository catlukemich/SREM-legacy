import pygame
import assets
import player
import iso
import gui
import world
import interface
from tkinter import *

# The main game class that is intantiated on startup.
class Game:

    def __init__(self, w, h):
        # Screen setup
        pygame.init()
        self.window = pygame.display.set_mode((w, h))
        pygame.display.set_caption("SREM")
        pygame.display.set_icon(assets.load_image("icon.png"))
        # The onscreen display objects creation:
        self.view = iso.View(self.window)
        self.gui = gui.Gui(self.window)
        # Player control object
        self.player = player.Player(self)
        # World creation
        self.world = world.World(self)
        self.world.display()
        # Interface creation
        self.interface = interface.Interface(self)
        self.interface.display()
        # Utilities
        self.done = False  # A flag for the game loop indicating if the game is done playing.
        self.clock = pygame.time.Clock() # Clock to control the framerate

    def loop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                else:
                    self.gui.on_event(event)

            self.update(self.clock)
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

    def update(self, clock):
        self.world.update(clock)
        self.interface.update(clock)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.view.draw()
        self.gui.draw()


if __name__ == "__main__":
    w = 800
    h = 600
    game = Game(w, h)
    game.loop()
