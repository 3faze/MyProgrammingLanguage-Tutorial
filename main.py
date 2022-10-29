run = True
while run: #Infinite loop
    main = input("> ")
    first_final = main.split(" ") #You don't need arguments there but I like to keep them
    final = " ".join(first_final)
    print(eval(final))
    if main == "quit": #Checking if the user is quitting
        quit()