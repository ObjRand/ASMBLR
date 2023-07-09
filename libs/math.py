lib_name = "math"
lib_functions = [
    "ROOT","SIN","COS"
]

for lib_func in lib_functions:
    funcs.append(f"{lib_name.upper()}.{lib_func}")

#FUNCS

# FIX GLITCH ???
#print(f"{lib_name.upper()}.{lib_functions[0]}")

import math

if name == "MATH.ROOT":
    if len(PRM) > 1:
        variables["return"] = math.pow(PRM[0], (1/PRM[1]))
    else:
        pass

if name == "MATH.SIN":
    print("test! sin")

if name == "MATH.COS":
    print("test! cos")