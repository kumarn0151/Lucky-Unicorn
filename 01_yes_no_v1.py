# Ask the user if they have played before 

show_instructions = ""
while show_instructions != "xxx":

    show_instructions = input ("Have you played this game "
                                "before? ").lower()
# if they say yes, output 'program continues'
# if they say no, output 'display instructions'
# if the answer is invaild, print an error.
 
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions == "yes"
        print ("program continues")

    elif show_instructions == "y":
        print ("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print ("program continues")

        print("display instructions") 

    elif show_instructions == "n":  
        print ("display instructions")

        # if they say no, output 'display instructions'
    else:
        print ("please answer yes / no")
