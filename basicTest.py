import slither, pygame, time


snakey = slither.Sprite()
snakey.setCostumeByName("costume1")

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.setCostumeByNumber(0)

SoExcited.goTo(300, 300)
SoExcited.setScaleTo(0.33)

slither.slitherStage.setColor(255, 0, 0)

screen = slither.setup() # Begin slither

continueLoop = True
while continueLoop:
    slither.blit(screen) # Display
    snakey.changeXBy(1)
    SoExcited.changeDirectionBy(1)
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
    time.sleep(0.01)    
