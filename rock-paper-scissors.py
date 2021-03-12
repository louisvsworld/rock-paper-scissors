import random

state = ""

while state == "":
    user = input("Choose your weapon! [Rock, Paper, Scissors] ")


    value = random.randint(1,3)

    #Sets value of weapon per integer
    if value == 1:
        value = "Rock"
    elif value == 2:
        value = "Paper"
    elif value == 3:
        value = "Scissors"

    if user == "Rock" or user == "Paper" or user == "Scissors":
        print("────────────────────────────────────────────────\nBot chose " + str(value)) 
    else:
       print("────────────────────────────────────────────────\nERROR ERROR ERROR\nPlease choose between 'Rock', 'Paper', or 'Scissors' ")
       

    #In the case of a tie
    if user == value:
        print("It's a tie!")
    
    #Determines if user wins or loses
    if user == "Scissors" and value == "Rock":
        print("You have lost.. ")
    elif user == "Rock" and value == "Paper":
        print("You have lost.. ")
    elif user == "Paper" and value == "Scissors": 
        print("You have lost..")
    elif user == "Scissors" and value == "Paper":
        print("You have won! ")
    elif user == "Rock" and value == "Scissors": 
        print("You have won! ")
    elif user == "Paper" and value == "Rock":
        print("You have won! ") 

    
    #Enables user to play again or end game by altering the variable while is dependent on
    state = input("────────────────────────────────────────────────\nPress enter to play again or type 'exit' to leave\n────────────────────────────────────────────────\n")

