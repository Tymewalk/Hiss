# mover.py
import pygame # We need pygame for the event constants and the key functions
import slither
from pygame.locals import *

sprite = slither.Sprite()
sprite.goto(slither.WIDTH // 2, slither.HEIGHT // 2) # Goto the middle of the screen
sprite.addCostume("../tests/assets/arrow.png", "arrow") # Load the arrow costume
sprite.costumeName = "arrow" # Set the costume.

# This dict holds the data for how fast the arrow moves and what direction it is pointing
controls = {"turn":0, "speed":0}

@slither.registerCallback(pygame.MOUSEBUTTONDOWN)
def handle_mousedown(event): # When the mouse button is pressed...
    print(controls) # ...print out the controls dict

def run_a_frame():
    keys = pygame.key.get_pressed()
    # Because this example relies on having keys pressed down,
    # we can't use the event handlers, and have to check the key states ourself
    if keys[K_LEFT]:
        controls["turn"] -= 4
    elif keys[K_RIGHT]:
        controls["turn"] += 4
    if keys[K_SPACE]:
        controls["speed"] = min(controls["speed"] + 2, 10)
    else:
        controls["speed"] = max(controls["speed"] - 0.2, 0)
    # Set the sprites direction...
    sprite.direction = controls["turn"]
    # ... and move it speed steps 
    sprite.moveSteps(controls["speed"])
    # Add wraparound checks.
    if sprite.xpos > slither.WIDTH:
        sprite.xpos = 0
    elif sprite.xpos < 0:
        sprite.xpos = slither.WIDTH
    if sprite.ypos > slither.HEIGHT:
        sprite.ypos = 0
    elif sprite.ypos < 0:
        sprite.ypos = slither.HEIGHT

# Print instructions
print("Use the left and right arrows to turn.\nUse the space key to go forward")
# Setup slither...
slither.setup("Move!")
# and start it running!
slither.runMainLoop(run_a_frame)


