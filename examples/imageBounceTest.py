import slither, os
circle = slither.Sprite()
circle.addCostume(os.path.join(os.path.dirname(__file__), "circle.png"), "circle")
circle.setCostumeByName("circle")
circle.goTo(0,0)
slither.slitherStage.setColor(255, 255, 255)

def run_a_frame():
    circle.changeXBy(1)
    circle.changeYBy(1)
    circle.changeDirectionBy(1)

slither.setup()
slither.runMainLoop(run_a_frame)
