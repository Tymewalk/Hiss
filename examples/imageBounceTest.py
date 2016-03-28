import slither

circle = slither.Sprite()
circle.addCostume("circle.png", "circle")
circle.setCostumeByName("circle")
circle.goto(0,0)

slither.slitherStage.setColor(255, 255, 255)

def run_a_frame():
    circle.xpos += 1
    circle.ypos += 1
    circle.direction += 1

slither.setup()
slither.runMainLoop(run_a_frame)
