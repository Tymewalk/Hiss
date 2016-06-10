import slither

snakey = slither.Sprite()
snakey.costumeName = "costume0"

snakey.goto(0, 0)

slither.setup() # Begin slither

def handlequit():
    print("Quitting...")
    return True
slither.registerCallback(pygame.QUIT, handlequit) # This uses the direct call form

@slither.registerCallback(pygame.MOUSEBUTTONUP) # This uses the decorator form
def handlemouseup(event):
    print("Mouseup:", event.pos, event.button)

def run_a_frame():
    snakey.xpos += 1
    snakey.ypos += 1
    snakey.direction += 1

slither.runMainLoop(run_a_frame)
