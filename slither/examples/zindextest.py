import slither, pygame, time

# Normally, since Snakey was made before SoExcited, SoExcited would be rendered after Snakey and be put on top.
snakey = slither.Sprite()

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.costumeNumber = 1

SoExcited.zindex = -1 # But when SoExcited's z-index is set to below that of Snakey's, SoExcited gets rendered before (and thus below) Snakey.

SoExcited.goto(300, 300)
SoExcited.scale = 0.33

slither.slitherStage.bgColor = (40, 40, 222)

slither.setup()

def run_a_frame():
    snakey.xpos += 1
    snakey.ypos += 1
    SoExcited.direction += 1

slither.runMainLoop(run_a_frame)
