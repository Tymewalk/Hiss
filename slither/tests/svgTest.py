import slither

cat = slither.Sprite()
cat.addCostume("assets/cat.svg", "cat")
cat.costumeNumber = 1
cat.scale = 1.5

cat.goto(175, 300)

cat2 = slither.Sprite()
cat2.addCostume("assets/cat.svg", "cat")
cat2.costumeNumber = 1
cat2.scale = 5

cat2.goto(500, 300)


slither.setup() # Begin slither

def run_a_frame():
    cat.direction += 2


slither.runMainLoop(run_a_frame)
