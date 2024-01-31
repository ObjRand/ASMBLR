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
        if "-" in str(PRM[0]):
            PRM[0] = int(str(PRM[0]).replace("-",""))
            variables["return"] = -math.pow(PRM[0], (1/PRM[1]))
        else:
            variables["return"] = math.pow(PRM[0], (1/PRM[1]))
    else:
        pass

if name == "MATH.SIN":
    print("test! sin")

if name == "MATH.COS":
    print("test! cos")