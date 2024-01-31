lib_name = "sys"
lib_functions = [
    "CMD","INPUT"
]

for lib_func in lib_functions:
    funcs.append(f"{lib_name.upper()}.{lib_func}")

#FUNCS

import sys

if name == lib_name.upper() + ".INPUT":
    if PRM != []:
        variables["return"] = input(PRM[0])
    else:
        variables["return"] = input()

if name == lib_name.upper() + ".CMD":
    if PRM != []:
       os.system(PRM[0])
    else:
        pass