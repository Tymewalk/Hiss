import slither, pygame, time

snakey = slither.Sprite()
snakey.setCostumeByName("costume0")

slither.slitherStage.setColor(40, 222, 40)
slither.slitherStage.addCostume("bg.png","bg")
slither.slitherStage.setCostumeByName("bg")

slither.setup() # Begin slither'

def run_a_frame():
    snakey.changeYBy(1)

slither.runMainLoop(run_a_frame)
