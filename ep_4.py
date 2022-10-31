import sys #No need to install this librarie, it already comes with python

file_path = sys.argv[1]

file = open(file_path, "r+") #Opens the file
file_read = file.read() #Reads the file
contents = file_read.split("\n") #Separates the character by lines

variables = {} #Dictionarie for variables
var_names = []
inputs = {}
inp_names = []

for i in contents:
    if i != " " or i != "\n" or i != "" or "//" not in i:
        if "PRINT " in i:
            first_separation = i.split("PRINT")
            if '"' in first_separation[1]:
                text = first_separation[1].split('"')
                print(text[1])
            else:
                for j in var_names:
                    if j in first_separation[1]:
                        print(variables[j])
                for k in inp_names:
                    if k in first_separation[1]:
                        print(inputs[k])
        elif "VAR " in i:
            first_separation = i.split("VAR")
            second_separation = first_separation[1].split(" ") #No need for an argument here
            value = None
            var_name = second_separation[1]
            if '"' in second_separation[3]:
                third_separation = first_separation[1].split('"')
                #First index is the text
                value = third_separation[1]
                variables[var_name] = value
            else:
                value = second_separation[3]
                variables[var_name] = value

            var_names.append(var_name)
            

        elif "INPUT " in i:
            first_separation = i.split("INPUT")
            second_separation = first_separation[1].split(" ")
            inp_text = first_separation[1].split('"')[1]
            inp_name = first_separation[1].split("=> ")[1]
            main_inp = input(inp_text)
            inp_val = main_inp
            inputs[inp_name] = inp_val
            inp_names.append(inp_name)
            

