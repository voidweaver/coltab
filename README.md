# coltab
A simple python script to display samples of 8-bit colors available in most terminals.

# About
This is just a script I wrote for my own use, but I figured I should put it here as well.

# Installation
1. Download the python file or clone this repository

2. Put the script file in `/usr/local/bin` or anywhere in your `$PATH`

3. Make sure [Python 3](https://www.python.org/) is installed with pip3
   ```
   $ python3 --version
   Python 3.x.x
   $ pip3 --version
   pip x.x.x from /path/to/dir (python 3.x)
   ```
4. If you've cloned this repository, you can run
   ```
   $ pip3 install requirements.txt
   ```
   or if you haven't, then run
   ```
   $ pip3 install click==7.1.2
   ```

5. Make sure the script has the permission to be executed by running
   ```
   $ chmod a+x coltab
   ```
   
6. Now you're all set! Try running `$ coltab`, it should run without any problem.

**Note:** I haven't tried running this script on Windows yet. It may or may not work, but if you happen to test it, please let me know.
