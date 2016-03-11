import pygame, time, random
# time is for the timer.
# random is for random numbers.
        
class Stage():
    def __init__(self, name):
        self.name = name
        self.costumes = []
        self.currentCostume = False

    def addCostume(self, costumePath):
        costume = pygame.image.load(costumePath)
        self.costumes.append(costume) 

class Sprite(Stage):
    def __init__(self, name):
        Stage.__init__(self, name)
        self.xpos = 0
        self.ypos = 0
        self.direction = 0 # Default is 0, not 90 - it makes more sense
    
def initialize():
    pygame.init()
    hissStage = Stage()
    screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
    caption = pygame.display.set_caption("Hiss Project")
    time.clock()
    # time.clock() (after being called once) will return how long it's been since time.clock() was first called
