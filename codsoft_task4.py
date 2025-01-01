import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
def display_scores(user_score, computer_score):
    print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}\n")
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.\n")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        display_scores(user_score, computer_score)
    print("Thanks for playing! Final scores:")
    display_scores(user_score, computer_score)
if __name__ == "__main__":
    main()
