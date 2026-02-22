import random

com_score = 0
player_score = 0
player2_score = 0

Wins = 0
Loses = 0
Ties = 0

Player1 = 0
Player2 = 0

while True:

    player_mode = int(input("Choose playing mode (comvp(1)/pVp(2)): "))
    if player_mode == 1:
        for i in range(3):
            print(f"\nRound {i + 1}")

            while True:
                player_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

                if player_choice == "r":
                    print("You chose 🪨")
                    break
                elif player_choice == "p":
                    print("You chose 📃")
                    break
                elif player_choice == "s":
                    print("You chose ✂️")
                    break
                else:
                    print("Invalid input")
                    

            choices = ["r","p","s"]
            com_choice = random.choice(choices)

            if com_choice == "r":
                print("Computer chose 🪨")
            elif com_choice == "p":
                print("Computer chose 📃")
            elif com_choice == "s":
                print("Computer chose ✂️")   

        
            if player_choice == com_choice:
                print("You tied")
            elif player_choice == "r" and com_choice == "p" or player_choice == "p" and com_choice == "s" or player_choice == "s" and com_choice == "r":
                print("You lose")
                com_score += 1
            elif player_choice == "r" and com_choice == "s" or player_choice == "p" and com_choice == "r" or player_choice == "s" and com_choice == "p":
                print("You win")
                player_score += 1


        if player_score > com_score:
            print("\nCongratz. You Wins the game!!") 
            Wins += 1
        elif com_score > player_score:
            print("\nGame over. You Lost. Better luck next time.")
            Loses += 1
        elif player_score == com_score:
            print("\nIts a Tie 👔")
            Ties += 1

        print(f"Wins: {Wins}")
        print(f"Loses: {Loses}")
        print(f"Ties: {Ties}")
        
        while True:
            replay = input("\nReplay game?(y/n): ").lower()
            if replay == "n":
                print("Thanks for playing!!")
                exit()
            elif replay == "y":
                break
            else:
                print("Invalid input")

    elif player_mode == 2:

        for i in range(3):
            print(f"\nRound {i + 1}")

            while True:
                player_choice = input("Rock, Paper, Scissors? (r/p/s)(P1): ").lower()

                if player_choice == "r":
                    print("You chose 🪨")
                    break
                elif player_choice == "p":
                    print("You chose 📃")
                    break
                elif player_choice == "s":
                    print("You chose ✂️")
                    break
                else:
                    print("Invalid input")
            
            while True:
                player2_choice = input("\nRock, Paper, Scissors? (r/p/s)(P2): ").lower()

                if player2_choice == "r":
                    print("You chose 🪨")
                    break
                elif player2_choice == "p":
                    print("You chose 📃")
                    break
                elif player2_choice == "s":
                    print("You chose ✂️")
                    break
                else:
                    print("Invalid input")

            if player_choice == player2_choice:
                print("You tied")
            elif player_choice == "r" and player2_choice == "p" or player_choice == "p" and player2_choice == "s" or player_choice == "s" and player2_choice == "r":
                print("Player2 wins")
                player2_score += 1
            elif player2_choice == "r" and player_choice == "s" or player2_choice == "p" and player_choice == "r" or player2_choice == "s" and player_choice == "p":
                print("Player1 win")
                player_score += 1

        if player_score > player2_score:
            print("\nPlayer 1 Wins the game!!") 
            Player1 += 1
        elif player2_score > player_score:
            print("\nPlayer 2 Wins the game!!")
            Player2 += 1
        elif player_score == player2_score:
            print("\nIts a Tie 👔")
            Ties += 1
            
        print(f"Player1: {Player1}")
        print(f"Player2: {Player2}")
        print(f"Ties: {Ties}")
        
        while True:
            replay = input("\nReplay game?(y/n): ").lower()
            if replay == "n":
                print("Thanks for playing!!")
                exit()
            elif replay == "y":
                break
            else:
                print("Invalid input")   
    else:
        print("Invalid Input")