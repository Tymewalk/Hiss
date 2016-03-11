import pygame, time, random
# time is for the timer.
# random is for random numbers.

sprites = [] # List of sprites
    
class Stage():
    def __init__(self):
        self.costumes = []
        self.currentCostume = False

    def addCostume(self, costumePath):
        costume = pygame.image.load(costumePath)
        self.costumes.append(costume)

class Sprite(Stage):
    def __init__(self, name="Default Name"):
        Stage.__init__(self)
        self.name = name
        self.xpos = 0
        self.ypos = 0
        self.direction = 0 # Default is 0, not 90 - it makes more sense
        self.showing = True
        sprites.append(self)
        
    def show(self):
        self.show = True
        
    def hide(self):
        self.show = False
    
pygame.init()
hissStage = Stage()
screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
caption = pygame.display.set_caption("Hiss Project")
time.clock()

def blit():
    for obj in sprites:
        if obj.showing:
            screen.blit(obj.currentCostume, (obj.xpos, obj.ypos))

    pygame.display.flip()
