#! usr/bin/env python3
# textTest.py
import slither

slither.slitherStage.bgColor = (40, 222, 40)

slither.setup() # Begin slither

slither.blitText("Hello, world!")

def run_a_frame():
    slither.blitText("Hello, world!", size=40)

slither.runMainLoop(run_a_frame)
