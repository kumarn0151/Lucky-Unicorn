

# Functions go here...
def yes_no(question):
    valid = False 
    while not valid:
        response = input (question).lower()

        if response == "yes" or response =="y":
            # response ="yes"
            return "yes" 

        elif response == "no" or response =="n":
            response = "no"
            return response 

        else:
            print ("please answer yes/ no ")


# Main Routine goes here...
show_instructions = yes_no("have you played the"
                            " game before? ")
print("you choose {}". format (show_instructions))
print ()
Having_fun = yes_no ("Are you having fun? ")
print ("you said {} to having fun.format (having_fun")