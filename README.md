# ASMBLR
ASMBLR is a interpreted programming language (EXTRA SLOW). Idk... Made it for fun!  

Designed for windows, but if you know how to use python, you can maybe use it on linux or unix (mac os)  
If you see any bugs, please report them on the "Issues" tab in github.  
Compiled installer coming soon! (Around 13-16 July 2023)  

## How to use!
Go to the Releases, and run the installer of what version you want. That's it!
You can go to CMD and type "ASMBLR open <file>.asmblr" or you can use the shell version by typing "ASMBLR shell".

## How to compile (windows only):
Compiling is not recomended as it only gives the language binary file, not including the standard libaries.  
This requires Python 3.x (that can be accessed in PATH)  
These steps shows an explanation of the command and the commands themselves.

In ASMBLR root folder, run these commands:  
`cd ..`  
`cd builder`  
`cd Scripts`  
`activate`  
`cd ..`  
`cd ..`  
`cd src`  
`python -m PyInstaller --onefile main.py`  
`cd dist`  
`rename "main.exe" "ASMBLR.exe"`  
`mkdir C:\ASMBLR`  
`mkdir C:\libs`  
`move ASMBLR.exe C:\ASMBLR`  

Then add "C:\ASMBLR" to your windows PATH environment variable!  

### How to get standard libraries for self-compiled build
Download "std_libs.zip" from the website, go to "C:/ASMBLR/libs" and extract all from zip.
