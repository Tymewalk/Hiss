from hiss import *

newSprite = Sprite()
newSprite.addCostume("SOS.png")
newSprite.currentCostume = newSprite.costumes[0] # TODO: Make "change costume" block

while True:
    blit() # Display
