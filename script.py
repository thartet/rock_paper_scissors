import os
import re
import random

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ['Y', 'y', 'yes', 'Yes', 'Of course!']:
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you very much for playing our game. See you next time!")
        return False

def main():
    play = True
    scores = [0, 0]
    while play:
        # Clear the screen for a fresh start, adapting to Windows or Linux
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("Rock, Paper, Scissors - Shoot!")
        print("Scores: You {} - {} Computer".format(scores[0], scores[1]))

        user_input=input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
        
        #Validate the user's input
        if not re.match("[SsRrPp]", user_input):
            print("Please choose a letter:")
            print("[R]ock, [S]cissors or [P]aper.")
            continue
            
        # Echo the user's choice
        print("You chose: " + user_input)
        choices = ['R', 'P', 'S']
        opponent_choice = random.choice(choices)

        # Echo the opponent's choice
        print("I chose: " + opponent_choice)

        # Determine the winner
        if opponent_choice == str.upper(user_input):
            print("Tie!")
            play=play_again()
        elif opponent_choice == 'R' and user_input.upper() == 'S':
            print("Scissors beats rock, I win!")
            scores[1] += 1
            play=play_again()
        elif opponent_choice == 'S' and user_input.upper() == 'P':
            print("Scissors beats paper! I win!")
            scores[1] += 1
            play=play_again()
        elif opponent_choice == 'P' and user_input.upper() == 'R':
            print("Paper beat rock, I win!")
            scores[1] += 1
            play=play_again()
        else:
            print("You win!\n")
            scores[0] += 1
            play=play_again()


if __name__ == '__main__':
    main()
else:
    print("[-] script.py did not execute correctly.")