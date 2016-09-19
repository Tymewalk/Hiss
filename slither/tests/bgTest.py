#! usr/bin/env python3
# bgTest.py
import math
import slither

snakey = slither.Sprite()
snakey.ypos = 460

slither.slitherStage.bgColor = (40, 222, 40)
slither.slitherStage.addCostume("assets/bg2.png", "bg")
slither.slitherStage.costumeName = "bg"

slither.setup() # Begin slither'

i = 0
def run_a_frame():
    global i
    snakey.xpos = ((math.sin(i) * 200) + 300)
    i += 0.05

slither.runMainLoop(run_a_frame)
