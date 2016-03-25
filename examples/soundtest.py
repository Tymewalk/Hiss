import slither, pygame, time
from time import sleep

slither.slitherStage.setColor(40, 222, 40)
slither.setup() # Begin slither
sound = slither.slitherSound.loadSound('boom.wav')

def run_a_frame():
    sound.play()
slither.runMainLoop(run_a_frame)
