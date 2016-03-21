import slither, pygame

snakey = slither.Sprite()
snakey.setCostumeByName("costume0")

snakey.goTo(0, 0)

slither.slitherStage.setColor(40, 222, 40)

slither.setup() # Begin slither

def handlequit():
    print("Quiting...")
    return True
slither.registerCallback(pygame.QUIT, handlequit) # This uses the direct call form

@slither.registerCallback(pygame.MOUSEBUTTONUP) # This uses the decorator form
def handlemouseup(event):
    print("Mouseup:", event.pos, event.button)

def run_a_frame():
    snakey.changeXBy(1)
    snakey.changeYBy(1)
    snakey.changeDirectionBy(1)

slither.runMainLoop(run_a_frame)
