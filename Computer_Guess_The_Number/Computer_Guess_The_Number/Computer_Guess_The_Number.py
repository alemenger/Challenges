import random as r


def computer_guess_the_number(x):

    print(" +++++++++++++++++++ ")
    print(" ++    WELCOME    ++ ")
    print(" +++++++++++++++++++\n ")
    print(f" Think in a number between 0 and {x} \n")


    limite_inferior = 0
    limite_superior = x

    answer = ""
    while answer != "c":
        #
        #GENERATE THE PREDICTION
        if limite_inferior != limite_superior:
            prediction = r.randint(limite_inferior,limite_superior)
        else:
            prediction = limite_inferior #tambien podria ser limite superior
        
        #GET USER INPUT
        answer = input(f" My prediction is {prediction}.\n\n"
         " If is bigger than your number, insert ('A').\n" 
         " If is lower than your number insert ('B').\n"
         " If it is correct, insert ('C').\n").lower()  
        if answer == "a":
            limite_superior = prediction - 1
        elif answer == "b":
            limite_inferior = prediction + 1 

    print(f" Yess! The computer guessed your number: {prediction}")

        
computer_guess_the_number(30)
