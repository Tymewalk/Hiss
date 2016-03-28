import slither, time, math

snakey = slither.Sprite()
snakey.setCostumeByName("costume0")
snakey.ypos = 360

slither.slitherStage.setColor(40, 222, 40)
slither.slitherStage.addCostume("bg2.png", "bg")
slither.slitherStage.setCostumeByName("bg")

slither.setup() # Begin slither'

i = 0
def run_a_frame():
    global i
    snakey.xpos = ((math.sin(i) * 200) + 300)
    i += 0.05

slither.runMainLoop(run_a_frame)
