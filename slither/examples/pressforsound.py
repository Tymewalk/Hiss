import slither, time # Get slither and time functions

slither.setup('Press S for sound', 400, 400) # Setup slither with the caption 'Press S for sound' and resolution 400px by 400px

def loop(): # Define main loop
    try: # Error handling wrapper
        if slither.keysDown()[0] == 's': # Run if key s is pressed...
            sound = slither.slitherSound.loadSound('./assets/boom.wav') # Load the sound 'boom.wav'
            sound.play() # Play the sound
            time.sleep(2) # Wait 2 seconds
    except: # Run code if there's an error
        pass # Do nothing

slither.runMainLoop(loop) # Run main loop
