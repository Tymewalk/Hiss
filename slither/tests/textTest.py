import slither

slither.slitherStage.bgColor = (40, 222, 40)

slither.blitText("Hello, world!")

slither.setup() # Begin slither

def run_a_frame():
    pass

slither.runMainLoop(run_a_frame)
