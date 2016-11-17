import slither, random # Get functions from slither and random

doge = [None]* 30 # Initialize array 'doge'
dogecount = 1 # Initialize iterator 'dogecount'

while dogecount != 30: # Produce 30 doges
    doge[dogecount] = slither.Sprite() # Make each doge a sprite
    doge[dogecount].addCostume('doge.png', 'doge') # Give them the costume 'doge'
    doge[dogecount].costumeName = 'doge' # Set the doges costume to 'doge'
    doge[dogecount].ypos = random.randint(0, 400) # Make the doges go to a random y position
    doge[dogecount].xpos = random.randint(0, 400) # Make the doges go to a random x position
    dogecount += 1 # Increase the iterator for reiteration

slither.setup('Doge invasion!', 400, 400) # Setup slither, set caption to 'Doge invasion!' and set resolution to 400px by 400px

def loop(): # Define main game loop called 'loop'
    pass # Do nothing...

slither.runMainLoop(loop) # Run main game loop
