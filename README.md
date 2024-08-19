# Project: Rock, Paper, Scissors Game

## **Overview:**

The goal of this project is to design a rock, paper, scissors game. Through this project, you will not only improve your understanding of the Python language but also enhance your grasp of the fundamental principles of coding. It is important to write your project code according to PEP-8 guidelines and to bring out your creativity in this project.

## **Project Objectives:**

- To apply fundamental Python concepts such as loops, conditional statements, and user input.
- To develop logical thinking skills and adaptability to flexibility.

## **Project Outline:**

- You will create a function for the rock, paper, scissors game and name this function rock_paper_scissors_YOUR_NAME_SURNAME.
- Your function should work smoothly and be executable in the Python terminal as rock_paper_scissors_YOUR_NAME_SURNAME().
- The game will consist of multiple rounds, and the first player to win two rounds will be the overall winner.
- After each game, both the user and the computer will be asked if they want to play another game. If both parties agree, the game will be repeated. (Don't forget to be kind to the computer! 😊)
- Remember! If your code doesn’t work, your project will not be evaluated.

 
## **Steps to Follow While Creating the Project:**

### 1. **Game Introduction:**

- Create a welcome message that explains the rules of the game.
- Inform the user about how to play the game or how to exit the game.
- The game rounds should consist of three outcomes: the player can win, the computer can win, or it can be a tie.
- The first to win two rounds wins the game.

### 2. **Game Setup:**
 

 - Define a list consisting of rock, paper, and scissors options. More options won’t hurt. Remember, your imagination will carry you forward.
 - Initialize counters for the number of games played, rounds played, player wins, and computer wins.

### 3. **Main Game Loop:**

- Use a while loop to make the game playable.
- Inside this loop, reset the round and win counters for each new game.

### 4. **Round Loop:**

- Use another while loop until either the player or the computer wins two rounds.
- Ask the player to choose one of the three options, and if they select an invalid option, ask them to enter a choice again.
- Generate the computer's choice randomly (hint: you can use the random module).
- After receiving the choices, use logical operations or basic if-else statements to determine the winner of the round.
- Since the first to win two rounds wins the game, don’t forget to update the win counters.
- Print the result of each round to the screen (hint: the print() function is perfect for this).

### 5. **Determine the Game Winner:**

- After the round loop ends (when one player wins two rounds), determine the overall winner of the game and display the appropriate message.

### 6. **Request to Continue:**

- Ask the user if they want to play another game.
- Ask if the computer wants to continue playing (you can generate a random answer).
- If both parties want to continue, the game should continue; however, if either party does not want to continue, the game should end (hint: you can use break for this).
- Display the appropriate message for each situation.
