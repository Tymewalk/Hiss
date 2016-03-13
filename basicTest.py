import hiss, pygame, time

SOS = hiss.Sprite()
SOS.addCostume("SOS.png", "avatar")
SOS.setCostumeByName("avatar")

SoExcited = hiss.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.setCostumeByName("avatar")

SoExcited.goTo(300, 300)
SoExcited.setScaleTo(0.33)

hiss.hissStage.setColor(255, 0, 0)

continueLoop = True
while continueLoop:
    hiss.blit() # Display
    SOS.changeXBy(1)
    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueLoop = False
    time.sleep(0.01)    
