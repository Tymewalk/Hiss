![Slither's logo](https://cloud.githubusercontent.com/assets/13385064/14028163/82c374ea-f1d1-11e5-84b7-8ebc442b2d70.png)

[![Codacy Badge](https://api.codacy.com/project/badge/grade/6c21312189334c1782a49e152d0f4b78)](https://www.codacy.com/app/stanleybookowl/Slither)

## What is Slither?
Slither is a Python module that uses PyGame to bring Scratch-like features to Python.
[Scratch](scratch.mit.edu) is a programming language developed by MIT that uses block-based scripts to introduce kids to programming.

## How do I run Slither?
### Through `pip`
Run `pip install slither`.

### Manually
Run `python setup.py build` and then `python setup.py install`.<br />
If that doesn't work, run `python setup.py bdist_wheel`, and then run `pip install path`, where path is the final path of the .whl file (which should be in dist/). If this fails, install wheel with `pip install wheel` then retry.<br />
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

# Contributors
A list of all contributors who have helped or are helping.

### @Tymewalk
Started Slither, added several groundwork features.

### @BookOwl
Helped majorly rewrite Slither so it's easier to code in. Additionally helped suggest and add changes that helped Slither get many important features.

### @Omegabyte
Began and currently works on documentation, also added sound support.

### @IronManMark20
Is working on adding SVG support to slither.

### @Icelys
Helped with a small costume changing fix.

# Code of Conduct
Rules to follow when contributing. Follow these and you should be fine.

- Never push directly to master. Always make branches and pull requests. This is to make sure Slither stays as bug-free as possible.
  - Additionally, wait to merge until you're sure your code is bug-free and/or someone has reviewed it.
  - The only exception is minor changes or important bugfixes that can't wait for someone to review it.
- Always ask for feedback before merging a pull request.
- Only @Tymewalk should merge pull requests that add features or change large portions of Slither.
- Make a new issue if you want to propose a new release. Don't make releases without getting approval from other contributors.
- Most importantly, have fun!


# Credits
Scratch is property of The Lifelong Kindergarten Group. The Slither devs are not affiliated with the LLK, nor do they own Scratch.
