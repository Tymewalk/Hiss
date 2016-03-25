import slither, pygame, time

# Normally, since Snakey was made before SoExcited, SoExcited would be rendered after Snakey and be put on top.
snakey = slither.Sprite()
snakey.setCostumeByName("costume0")

SoExcited = slither.Sprite()
SoExcited.addCostume("SoExcited.png", "avatar")
SoExcited.setCostumeByNumber(0)

SoExcited.changeZIndexBy(-1) # But when SoExcited's z-index is set to below that of Snakey's, SoExcited gets rendered before (and thus below) Snakey.

SoExcited.goTo(300, 300)
SoExcited.setScaleTo(0.33)

slither.slitherStage.setColor(40, 40, 222)

slither.setup()

def run_a_frame():
    snakey.changeXBy(1)
    snakey.changeYBy(1)
    SoExcited.changeDirectionBy(1)

slither.runMainLoop(run_a_frame)
