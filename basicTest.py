from hiss import *

newSprite = Sprite()
newSprite.addCostume("SOS.png")
newSprite.currentCostume = newSprite.costumes[0] # TODO: Make "change costume" block

hissStage.bgcolor = (255, 255, 255)

continueLoop = True
while continueLoop:
    blit() # Display
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
