import random


def rock_paper_scissors_metin_kuris():

    """
    Plays a game of Rock, Paper, Scissors with the user.

    The game consists of multiple rounds where the player competes against the computer. 
    The player and the computer each choose one of "rock", "paper", or "scissors". 
    The outcome of each round is determined based on the rules of the game:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock

    The game continues until either the player or the computer wins 2 rounds.
    At the end of the game, the player is asked if they want to play again. 
    If the player chooses to play again, the game restarts; otherwise, the game ends.

    The game also handles invalid inputs by prompting the user to enter a valid choice.
    """

    print(
          "We are playing one of the famous games in the world!\n"
          "Rock, paper, and scissors!\n"
          "We will play 3 rounds and whoever wins a total of 2 rounds, wins the game.\n"
          "Enter rock, paper, or scissors to play, or if you do not want to play, write 'exit'\n"
          "The game starts NOW! \n\n"
)
    game_number = 1   # Game number 
    rounds_number = 1 # Round number 
    player_wins = 0   # Number of player wins
    computer_wins= 0  # Number of computer wins


    valid_answer = ["rock", "paper","scissors","exit"] # Valid input values

    while True:

        print(f"### Game {game_number}, Round {rounds_number}: ###")
        
        # The entered value is converted to lowercase letters and spaces are deleted.
        ask_to_player = input("Rock, Paper, Scissors, or Exit?: ").lower().strip() 
       
        if ask_to_player not in valid_answer: # Enter the valid value
            print("Invalid choice! Please try again. Either choose rock, paper, or scissors.\n")
            continue

        if ask_to_player == "exit":
            if game_number == 1: 
                print(
                      "Well, then why did you call the function if you don't want to play? " 
                      "Come back when you really want to play the game."
                )
            else:
                print("Thanks for playing!")
            break
        
        computer_choice = random.choice(valid_answer[:-1]) # Compter is chosen random in the valid_answer.

        print(f"\nPlayer chose: {ask_to_player}")
        print(f"Computer chose: {computer_choice}\n")

        if computer_choice == ask_to_player: # If there is a tie.
            print("It's a tie this round!\n")
        elif (ask_to_player == "rock" and computer_choice == "scissors") or \
             (ask_to_player == "paper" and computer_choice == "rock") or \
             (ask_to_player == "scissors" and computer_choice == "paper"):  # If player win the round.
             
             player_wins += 1
             print(" You are so lucky! You win this round.\n")
        else:  # if computer win the round.
            print("Hah! You lose this round!\n")
            computer_wins += 1

        print(f"Player: {player_wins}, Computer: {computer_wins}\n")
        print("####################################\n")
        rounds_number += 1

        if  player_wins == 2: # If player have 2 wins, player win the game 
            print("You have won the game.\n")
            
        elif computer_wins == 2: # If computer have 2 wins, it win the game.
            print("Hah! Loser, you have lost the game.\n") 
                  

        if player_wins == 2 or computer_wins == 2: # If the computer or the player wins 2 rounds in a game
            player_continue = input("Do you want to challage me again, champion? (yes/no):")

            computer_answer = ["yes","no"]
            computer_continue = random.choice(computer_answer) # Computer is chosen random in the computer_answer.

            if player_continue == "yes" and computer_continue == "yes": # If player and computer  want to play agian the game
                print("I want to play again as well! Let's play one more!")
                game_number += 1
                rounds_number = 1
                player_wins = 0
                computer_wins= 0 
                continue

            elif player_continue == "no": # If player do not want to play agian the game
                print("Come back whenever you want to play, see you.") 
                break

            else:
                print("Unfortunately, I don't want to play, maybe later.")
                break

        else: 
            continue
 
       
if __name__ == "__main__":
    rock_paper_scissors_metin_kuris()