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

    def __init__(self, window):
        # Properties initialization:
        self.window = window 
        self.view = iso.View(self.window) 
        self.gui = gui.Gui(self.window)
        self.player = player.Player(self)
        self.world = world.World(self)
        self.interface = interface.Interface(self)
        
        # Game loop variables:
        self.done = False  # A flag for the game loop indicating if the game is done playing.
        self.clock = pygame.time.Clock() # Clock to control the framerate
        
        self.world.display()
        self.interface.display()

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
    pygame.init()
    w = 800
    h = 600
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption("SREM")
    pygame.display.set_icon(assets.load_image("icon.png"))
    game = Game(window)
    game.loop()
