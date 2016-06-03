# usr/bin/env python3
# mouseTest.py

from slither import *
from slither import Mouse

def run_a_frame():
    print(Mouse.buttonsPressed())
    print(Mouse.pos())
    print(Mouse.isFocused())
    print()

slither.setup()
slither.runMainLoop(run_a_frame)
