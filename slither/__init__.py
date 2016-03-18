import pygame, time, random
# time is for the timer.
# random is for random numbers.

sprites = [] # List of all sprites
    
class Stage():
    def __init__(self):
        self.snakey = pygame.image.load("snakey.png")
        self.costumes = {"costume0" : self.snakey}
        self.costumeNumber = 0
        self.costumeName = "costume0"
        self.currentCostume = self.snakey
        self.bgColor = (255, 255, 255)

    # Stage-specific functions
    def setColor(self, r, g, b):
        '''Set the stage's color. Only works on the stage, not sprites.'''
        self.bgColor = (r, g, b)

    # Functions shared by sprites
    def addCostume(self, costumePath, costumeName):
        '''Add a costume based on a given path and name.'''
        costume = pygame.image.load(costumePath)
        self.costumes[costumeName] = costume

    def deleteCostumeByName(self, name):
        '''Delete a costume by name.'''
        self.costumes.pop(name, None)
        setCostumeByName(self.costumeName) # Make sure we recalculate the costume number!

    def deleteCostumeByNumber(self, number):
        '''Delete a costume by number.'''
        if number < len(self.costumes.keys()):
            costumeName = self.costumes.keys()[number]
            self.deleteCostumeByName(costumeName)
            
    def setCostumeByName(self, name):
        '''Set a costume by its name.'''
        if name in self.costumes:
            self.currentCostume = self.costumes[name]
            self.costumeName = name
            self.costumeNumber = self.costumes.keys().index(name)

    def setCostumeByNumber(self, number):
        '''Set a costume by its number.'''
        if number < len(self.costumes.keys()):
            costumeName = self.costumes.keys()[number]
            self.setCostumeByName(costumeName)

    def getCostumeNumber(self):
        '''Get the costume number of the sprite.'''
        return self.costumeNumber

    def getCostumeName(self):
        '''Get the costume name of the sprite.'''
        return self.costumeName


slitherStage = Stage()

class Sprite(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.xpos = 0
        self.ypos = 0
        self.direction = 0 # Default is 0, not 90 - it makes more sense
        self.showing = True
        self.scale = 1 # How much to multiply it by in the scale
        sprites.append(self)
        
    def show(self):
        '''Show the sprite.'''
        self.showing = True
        
    def hide(self):
        '''Hide the sprite.'''
        self.showing = False

    def changeXBy(self, amount):
        '''Change the sprite's X Position by (amount).'''
        self.xpos += amount

    def changeYBy(self, amount):
        '''Change the sprite's Y Position by (amount).'''
        self.ypos += amount

    def goTo(self, xpos, ypos):
        '''Go to xpos, ypos.'''
        self.xpos = xpos
        self.ypos = ypos

    def setXTo(self, xpos):
        '''Set the sprite's X Position to (amount).'''
        self.xpos = xpos

    def setYTo(self, ypos):
        '''Set the sprite's Y Position to (amount).'''
        self.ypos = ypos

    def changeScaleBy(self, amount):
        '''Change the sprite's scale by (amount).'''
        self.scale += amount

    def setScaleTo(self, scale):
        '''Set the sprite's scale to (amount).'''
        self.scale = scale
        
    def getScale(self):
        '''Get the sprite's current scale.'''
        return self.scale

    def setDirection(self, direction):
        self.direction = direction

    def changeDirectionBy(self, amount):
        self.direction += amount

    def getDirection(self):
        return self.direction
        
    def isVisible(self):
        '''Check if the object is visible, not just showing.'''
        return self.showing and self.scale > 0

def setup():
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
    caption = pygame.display.set_caption("Slither Project") # Maybe a set caption to function?
    time.clock() # For future timer
    return screen

def blit(screen):
    '''Draw objects to the screen. THIS MUST BE CALLED FOR SLITHER TO DISPAY OBJECTS.'''
    if screen:
        screen.fill(slitherStage.bgColor)
        
        for obj in sprites:
            if obj.isVisible():
                # Now that we know the object's showing, do calculations and stuff
                image = obj.currentCostume # So we can modify it
                if not obj.scale == 1: # Don't do anything if it's a scale of 1
                    imageSize = image.get_size()
                    image = pygame.transform.scale(image, (int(imageSize[0] * obj.scale), int(imageSize[1] * obj.scale)))
                if not obj.direction == 0:
                    image = pygame.transform.rotate(image, obj.direction)
                screen.blit(image, (obj.xpos, obj.ypos))

    pygame.display.flip()
