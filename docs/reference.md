# Reference

## function `keysDown()`
Returns a list of the currently held down keys

## class `Mouse`
A class for getting and setting mouse properties
This is a static class, all methods should be called directly through the class

### function `Mouse.buttonsPressed()`
Returns a three-tuple of bools that give the state of the left, middle, and right buttons

### function `Mouse.isFocused()`
Returns `True` if the mouse is focused on the slither window

### function `Mouse.isVisible()`
Returns `True` if the mouse is visable

### function `Mouse.leftPressed()`
Returns `True` if the left mouse button is pressed

### function `Mouse.middlePressed()`
Returns `True` if the middle mouse button is pressed

### function `Mouse.pos()`
Returns the position of the mouse as an `(x, y)` tuple

### function `Mouse.relativeMovement()`
Returns the reletive movement of the mouse since the last call to this function as a `(x, y)` tuple

### function `Mouse.rightPressed()`
Returns `True` if the right mouse button is pressed

### function `Mouse.setPos(x, y)`
Sets the position of the mouse pointer to `(x, y)`

### function `Mouse.setVisible(visable)`
Sets the visibility of the mouse

### function `Mouse.setXPos(x)`
Sets the x position of the mouse

### function `Mouse.setYPos()y`
Sets the y position of the mouse

### function `Mouse.xPos()`
Gets the x position of the mouse

### function `Mouse.yPos()`
Gets the x position of the mouse


## class `Stage`
The stage class is the base class of all the sprites. It has one concrete instance, `slitherStage`

### data `costumes`
A `collections.OrderedDict` of costumes

### data `bgColor`
A `(red, green, blue)` tuple used as the background color of the stage

### function `addCostume(costumePath, costumeName)`
Loads a costume from the path `costumePath` and gives it the name `costumeName`

### function `deleteCostumeByName(name)`
Deletes the costume with the name `name`

### function `deleteCostumeByNumber(n)`
Deletes the costume numbered `n`

### property `costumeNumber`
The costume number of the current costume. Assigning `n` to this switches to costume `n % len(self.costumes)`
### property `costumeName`
The name of the current costume. Assigning to this switches to the costume with that name

## slitherStage
An instance of Stage. Manipulate this to change the stage used in slither programs


