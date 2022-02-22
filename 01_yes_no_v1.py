# Ask the user if they have played before 

show_instructions = ""
while show_instructions != "xxx":

    show_instructions = input ("Have you played this game "
                                "before? ").lower()

    # If they say yes, output 'program continues' 
    if show_instructions == "yes":
        print ("program continues")

    elif show_instructions == "y":
        print ("program continues")

    elif show_instructions == "no":
        print("display instructions") 

    elif show_instructions == "n":  
        print ("display instructions")

        # if they say no, output 'display instructions'
    else:
        print ("please answer yes / no")
