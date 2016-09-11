# SLITHER FOR PYTHON 2 AND 3
# Hi there, code divers!
# There's a lot of cool stuff here that has comments so you can understand what's going on.
# You can even mess around with it yourself :)
# If you think your messing around might help, go to:
# https://github.com/PySlither/Slither
# and make a pull request!

import pygame
import sys, os, collections, warnings, math

WIDTH, HEIGHT = (800, 600)
SCREEN_SIZE = (WIDTH, HEIGHT)

sprites = [] # List of all sprites
clock = pygame.time.Clock() # Used to control framerate
eventnames = ['QUIT', 'ACTIVEEVENT', 'KEYDOWN', 'KEYUP', 'MOUSEMOTION', 'MOUSEBUTTONUP', 'MOUSEBUTTONDOWN',
              'JOYAXISMOTION', 'JOYBALLMOTION', 'JOYHATMOTION', 'JOYBUTTONUP', 'JOYBUTTONDOWN',
              'VIDEORESIZE', 'VIDEOEXPOSE', 'USEREVENT']
eventCallbacks = {
                    getattr(pygame, name): lambda e=None: True
                    for name in eventnames
                } # Create a dict of callbacks that do nothing
globalscreen = None

keysPressed = []

try:
    scriptdir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
except AttributeError:
    warnings.warn("Couldn't find scripts dir, some functions may not work.")
    scriptdir = os.path.realpath(".")


def keysDown():
    "returns the keys that are currently pressed"
    return keysPressed[:]

# Convienience functions
# Taken from http://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
def rotateCenter(image, angle):
    '''rotate a Surface, maintaining position.'''
    rot_sprite = pygame.transform.rotate(image, angle)
    return rot_sprite

class Mouse:
    """A class for getting and setting mouse properties
    This is a static class, all functions should be called directly through the class"""
    _v = True
    
    @staticmethod
    def buttonsPressed():
        """Returns a three-tuple of bools that gives the state 
        of the left, middle, and right buttons"""
        return tuple(bool(state) for state in pygame.mouse.get_pressed())
    
    @staticmethod
    def leftPressed():
        return Mouse.buttonsPressed()[0]
    
    @staticmethod
    def middlePressed():
        return Mouse.buttonsPressed()[1]
    
    @staticmethod
    def rightPressed():
        return Mouse.buttonsPressed()[2]
    
    @staticmethod
    def pos():
        return pygame.mouse.get_pos()
    
    @staticmethod
    def xPos():
        return Mouse.pos()[0]
    
    @staticmethod
    def yPos():
        return Mouse.pos()[1]
    
    @staticmethod
    def relativeMovement():
        "Returns how much the mouse has moved since the last call to this function"
        return pygame.mouse.get_rel()
    
    @staticmethod
    def setPos(x, y):
        pygame.mouse.set_pos(x, y)
        
    @staticmethod
    def setXPos(x):
        pygame.mouse.set_pos(x, Mouse.yPos())
        
    @staticmethod
    def setYPos(y):
        pygame.mouse.set_pos(Mouse.xPos(), y)
        
    @staticmethod
    def isVisible():
        return Mouse._v
    
    @staticmethod
    def setVisible(status):
        Mouse._v = pygame.mouse.set_visible(status)
        
    @staticmethod
    def isFocused():
        return bool(pygame.mouse.get_focused())
    
# Stage class
class Stage(object):
    def __init__(self):
        self.snakey = pygame.image.load(os.path.join(os.path.dirname(__file__), "snakey.png"))
        self.costumes = collections.OrderedDict({"costume0" : self.snakey})
        self._costumeNumber = 0
        self._costumeName = "costume0"
        self.currentCostume = None
        self.bgColor = (255, 255, 255)

    # Functions shared by sprites
    def addCostume(self, costumePath, costumeName):
        '''Add a costume based on a given path and name.'''
        costume = pygame.image.load(os.path.join(scriptdir, costumePath))
        self.costumes[costumeName] = costume
        self._costumeName = costumeName # Switch to the new costume

    def deleteCostumeByName(self, name):
        '''Delete a costume by name.'''
        self.costumes.pop(name, None)
        self.recalculateNumberFromName(self.costumeName) # Make sure we recalculate the costume data!

    def deleteCostumeByNumber(self, number):
        '''Delete a costume by number.'''
        if number < len(self.costumes):
            costumeName = self.costumes.keys()[number]
            self.deleteCostumeByName(costumeName) # TODO: Fix this stupid "get name from number" thing

    @property
    def costumeNumber(self):
        '''The number of the costume the sprite is showing'''
        return self._costumeNumber

    @costumeNumber.setter
    def costumeNumber(self, val):
        val = val % len(self.costumes)
        self._costumeName = list(self.costumes.keys())[val]
        self.currentCostume = self.costumes[self.costumeName]
        self._costumeNumber = val

    @property
    def costumeName(self):
        '''The name of the costume the sprite is showing'''
        return self._costumeName

    @costumeName.setter
    def costumeName(self, val):
        if val in self.costumes:
            self._costumeName = val
            self.currentCostume = self.costumes[self.costumeName]


slitherStage = Stage()

# The Sprite inherits things such as the costumes from the stage so everything can be kept in one place.
class Sprite(Stage):
    def __init__(self):
        Stage.__init__(self) # Get all the stuff from the stage, too
        self.currentCostume = self.snakey # By default we should be set to Snakey
        self.xpos = 0 # X Position
        self.ypos = 0 # Y Position
        self.direction = 0 # Direction is how much to change the direction, hence why it starts at 0 and not 90
        self.show = True
        self.scale = 1 # How much to multiply it by in the scale
        self._zindex = 0 # How high up are we in the "z" axis?
        sprites.append(self) # Add this sprite to the global list of sprites

    @property
    def zindex(self):
        '''The location of the sprite in the z-axis. Those with higher z-indexes are displayed above those with lower ones.'''
        return self._zindex

    @zindex.setter
    def zindex(self, val):
        #if val < 0 or int(val) != val:
        #    raise ValueError("zindex must be a non-negative integer")
        self._zindex = val
        reorderSprites()

    def goto(self, xpos, ypos):
        '''Go to xpos, ypos.'''
        self.xpos = xpos
        self.ypos = ypos
    
    def moveSteps(self, numSteps):
        """Move numSteps steps in the current direction"""
        self.goto(self.xpos + math.cos(math.radians(self.direction)) * numSteps,
                  self.ypos + math.sin(math.radians(self.direction)) * numSteps)

    def isVisible(self):
        '''Check if the object is visible, not just showing.
        This is better than Sprite.show because it also checks the scale.'''
        return self.show and self.scale > 0

    def delete(self):
        '''Remove the sprite from the global sprites list, causing it not to be drawn.'''
        sprites.remove(self)

    def isTouching(self, collideSprite):
        '''Detects if one sprite is touching another.'''
        ourRect = self.currentCostume.get_rect()
        theirRect = collideSprite.currentCostume.get_rect()
        ourRect.center = (self.xpos, self.ypos)
        theirRect.center = (collideSprite.xpos, collideSprite.ypos)
        return ourRect.colliderect(theirRect)

pygame.mixer.init(44100, -16, 2, 2048)

class Sound():
    # Based on pygame examples, http://stackoverflow.com/questions/8690301/pygame-memoryerror
    def loadSound(self, name):
        '''Load a sound. Set this function to a variable then call variable.play()'''
        try:
            pygame.mixer.get_init()
        except:
            pass
        class NoneSound:
            def play(self): pass
        if not pygame.mixer:
            return NoneSound()
        fullname = os.path.join(scriptdir, name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error as e:
            print ('Cannot load sound: %s' % fullname)
            raise e
        return sound

slitherSound = Sound()

# Convienience function to blit text
def blitText(text, x=0, y=0, size=12, font=False, fontPath=False, antialias=0, color=(0,0,0)):
    global globalscreen
    if font:
        textFont = pygame.font.SysFont(font, size)
    elif fontPath:
        textFont = pygame.font.Font(fontPath, size)
    else:
        textFont = pygame.font.SysFont("Helvetica", size) # Users should always have Helvetica installed

    textImage = textFont.render(text, antialias, color)

    globalscreen.blit(textImage, (x, y))

    #pygame.display.flip()

def setup(caption=sys.argv[0]):
    '''Sets up PyGame and returns a screen object that can be used with blit().'''
    global globalscreen
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    caption = pygame.display.set_caption(caption)
    globalscreen = screen
    return screen

projectFPS = 60 # 60 is the default
def setFPS(fps):
    '''Set the FPS of the project. Default is 60, and Scratch runs at 30.'''
    global projectFPS
    projectFPS = fps # projectFPS is the FPS that the main loop uses

def reorderSprites():
    global sprites
    sprites = sorted(sprites, key=(lambda s: s.zindex))

def blit(screen):
    '''Takes a screen as an argument and draws objects to the screen. THIS MUST BE CALLED FOR SLITHER TO DISPAY OBJECTS.'''
    if screen:
        screen.fill(slitherStage.bgColor)

        if slitherStage.currentCostume:
            screen.blit(pygame.transform.scale(slitherStage.currentCostume, SCREEN_SIZE), (0, 0))

        for obj in sprites:
            if obj.isVisible(): # Check if the object is showing before we do anything
                image = obj.currentCostume # So we can modify it and blit the modified version easily
                # These next few blocks of code check if the object has the defaults before doing anything.
                if not obj.scale == 1:
                    imageSize = image.get_size()
                    image = pygame.transform.scale(image, (int(imageSize[0] * obj.scale), int(imageSize[1] * obj.scale)))
                if not obj.direction == 0:
                    image = rotateCenter(image, -obj.direction)
                new_rect = image.get_rect()
                new_rect.center = (obj.xpos, obj.ypos)
                screen.blit(image, new_rect)

    #pygame.display.flip()

def registerCallback(eventname, func=None):
    '''Register the function func to handle the event eventname'''
    if func:
        # Direct call (registerCallback(pygame.QUIT, func))
        eventCallbacks[eventname] = func
    else:
        # Decorator call (@registerCallback(pygame.QUIT)
        #                 def f(): pass
        def f(func):
            eventCallbacks[eventname] = func
        return f

def runQuitCallback():
    return eventCallbacks[pygame.QUIT]()

def runMainLoop(frameFunc):
    while True:
        blit(globalscreen)
        frameFunc()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if runQuitCallback():
                    # runQuitCallback would run the function
                    # given to setQuitCallback, and return its result
                    pygame.quit()
                    sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    keysPressed.append(pygame.key.name(event.key))
                elif event.type == pygame.KEYUP:
                    keysPressed.remove(pygame.key.name(event.key))
                eventCallbacks[event.type](event)
                # eventCallbacks would be a dictionary mapping
                # event types to handler functions.
        pygame.display.flip() # Always flip at the end
        clock.tick(projectFPS) # Run at however many FPS the user specifies
