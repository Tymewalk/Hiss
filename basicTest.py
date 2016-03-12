import hiss, pygame, time

newSprite = hiss.Sprite()
newSprite.addCostume("SOS.png")
newSprite.setCostumeByNumber(0) # TODO: Make "change costume" block

hiss.hissStage.setColor(255, 0, 0)

continueLoop = True
while continueLoop:
    hiss.blit() # Display
    newSprite.changeXBy(1)
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
    time.sleep(0.01)    
