import slither

i = 0

def run_a_frame():
    global i
    slither.setCaption("-"*(i+1))
    i = (i + 1) % 60

slither.setup("")

slither.runMainLoop(run_a_frame)
