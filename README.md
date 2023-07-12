# ASMBLR
ASMBLR is a interpreted programming language (EXTRA SLOW). Idk... Made it for fun!

If you see any bugs, please report them on the "Issues" tab in github.

Compiled installer coming soon! (Around 13-16 July 2023)

## How to use!
Go to the Releases, and run the installer of what version you want. That's it!
You can go to CMD and type "ASMBLR open <file>.asmblr" or you can use the shell version by typing "ASMBLR shell".

## How to compile (windows only):
Compiling is not recomended as it only gives the language binary file, not including the standard libaries.This requires Python 3.x (that can be accessed in PATH)

These steps shows an explanation of the command and the commands themselves.

In ASMBLR root folder, run a command to build a python VENV called builder:
"python -m venv builder"

Enter the venv scripts folder and activate VENV:
"cd builder && cd Scripts && activate"


Install pyinstaller on the VENV:
"pip install pyinstaller"


In the venv activated cmd, enter src: "cd .. & cd .. & cd src"


Now, compile the files:
"python -m PyInstaller --onefile main.py"


When its done, go to dist folder. 
You will see a file called "main.exe", rename it to "ASMBLR". 
Make a folder in "C:/" called "ASMBLR", then in "C:/ASMBLR", make a folder named libs. 
Copy the exe to "C:/ASMBLR" and That's it!

### How to get standard libraries for self-compiled build
Download "std_libs.zip" from the website, go to "C:/ASMBLR/libs" and extract all from zip.
