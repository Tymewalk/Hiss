#! usr/bin/env python3
# soundtest.py
# Sound works, make sure your volume is up.
import slither
import time

sound = slither.slitherSound.loadSound('assets/boom.wav')
sound.play()
time.sleep(2)
