# usr/bin/env python3
# svgTest.py - Test Slither's SVG support

import slither

if slither.svgSupport:
    print("We have SVG support!")
else:
    print("No SVGs today :(")

svg = slither.Sprite()
svg.addCostume("assets/svg Logo.svg", "svg")
svg.costumeNumber = 1
svg.scale = 1
svg.showBoundingBox = False
svg.goto(100, 300)

svg2 = slither.Sprite()
svg2.addCostume("assets/svg Logo.svg", "svg")
svg2.costumeNumber = 1
svg2.scale = 5
svg2.showBoundingBox = False
svg2.goto(500, 300)

slither.setup() # Begin slither

def run_a_frame():
    pass

slither.runMainLoop(run_a_frame)
