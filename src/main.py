import os,re,sys,time,pathlib
import string as str_lib

conditions = [
    "==", ">", "<", ">=", "<=", "!="
]

built_in = ["IMPORT","IMPORT_LOCAL","RTRN","GOTO","END"]
built_in_funcs = [
    "PRINT",
    #"CMD",
    "VARS","SLEEP",
    "IF","EXIT",
    "APND","GET_IDX","SET_IDX","POP",
    "TS","TI","TF"
]
funcs = []

build_in_math={
    "ADD":"+=",
    "SUB":"-=",
    "MUL":"*=",
    "DIV":"/=",
    "FDIV":"//=",
    "POW":"**=",
    "MOD":"%="
}

labels = {}
in_label = False
in_goto = False
goto_line = 0
STOP_END = False

# Program Variables
env_variables = {"version":"Ver1.1-Beta","file_path":os.getcwd(),"lang_path":"C:/ASMBLR"}

variables = {
    "return":None
}

illegal_variables = ["true","false"]

current_line = -1
file_lines = 0

to_shell = False

lib_name = ""
lib_section = []
lib_functions = ""

def shell():
    parse_line(input("ASMBLR ->"),True)

    shell()

def error(text):
    print(f"ERROR at line {current_line + 1}: {text}\nNOW, GO FIX IT!!!")

    if to_shell: shell()
    else: exit()

def load_lib(lib,local = False):
    global lib_name, lib_section, lib_functions, funcs

    lib_file = []
    func_section = False

    temp1 = []
    temp2 = []

    if local:
        path = env_variables["file_path"]
    else:
        path = env_variables["lang_path"]
    
    with open(path + f"/libs/{clean_value(lib)}.py","r") as f:
        #for line in f.read():
        #    lib_file.append(line.strip())

        lib_file = f.read()

        if "#FUNCS" in lib_file:
            for line in lib_file.split("\n"):
                if "#FUNCS" in line:
                    func_section = True

                if func_section:
                    temp2.append(line)
                else:
                    temp1.append(line)

            lib_section = "\n".join(temp1)
            lib_functions += "\n".join(temp2)

            exec(lib_section)
        else:
            error(f"Lib called \"{lib}\" doesn't have a \"#FUNCS\" section, making it broken!")

def is_number(s):
    return bool(re.match(r'^-?\d+(?:\.\d+)?$', s))

def clean_value(value):
    value = value.strip()
    
    if "\"" in value:
        if value.startswith("\"") and value.endswith("\""):
            value = value.replace("\\\"","\"")[1:-1]
        else:
            error("Missing double quote at start or end of string!")
    else:
        if value in variables:
            return variables[value]
        else:
            if value.startswith("[") and value.endswith("]"):
                value = value[1:-1]

                value_list = value.split(",")
                temp_list = []
                for item in value_list:
                    temp_list.append(clean_value(item))
                
                value = temp_list
            
            # Int or Float
            elif value.isdecimal():
                value = int(value)
            elif not re.match(r'^-?\d+(?:\.\d+)$', value) is None:
                value = float(value)

            # Check if bool (T/F)
            elif value.lower() == "true":
                value = bool(1)
            elif value.lower() == "false":
                value = bool(0)

            # Well, check if var name has illegal symbols!
            else:
                for symbol in str_lib.punctuation:
                    if symbol in value:
                        error(f"Can't have illegal symbols in variable name!")
                
                error(f"No Variable named {value}!")

    return value

def assign_var(line):
    line_array = line.replace(" ","").split("=",1)

    if line_array[0].lower() in illegal_variables:
        error(f"Can't name variable {line_array[0]}!")

    var_value = clean_value(line_array[1])
    variables[line_array[0]] = var_value

def print_func(PRM):
    if PRM == []:
        print()
        return
    
    if len(PRM) == 1:
        print(str(PRM[0])
            .replace('\\n', '\n')
            .replace('\\t', '\t')
            .replace('\\v', '\v')
            .replace('\\a', '\a'),
        end="")
        
        return
    else:
        # Turn all elements of list to str for printing
        for i,prm in enumerate(PRM):
            PRM[i] = str(prm)

        print(
            "".join(PRM[0:len(PRM)])
            .replace('\\n', '\n')
            .replace('\\t', '\t')
            .replace('\\v', '\v')
            .replace('\\a', '\a'),
        end="")

def arthimetic(exp,name,PRM):
    try:
        total = PRM[0]
        PRM.pop(0)

        for prm in PRM:
            values = {"total":total,"prm":prm}
            exec(f"total {exp} prm", values)

        variables["return"] = values["total"]
    except:
        error(f"Can't use Nonetype as PRM for {name}")

def command(name,PRM):
    # Small bugs!
    exec(lib_functions)

    if name == "PRINT":
        print_func(PRM)
        return

    if name == "VARS":
        print(variables)
        return

    for item in list(build_in_math.keys()):
        if name == item:
            arthimetic(build_in_math[name],name,PRM)
            return

    if name == "SLEEP":
        if PRM != []:
            time.sleep(PRM[0])
        return

    if name == "IF":
        if len(PRM) > 4:
            if PRM[1] in conditions:
                values = {"val1":PRM[0],"val2":PRM[2],"result":False}
                exec(f"result = (val1 {PRM[1]} val2)",values)
                
                #print(values["result"])

                if values["result"]:
                    parse_line(PRM[3])
                else:
                    parse_line(PRM[4])
            else:
                # HANDLE ERRORS
                pass
        else:
            # HANDLE ERRORS
            pass

        return

    if name == "APND":
        if len(PRM) > 1:
            if type(PRM[0]) == list:
                PRM[0].append(PRM[1])

                variables["return"] = PRM[0]
        else:
            # HANDLE ERRORS
            pass

        return
    
    if name == "GET_IDX":
        if len(PRM) > 1:
            if type(PRM[0]) == list:
                try:
                    variables["return"] = PRM[0][PRM[1]]
                except IndexError:
                    error(f"List index out of range! ({len(PRM[0])-1} < INDEX:{PRM[1]})")
        else:
            # HANDLE ERRORS
            pass

        return

    if name == "SET_IDX":
        if len(PRM) > 2:
            if type(PRM[0]) == list:
                try:
                    PRM[0][PRM[1]] = PRM[2]

                    variables["return"] = PRM[0]
                except IndexError:
                    error(f"List index out of range! ({len(PRM[0])-1} < INDEX:{PRM[1]})")
        else:
            # HANDLE ERRORS
            pass

        return

    if name == "POP":
        if len(PRM) > 1:
            if type(PRM[0]) == list:
                try:
                    PRM[0].pop(PRM[1])
                    variables["return"] = PRM[0]
                except IndexError:
                    error(f"List index out of range! ({len(PRM[0])-1} < INDEX:{PRM[1]})")
        else:
            # HANDLE ERRORS
            pass

        return

    if name == "TS":
        if PRM != []:
            variables["return"] = str(PRM[0])

        return

    if name == "TI":
        if PRM != []:
            if is_number(PRM[0]) and not "." in PRM[0]: variables["return"] = int(PRM[0])

        return

    if name == "TF":
        if PRM != []:
            if PRM[0].isdecimal() and "." in PRM[0]: variables["return"] = float(PRM[0])

        return

    if name == "EXIT":
        exit()

def remove_strings(line):
    strings = re.findall(r'"(.*?)"',line)
    temp_line = line

    for temp_str in strings:
        temp_line = temp_line.replace(temp_str,"")

    return temp_line

def parse_line(line,shell = False):
    # Optimise Later :)
    global in_label,in_goto,current_line,goto_line,STOP_END

    # GLOBAL DEBUG SPOT!
    #print(current_line + 1, " ", goto_line)
    #print(f"line number ({current_line + 1},{goto_line + 1}): {line}")
    #print(variables)

    temp_line_array = line.strip().split(" ",1)

    if line == "":
        return

    if "!" in line:
        temp_line = remove_strings(line)

        if "!" in temp_line:
            line = line.replace(line[line.find("!"):],"")

    # Line Array
    line_array = line.strip().split(" ",1)

    if line.startswith(":") and not shell:
        labels[line[1:].replace(" ","")] = current_line
        in_label = True

        return

    # IMPORT
    if line_array[0] == "IMPORT":
        if len(line_array) > 1:
            load_lib(line_array[1])

    if line_array[0] == "IMPORT_LOCAL":
        if len(line_array) > 1:
            load_lib(line_array[1],True)

    # END
    if line_array[0] == "END" and not shell:
        if (in_label or in_goto):
            in_label = False

            # Examine this code, as it has brought you a problem that was fixed only by a restless night!
            if in_goto and not STOP_END:
                current_line = goto_line
                STOP_END = True
            else: 
                in_goto = False
                STOP_END = False

            return
        else:
            error("No Label to END!")

    if in_goto or not in_label:
        # VARS
        if "=" in line:
            temp_line = remove_strings(line)

            if "=" in temp_line:
                assign_var(line)

                return

        if line_array[0] in built_in:
            # RTRN
            if line_array[0] == "RTRN":
                if len(line_array) > 1:
                    env_variables["return"] = clean_value(
                        ''.join(
                            line_array[1:len(line_array)]
                        )
                    )
                else:
                    pass
            # GOTO
            elif line_array[0] == "GOTO" and not shell:
                if len(line_array) > 1:
                    in_goto = True

                    goto_line = current_line
                    current_line = labels[line_array[1].replace(" ","")]

            return
        
        if len(line_array) > 1:
            #re.findall(r'"(.*?)"',"INSERT") # This is a "anything in quotes" in string regex
            
            # Comma Matcher
            matcher = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
            TEMP_PRM = matcher.split(line_array[1])
            PRM = []

            # WE ARE CLOSE

            for prm in TEMP_PRM:
                PRM.append(clean_value(prm))
        else:
            PRM = []

        if line_array[0] in built_in_funcs or line_array[0] in list(build_in_math.keys()) or line_array[0] in funcs:
            command(line_array[0],PRM)

    return

def parse_file(current_file):
    global current_line

    with open(current_file,"r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i][-1:] == "\n":
            lines[i] = lines[i][:-1]

    while not current_line >= len(lines) - 1:
        current_line += 1
        parse_line(lines[current_line])

    current_line = -1

def main():
    global to_shell

    #debug!
    #if sys.argv[0].endswith("\\"):
    #    env_variables["lang_path"] = sys.argv[0]
    #else:
    #env_variables["lang_path"] = os.path.dirname(sys.argv[0].replace("\\","/"))

    # Might not work on linux...
    # env_variables["lang_path"] = str(pathlib.Path(__file__).parent.resolve())
    # sys.insert_path(0, “path”)

    if len(sys.argv) > 1:
        if sys.argv[1] == "shell":
            to_shell = True

            shell()
        elif sys.argv[1] == "open":
            to_shell = False

            if len(sys.argv) > 2:
                if len(sys.argv) > 3:
                    env_variables["lang_path"] = sys.argv[3]

                current_file = env_variables["file_path"] + "\\" + sys.argv[2]
                parse_file(current_file)
            else:
                print("ERROR: No input files!")
        elif sys.argv[1] == "help":
            print("If you need help understanding how asmblr works... good luck!\nI'm just kidding, here is an example: ASMBLR open <file>.asmblr\nYou can also open the shell interpreter! (example: ASMBLR shell)")

main() 
