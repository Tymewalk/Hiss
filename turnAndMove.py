import slither, pygame, time


snakey = slither.Sprite()
snakey.setCostumeByName("costume0")

snakey.goTo(0, 250)

slither.slitherStage.setColor(40, 222, 40)

screen = slither.setup() # Begin slither

continueLoop = True
while continueLoop:
    slither.blit(screen) # Display
    snakey.changeXBy(1)
    snakey.changeDirectionBy(1)
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
    time.sleep(0.01)    
