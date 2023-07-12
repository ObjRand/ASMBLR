# ASMBLR
ASMBLR is a interpreted programming language (EXTRA SLOW). Idk... Made it for fun!

## How to use!
Go to the Releases, and run the installer of what version you want. That's it!
You can go to CMD and type "ASMBLR open <file>.asmblr" or you can use the shell version by typing "ASMBLR shell"

## How to compile (windows only):
Compiling is not recomended as it only gives the language binary file, not including the standard libaries.This requires Python 3.x (that can be accessed in PATH)

These steps shows an explanation of the command and the commands themselves.

In ASMBLR root folder, run a command to build a python VENV called builder
python -m venv builder


enter the venv scripts folder and activate VENV
cd builder && cd Scripts && activate


install pyinstaller on the VENV
pip install pyinstaller


in the venv activated cmd, enter src
cd .. & cd .. & cd src


compile files
python -m PyInstaller --onefile main.py


when its done, go to dist folder.

you will see a file called "main.exe", rename it to "ASMBLR"

make a folder in "C:/" called "ASMBLR"

copy the exe to "C:/ASMBLR"

in "C:/ASMBLR", make a folder named libs

### How to get standard libraries for self-compiled build
download "std_libs.zip" from the website, go to "C:/ASMBLR/libs" and extract all from zip
