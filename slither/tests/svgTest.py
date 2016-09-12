import slither
import cairosvg
print(cairosvg.__version__)

cat = slither.Sprite()
cat.addCostume("assets/gear.svg", "cat", 1)
cat.costumeNumber = 1

cat.goto(300, 310)

cat2 = slither.Sprite()
cat2.addCostume("assets/cogwheel.svg", "cat", 2)
cat2.costumeNumber = 1

cat2.goto(500, 300)


slither.setup() # Begin slither

def run_a_frame():
    cat.direction -= 1
    cat2.direction += 1


slither.runMainLoop(run_a_frame)
