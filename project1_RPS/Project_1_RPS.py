import random # Import random module to let the computer choose from given list

choices = [ "rock" ,"paper", "scissors"]

while True:
    
    # ask user for the input
    user = input("\n Enter your hand : (Rock, paper or Scissors)  ").lower()
    
    if user not in  choices:
        print("\n You entered the wrong hand, do it again")
        continue
    
    computer = random.choice(choices)
    print("\nyour hand is     : ", user)
    print("computer hand is : ", computer)
    
    
    if user == computer:
        print("\n It is a tie.")
        
    elif(
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ): 
        print("\n whohooo, you won")
            
    else:
        print("\n  you lose!")
        
        
    play_again = input("\n do you want to play again, (yes/no)")
    
    
    if play_again != "yes":
        print("thanks for playing!")
        
        break
    
    
    
input("press enter to close terminal")