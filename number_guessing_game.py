import random

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Ask the player to choose a difficulty level
print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = input("\nEnter your choice: ")
choice = int(choice)  # convert the string input into an integer

# Set number of attempts based on chosen difficulty
if choice == 1:
    attempts = 10
    difficulty = "Easy"
elif choice == 2:
    attempts = 5
    difficulty = "Medium"
elif choice == 3:
    attempts = 3
    difficulty = "Hard"
else:
    print("Invalid choice, defaulting to Medium.")
    attempts = 5
    difficulty = "Medium"

print(f"\nGreat! You have selected the {difficulty} difficulty level.")
print("Let's start the game!\n")

# Generate the secret number
secret_number = random.randint(1, 100)
attempts_used = 0

# Main guessing loop
while attempts_used < attempts:
    guess = int(input("Enter your guess: "))
    attempts_used += 1

    if guess < secret_number:
        print("Incorrect! The number is greater than", guess)
    elif guess > secret_number:
        print("Incorrect! The number is less than", guess)
    else:
        print(f"Congratulations! You guessed the correct number in {attempts_used} attempts.")
        break
else:
    print(f"\nSorry, you've run out of attempts! The number was {secret_number}.")
