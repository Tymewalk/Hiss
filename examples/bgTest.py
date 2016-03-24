import slither, pygame, time, os, math
snakey = slither.Sprite()
snakey.setCostumeByName("costume0")
snakey.setXTo(300)
slither.slitherStage.setColor(40, 222, 40)
slither.slitherStage.addCostume(os.path.join(os.path.dirname(__file__), "bg.png"), "bg")
slither.slitherStage.setCostumeByName("bg")

slither.setup() # Begin slither'

i = 0
def run_a_frame():
    global i
    snakey.setYTo((math.sin(i) * 200) + 200)
    i += 0.05

slither.runMainLoop(run_a_frame)
