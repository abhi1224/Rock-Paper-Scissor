import random 

def drawline():
    for i in range(1,29):
        print("__" , end=" ")
    
    print("\n")

def gameRule():
    print (''' \n \n Game's rule :- \n 
    1. If both player choise the same things then the game will be tie.
    2. If player 1 choise the rock and player 2 choice the scissor . 
       The rock smashes the scissor that's why the player 1 (Rock) will be win .
    3. If player 1 choise the rock and player 2 choice the paper . 
       The paper cover the rock that's why the player 2 (Paper) will be win .     
    4. If player 1 choise the scissor and player 2 choice the rock . 
       The rock smashes the scissor that's why the player 2 (Rock) will be win .
    5. Press r for Rock , p for Paper and s for Scissor.
    ''')

def playagain():
    drawline()
    playAgain = input("Play Again ? : y/n :")

    if(playAgain.lower() == "n"):
        exit() 


def game(userAction , computerAction):

    if userAction == computerAction:
        print(f"Both players selected {userAction}. It's a tie!")

    elif userAction == "r":
        if computerAction == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif userAction == "p":
        if computerAction == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif userAction == "s":
        if computerAction == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    playagain()
    


if __name__ == "__main__": 

    drawline()
    gameRule()
    drawline()

    while True:
        possibleAction = ["r", "p", "s"]
        computerAction = random.choice(possibleAction)
        userAction = input("\nPlayer 1 : \nRock (r) Paper(p) Scissor (s): ")
        userAction = userAction.lower()

        print(f"\nPlayer 2 : \nRock (r) Paper(p) Scissor (s): {computerAction} \n \n")
        drawline()

        if(userAction in possibleAction):
            game(userAction, computerAction)
        else:
            print("Please enter correct word. r for Rock and p for Paper and s for Scissor.")   
            playagain()
            
            
