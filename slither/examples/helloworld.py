import slither # Get slither functions

snakey = slither.Sprite() # Make a sprite called snakey
snakey.costumeName = "costume0" # Set snakey's costume to costume0

snakey.goto(200, 200) # Make snakey go to x 200 and y 200

slither.setup('Hello World!', 400, 400) # Setup slither with caption 'Hello World!' and resolution 400px by 400px

def run_a_frame(): # Define main game loop
    pass # Do nothing. This is only a simple project

slither.runMainLoop(run_a_frame) # Start main game loop
