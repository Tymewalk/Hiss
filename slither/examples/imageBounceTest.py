import slither

def create_circle():
    circle = slither.Sprite()
    circle.addCostume("circle.png", "circle")
    circle.costumeName = "circle"
    circle.goto(0,0)
    return circle
circle1, circle2, circle3 = create_circle(), create_circle(), create_circle()
circle4 = create_circle()
circle4.goto(400,300)
slither.slitherStage.bgcolor = (255, 255, 255)

def run_a_frame():
    circle1.xpos += 0.5
    circle1.ypos += 0.5
    circle1.direction += 1

    circle2.xpos += 0.5
    circle2.direction += 1

    circle3.ypos += 0.5
    circle3.direction += 1

    circle4.direction += 1

slither.setup()
slither.runMainLoop(run_a_frame)
