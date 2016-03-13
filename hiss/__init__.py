import pygame, time, random
# time is for the timer.
# random is for random numbers.

sprites = [] # List of sprites
    
class Stage():
    def __init__(self):
        self.costumes = {}
        self.costumeNumber = 0
        self.currentCostume = False
        self.bgColor = (255, 255, 255)

    # Stage-specific functions
    def setColor(self, r, g, b):
        self.bgColor = (r, g, b)

    # Functions shared by sprites
    def addCostume(self, costumePath, costumeName):
        costume = pygame.image.load(costumePath)
        self.costumes[costumeName] = costume

    def setCostumeByName(self, name):
        if name in self.costumes:
            self.currentCostume = self.costumes[name]
            self.costumeNumber = self.costumes.keys().index(name)


hissStage = Stage()

class Sprite(Stage):
    def __init__(self, name="Default Name"):
        Stage.__init__(self)
        self.name = name # Why is this here?
        self.xpos = 0
        self.ypos = 0
        self.direction = 0 # Default is 0, not 90 - it makes more sense
        self.showing = True
        self.scale = 1 # How much to multiply it by in the scale
        sprites.append(self)
        
    def show(self):
        self.showing = True
        
    def hide(self):
        self.showing = False

    def changeXBy(self, amount):
        self.xpos += amount

    def changeYBy(self, amount):
        self.ypos += amount

    def goTo(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def setXTo(self, xpos):
        self.xpos = xpos

    def setYTo(self, ypos):
        self.ypos = ypos

    def changeScaleBy(self, amount):
        self.scale += amount

    def setScaleTo(self, scale):
        self.scale = scale

    def isVisible(self):
        '''Check if the object is visible, not just showing.'''
        return self.showing and self.scale > 0

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
caption = pygame.display.set_caption("Hiss Project")
time.clock()

def blit():
    screen.fill(hissStage.bgColor)
    
    for obj in sprites:
        if obj.isVisible():
            # Now that we know the object's showing, do calculations and stuff
            image = obj.currentCostume # So we can modify it
            if not obj.scale == 1: # Don't do anything if it's a scale of 1
                imageSize = image.get_size()
                image = pygame.transform.scale(image, (int(imageSize[0] * obj.scale), int(imageSize[1] * obj.scale)))
            screen.blit(image, (obj.xpos, obj.ypos))

    pygame.display.flip()
    
