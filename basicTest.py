import slither, pygame, time


snakey = slither.Sprite()
snakey.setCostumeByName("costume0")

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.setCostumeByNumber(0)

SoExcited.goTo(300, 300)
SoExcited.setScaleTo(0.33)

slither.slitherStage.setColor(40, 222, 40)

screen = slither.setup() # Begin slither

def run_a_frame():
    snakey.changeXBy(1)
    SoExcited.changeDirectionBy(1)

slither.runMainLoop(run_a_frame)
