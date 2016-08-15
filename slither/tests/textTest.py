import slither

slither.slitherStage.bgColor = (40, 222, 40)

slither.setup() # Begin slither

slither.blitText("Hello, world!")

def run_a_frame():
    pass

slither.runMainLoop(run_a_frame)
