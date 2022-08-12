#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
$$\   $$\ $$\           $$\                                                           $$\                                                                                                   
$$ |  $$ |\__|          $$ |                                                          $$ |                                                                                                  
$$ |  $$ |$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\        $$ |     $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\       $$ |    $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\       $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ /  $$ |$$ |  \__|      $$ |    $$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  \__|      $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |            $$ |    $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |            $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
$$ |  $$ |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |            \$$$$$$  |$$ |            $$$$$$$$\$$$$$$  |\$$$$$\$$$$  |\$$$$$$$\ $$ |            \$$$$$$$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
\__|  \__|\__| \____$$ |\__|  \__| \_______|\__|             \______/ \__|            \________\______/  \_____\____/  \_______|\__|             \____$$ | \_______|\__| \__| \__| \_______|
              $$\   $$ |                                                                                                                        $$\   $$ |                                  
              \$$$$$$  |                                                                                                                        \$$$$$$  |                                  
               \______/                                                                                                                          \______/                                   
"""

import random

print(logo)
print("Welcome to the Numbers Guessing Game!")
print("I'm thinking of a numbe between 1 and 100")


def number_of_lives():
    correct_response = False
    while not correct_response:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()
        if difficulty == 'hard':
            return 5
            correct_response = True
        elif difficulty == 'easy':
            return 10
            correct_response = True
        else:
            print("Not a valid option, please type 'easy' or 'hard'")


def play_game(lives):
    number = random.randint(1,100)
    game_active = True
    while game_active:
        print(f"You have {lives} remaining to guess the number")
        guess = int(input("Please make a guess:"))
        if lives == 1:
            print(f"You ran out of lifes, the number was {number}. Game over.")
            game_active = False
            break
    
        if guess == number:
            print(f"Well done, you have guessed {number} correctly!")
            game_active = False
        elif guess > number:
            print("Too high, guess again")
            lives -= 1
        else:
            print("Too low, guess again")
            lives -=1

numoflives = number_of_lives()
play_game(numoflives)
