# moveStepsTest.py
import slither

sprite = slither.Sprite()
sprite.addCostume("assets/arrow.png", "arrow")
sprite.costumeName = "arrow"
sprite.goto(slither.WIDTH // 2, 75)

def run_a_frame():
    sprite.direction += 5
    sprite.moveSteps(20)

slither.setup()
slither.setFPS(30) # Slow slither down
slither.runMainLoop(run_a_frame)