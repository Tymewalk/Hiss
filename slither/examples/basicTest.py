import slither, pygame, time

snakey = slither.Sprite()
snakey.costumeName = "costume0" # You can set the default costume (costume0) by name...
snakey.ypos = 100

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.costumeNumber = 1 # ...or you can use a number.

SoExcited.goto(300, 300)
SoExcited.scale = 0.33 # May look grainy when used on too low a scale.

slither.slitherStage.bgColor = (40, 222, 40)

slither.setup() # Begin slither

def run_a_frame():
    snakey.xpos += 1
    SoExcited.direction += 1

slither.runMainLoop(run_a_frame)
