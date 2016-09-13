# Installing ImageMagick
In order for Slither to have support for SVG files, you need to have ImageMagick installed. Here are some installation instructions for common platforms.

## On Windows
Download and install the correct binary from http://www.imagemagick.org/script/binary-releases.php#windows

## On OSX/MacOS
If you have homebrew installed, the easiest way is to run `brew install imagemagick` in your terminal.

If you have MacPorts installed, you can run `sudo port install ImageMagick` to install ImageMagick.

Otherwise, follow the instructions at http://www.imagemagick.org/script/binary-releases.php#macosx

## On GNU/Linux

### Debian
Run `sudo aptitude update &&  aptitude install imagemagick`

### Ubuntu
Run `sudo apt-get install imagemagick`

### Other systems
Use your package manager to install ImageMagick if it has it, otherwise try http://www.imagemagick.org/script/binary-releases.php#unix
