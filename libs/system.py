lib_name = "sys"
lib_functions = [
    "CMD","INPUT"
]

for lib_func in lib_functions:
    funcs.append(f"{lib_name.upper()}.{lib_func}")

#FUNCS

import sys

if name == "SYS.INPUT":
    if PRM != []:
        variables["return"] = input(PRM[0])
    else:
        pass

if name == "SYS.CMD":
    if PRM != []:
       os.system(PRM[0])
    else:
        pass