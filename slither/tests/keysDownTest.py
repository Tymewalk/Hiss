# usr/bin/env python3
# keysDownTest.py - Test slither.keysDown()

from slither import *

def run_a_frame():
    print(slither.keysDown())

slither.setup()
slither.runMainLoop(run_a_frame)
