import random
print("\n===============Welcome to the Dice Game===============")
# Prompt the user to enter their name.
player_name = input("Please enter your name: ").capitalize()
#Greets User
print(f"Hello, {player_name}! Let's play the dice game.\n")
#Explain Rules
print("First the rules:\nI will roll a dice and so will you.\nThe player with the higher number wins the round.\nThe first player to reach 5 points wins the match. Good luck!\n")

#Defining Functions To Start The Game And Play Again
def play_game():
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        input("Press Enter to roll the dice...")
        print("Rolling the dice...")
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        print(f"{player_name} rolled a {player_roll}.")
        print(f"Computer rolled a {computer_roll}.")

        if player_roll > computer_roll:
            player_score += 1
            print(f"{player_name} wins this round! Score: {player_score} - {computer_score}\n")
        elif computer_roll > player_roll:
            computer_score += 1
            print(f"Computer wins this round! Score: {player_score} - {computer_score}\n")
        else:
            print("It's a tie! Roll again.\n")

    if player_score == 5:
        print(f"Congratulations, {player_name}! You won the match with a score of {player_score} - {computer_score}.")
    else:
        print(f"Computer wins the match with a score of {computer_score} - {player_score}. Better luck next time, {player_name}!")

def play_again():
    choice = input("Do you want to play another match? (yes/no): \n").strip().lower()
    if choice == 'yes':
        play_game()
        play_again()
    elif choice == 'no':
        print("\nThank you for playing! Goodbye!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.\n")
        play_again()

#calls Function to run the Game
play_game()
play_again()
