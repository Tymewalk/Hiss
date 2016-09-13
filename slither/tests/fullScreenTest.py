#! usr/bin/env python3
# fullScreenTest.py

import slither, pygame

snakey = slither.Sprite()
snakey.costumeName = "costume0" # You can set the default costume (costume0) by name...
snakey.goto(400, 300)

slither.slitherStage.bgColor = (40, 222, 40)

slither.setup() # Begin slither

def run_a_frame():
    snakey.direction += 1

@slither.registerCallback(pygame.MOUSEBUTTONUP)
def handle_mousedown(event):
    slither.toggleFullScreen()

slither.runMainLoop(run_a_frame)
