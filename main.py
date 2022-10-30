import sys #No need to install this librarie, it already comes with python

file_path = sys.argv[1]

file = open(file_path, "r+") #Opens the file
file_read = file.read() #Reads the file
contents = file_read.split("\n") #Separates the character by lines

for i in contents:
    if i != " " or i != "\n" or i != "":
        if "PRINT " in i:
            first_separation = i.split("PRINT")
            try:
                text = first_separation[1].split('"')
                print(text[1])
            except:
                if '"' not in first_separation:
                    print(first_separation[1].split()[0])
