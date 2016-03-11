import hiss, pygame

newSprite = hiss.Sprite()
newSprite.addCostume("SOS.png")
newSprite.currentCostume = newSprite.costumes[0] # TODO: Make "change costume" block

hiss.hissStage.bgcolor = (255, 0, 0)

continueLoop = True
while continueLoop:
    hiss.blit() # Display
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
