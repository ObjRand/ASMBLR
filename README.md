# ASMBLR
[![ASMBLR LOGO](/website/ASMBLR.png)](https://objrand.github.io/ASMBLR/)

ASMBLR is a interpreted programming language (EXTRA SLOW). Idk... Made it for fun!  

Designed for windows, but if you know how to use python, you can maybe use it on linux or unix (mac os)  
If you see any bugs, please report them on the "Issues" tab in github.  

## How to use!
Go to the Releases, get the zip of what version you want and run the setup.bat file with admin permissions. Afterwards, put "C:\ASMBLR" in windows PATH.  
That's it!  
You can go to CMD and type "ASMBLR open <file>.asmblr" or you can use the shell version by typing "ASMBLR shell".

## How to compile (windows only):
Compiling is not recomended as it only gives the language binary file, not including the standard libaries.  
This requires Python 3.x (that can be accessed in PATH)  
These steps shows an explanation of the command and the commands themselves.

In ASMBLR root folder, run these commands:  
```
cd ..
cd builder  
cd Scripts
activate
cd ..
cd ..
cd src 
python -m PyInstaller --onefile main.py  
cd dist  
rename "main.exe" "ASMBLR.exe"
mkdir C:\ASMBLR  
mkdir C:\libs  
move ASMBLR.exe C:\ASMBLR
```

Then add "C:\ASMBLR" to your windows PATH environment variable!  

### How to get standard libraries for self-compiled build
Download "std_libs.zip" from the website, go to "C:/ASMBLR/libs" and extract all from zip.


## 1.1 Plans:
This update is quite important for me, as I have *FINALLY* come back to coding (*at least somewhat*), 
and I'm having fun fixing and improving ASMBLR.

Well, here are the plans for *1.1*:
- [X] FIXING "*GOTO*" and "*END*".
- [ ] DATA TYPE CONVERSION WILL FINALLY BE ADDED FULLY.
- [ ] ***BETTER*** LIBRARY SUPPORT.
- [ ] NEW *ADDITIONS* TO THE WEBSITE!
- [ ] MORE *AUTOMATIC* INSTALLER!
- [ ] EASIER COMPILING
- [ ] *IMPROVED* INSTRUCTIONS AND WIKI

### Branching System (***For 1.x***)
(NOT INCLUDING 1.0) 
*1.x* will probably be the ASMBLR Standard Versions with LTS.
*1.x_Beta* are Beta Branches, not for main release yet.
*1.x_EX* are **EXPERIMENTAL** Branches, but they can be pull requested into a *BETA* **or** *MAIN*

### To do?
- [ ] ***PROPER*** Error Handling (Tough one...)
- [ ] Optimise Code (Make it faster and lighter)
