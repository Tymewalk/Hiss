import slither, pygame, time

snakey = slither.Sprite()
snakey.setCostumeByName("costume0") # You can set the default costume (costume0) by name...

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.setCostumeByNumber(0) # ...or you can use a number.

SoExcited.goTo(300, 300)
SoExcited.setScaleTo(0.33) # May look grainy when used on too low a scale.

slither.slitherStage.setColor(40, 222, 40)

slither.setup() # Begin slither

def run_a_frame():
    snakey.changeXBy(1)
    SoExcited.changeDirectionBy(1)

slither.runMainLoop(run_a_frame)
