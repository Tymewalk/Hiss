# Slither
A Python module for bridging Scratch and Python.

## What is Slither?
Slither is a Python module that uses PyGame to bring Scratch-like features to Python.
[Scratch](scratch.mit.edu) is a programming language developed by MIT that uses block-based scripts to introduce kids to programming.

## How do I run Slither?
To install, run `python setup.py bdist_wheel`, and then run `pip install path`, where path is the final path of the .whl file (which should be in dist/). If this fails, install wheel with `pip install wheel` then retry.<br />
If it still fails, make sure you have `setuptools` fully updated and properly installed.<br />
Remember to add `import slither` in your script.<br />
Note that you must have PyGame installed in order to use Slither.

## Why use Slither?
Those just getting started with Python after using Scratch may want to go straight from one GUI to another. Slither allows those people to quickly make simple projects in a matter of minutes, while also learning Python.

## How can I help with Slither?
Check the issues to see what problems need fixing. Then make a pull request detailing what you've changed and how it should help. After testing, someone will merge it into the main project.<br />
If you help enough times, @Tymewalk will add you as a collaborator.<br />
**WARNING: Abuse of collaborator permissions WILL result in you being removed as a collaborator.**<br />
So just be careful with what you do and you'll be fine.<br />

## I'm making a change! What should I do?
### As a pull request
Nothing. I'll look it over and fix what needs to be fixed.

### As a collaborator
If it's a small change, go ahead and commit it to master.
Examples of small changes include "Fix spelling error", "Properly indent code", etc.

If it's a big change, make a new branch and then a pull request for it.
Examples of big changes include adding new functions, re-writing a lot of code, etc.

## Uh-oh! There's a problem!
First, check to make sure you've properly installed all of Slither's requirements and Slither.<br />
Next, check your Python program over. Do you have correct syntax and spelling?<br />
Finally, check to see if you have the newest version of Slither.

If you've done all three of those things and it still doesn't work, file an issue.

## Credits
Scratch is property of The Lifelong Kindergarten Group. I am not affiliated with the LLK, nor do I own Scratch.
