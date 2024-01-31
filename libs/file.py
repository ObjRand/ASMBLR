lib_name = "file"
lib_functions = [
    "OPEN","READ","WRITE", "CLOSE"
]

for lib_func in lib_functions:
    funcs.append(f"{lib_name.upper()}.{lib_func}")

#FUNCS

# FIX GLITCH ???
#print(f"{lib_name.upper()}.{lib_functions[0]}")

if name == "FILE.OPEN":
    if len(PRM) > 1:
        pass
    else:
        pass

if name == "FILE.READ":
    if len(PRM) > 1:
        pass
    else:
        pass

if name == "FILE.WRITE":
    if len(PRM) > 1:
        pass
    else:
        pass

if name == "FILE.CLOSE":
    if len(PRM) > 1:
        pass
    else:
        pass