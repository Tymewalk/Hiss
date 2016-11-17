import slither # Get slither functions

background = slither.slitherStage # Make 'background' the stage
background.addCostume('grass.png', 'grass') # Add costume 'grass' to background
background.costumeName = 'grass' # Set the costume to grass

snakey = slither.Sprite() # Make a sprite named snakey (default)
snakey.goto(700, 200) # Make snakey go to xpos 700 and ypos 200

slither.setup('Run Snakey!', 800, 400) # Setup slither, set the caption to 'Run Snakey!' and set the resolution to 800px by 400px

def myloop(): # Make a main loop named 'myloop'
    slither.blitText('Run snakey, Run!', 300, 20, 32) # Add the text 'Run snakey, Run!' to the screen on xpos 300, ypos 20 with font size 32
    snakey.xpos -= 10 # Make snakey run forward
    if snakey.xpos == 100: # Trigger code if snakey is about to exit screen
        snakey.goto(700, 200) # Make snakey restart
   
slither.runMainLoop(myloop) # Run the main game loop
