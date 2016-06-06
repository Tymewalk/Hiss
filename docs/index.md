![Slither's logo](https://cloud.githubusercontent.com/assets/13385064/14028163/82c374ea-f1d1-11e5-84b7-8ebc442b2d70.png)

[![Codacy Badge](https://api.codacy.com/project/badge/grade/6c21312189334c1782a49e152d0f4b78)](https://www.codacy.com/app/stanleybookowl/Slither)

# What is Slither?
Slither is a Python module that uses PyGame to bring Scratch-like features to Python.
[Scratch](scratch.mit.edu) is a programming language developed by MIT that uses block-based scripts to introduce kids to programming.

# Why use Slither?
Those just getting started with Python after using Scratch may want to go straight from one GUI to another. Slither allows those people to quickly make simple projects in a matter of minutes, while also learning Python.

# How do I install Slither?
## Through pip
Run `pip install slither`.

## Manually
Run `python setup.py build` and then `python setup.py install`.<br />
If that doesn't work, run `python setup.py bdist_wheel`, and then run `pip install path`, where path is the final path of the .whl file (which should be in dist/). If this fails, install wheel with `pip install wheel` then retry.<br />
If it still fails, make sure you have `setuptools` fully updated and properly installed.<br />
Remember to add `import slither` in your script.<br />

Slither supports both Python 2 and Python 3. Also, note that you must have PyGame installed in order to use Slither.


# Uh-oh! There's a problem!
First, check to make sure you've properly installed all of Slither's requirements and Slither.<br />
Next, check your Python program over. Do you have correct syntax and spelling?<br />
Finally, check to see if you have the newest version of Slither.

If you've done all three of those things and it still doesn't work, file an issue.

# How can I help with Slither?
Check the issues to see what problems need fixing. Then make a pull request detailing what you've changed and how it should help. After testing, someone will merge it into the main project.<br />
If you help enough times, Tymewalk will add you as a collaborator.<br />
**WARNING: Abuse of collaborator permissions WILL result in you being removed as a collaborator.**<br />
So just be careful with what you do and you'll be fine.

# Credits
Scratch is property of The Lifelong Kindergarten Group. The Slither devs are not affiliated with the LLK, nor do they own Scratch.
