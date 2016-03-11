import pygame, time, random
        
class Stage():
    def __init__(self, name):
        self.name = name
        self.costumes = []

    def addCostume(self, costumePath):
        costume = pygame.image.load(costumePath)
        self.costumes.append(costume) 

class Sprite(Stage):
    def __init__(self, name):
        Stage.__init__(self, name)
        self.xpos = 0
        self.ypos = 0
    
def beginGame():
    pygame.init()

    screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
    caption = pygame.display.set_caption("Hiss Project")
