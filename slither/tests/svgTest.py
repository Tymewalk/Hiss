import slither

cat = slither.Sprite()
cat.addCostume("assets/cat.svg", "cat")
cat.costumeNumber = 1

cat.goto(400, 200)

slither.slitherStage.bgColor = (40, 222, 40)

slither.setup() # Begin slither

def run_a_frame():
    cat.direction += 5
    cat.moveSteps(10)

slither.runMainLoop(run_a_frame)
