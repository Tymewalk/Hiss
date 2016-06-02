# isTouchingTest.py
import slither

toucher = slither.Sprite()
toucher.addCostume("assets/arrow.png", "arrow")
toucher.costumeName = "arrow"
toucher.goto(0, 100)

snakey = slither.Sprite()
snakey.goto(slither.WIDTH // 2, 100)

def run_a_frame():
    toucher.moveSteps(3)
    if toucher.isTouching(snakey):
        print("Touching!")
    else:
        print("Not touching.")

slither.setup()
slither.runMainLoop(run_a_frame)
