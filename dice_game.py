
'''
Owen Powell
IS 303 - A04

Dice Game
This program lets you roll a dice against the computer.

Inputs:
- which sided die would the player like to use
- how many rounds would the user like to play


Processes:
- get_valid_die() This makes sure the selected die has either 6, 8, 10, 12, or 20 sides. 
- get_valid_rounds() This makes sure the selected amount of rounds is a number 1-10
- roll_dice(num_sides) This picks a random number between 1 and whatever the selected sides are.
- determine_winner(player_roll, computer_roll) This checks the two rolls and determines who won, returning a string.
- play_round(num_sides, scoreboard) This creates the player_roll and computer_roll variables, rolling for both.
    It calls the determine_winner function and stores the info in a scoreboard list of dictionaries. Displays rolls for the user and computer.
- show_scoreboard(scoreboard, rounds_chosen) This shows how many rounds have been played, how many rounds are left, and the score.

Outputs:
- Scoreboard that shows the round number, the rounds remaining, and a
running tally of round wins for the player and computer.
'''
import random
scoreboard = []

def get_valid_die():
    while True:
        try:
            num_sides = int(input("How many sides on the dice? (6, 8, 10, 12, 20) "))
            if num_sides not in [6, 8, 10, 12, 20]:
                print("Please enter a valid dice number.")
            else:
                return num_sides
        except ValueError:
            print("Please enter a valid dice number.")

def get_valid_rounds():
    while True:
        try:
            rounds_chosen = int(input("How many rounds would you like to play? (1-10) "))
            if rounds_chosen not in range(1,11):
                print("Please enter a number 1-10.")
            else:
                return rounds_chosen
        except ValueError:
            print("Please enter a number 1-10.")

def roll_die(num_sides):
    roll = random.randint(1, num_sides)
    return roll

def determine_winner(player_roll, computer_roll):
    if player_roll > computer_roll:
        return "Player"
    elif player_roll == computer_roll:
        return "Tie"
    else:
        return "Computer"
    
def play_round(num_sides, scoreboard):
    player_roll = roll_die(num_sides)
    computer_roll = roll_die(num_sides)
    winner = determine_winner(player_roll, computer_roll)
    while winner == "Tie":
        player_roll = roll_die(num_sides)
        computer_roll = roll_die(num_sides)
        winner = determine_winner(player_roll, computer_roll)
    print(f"You rolled: {player_roll}")
    print(f"The computer rolled: {computer_roll}")
    round_number = len(scoreboard) + 1
    
    
    
    scoreboard.append({"round":round_number, 
    "player_roll":player_roll, 
    "computer_roll":computer_roll,
    "winner":winner})

def show_scoreboard(scoreboard, rounds_chosen):
    player_wins = 0
    computer_wins = 0
    rounds_played = len(scoreboard)
    rounds_remaining = rounds_chosen - rounds_played
    print(f"Rounds played: {rounds_played} - Rounds remaining: {rounds_remaining}")
    for i in scoreboard:
        if i["winner"] == "Player":
            player_wins += 1
        elif i["winner"] == "Computer":
            computer_wins += 1
        print(f"Round {i['round']}. You rolled a {i['player_roll']} - The computer rolled a {i['computer_roll']} - Winner: {i['winner']}")
    print(f"--- Your wins: {player_wins} - Computer Wins: {computer_wins} ---")

print("Welcome to my dice game! You will roll against the computer, and you can play with dice that have 6, 8, 10, 12, or 20 sides!")
num_sides = get_valid_die()
rounds_chosen = get_valid_rounds()
for i in range(rounds_chosen):
    play_round(num_sides, scoreboard)
show_scoreboard(scoreboard, rounds_chosen)