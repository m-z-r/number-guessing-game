
# Import the random module to generate a random number
import random

# Choose a random integer between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to count the player's guesses
attempts = 0

# Display the game title and instructions
print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?")

# Start an infinite loop so the player can keep guessing
while True:
    try:
        # Ask the player to enter a number
        guess = int(input("\nEnter your guess: "))

        # Count this valid numerical guess
        attempts += 1

        # If the guess is smaller than the secret number
        if guess < secret_number:
            print("Too low! Try a higher number.")

        # If the guess is greater than the secret number
        elif guess > secret_number:
            print("Too high! Try a lower number.")

        # If neither condition is true, the guess is correct
        else:
            # Display the winning message and game results
            print("\nCongratulations! You guessed it!")
            print(f"The secret number was {secret_number}.")
            print(f"You got it in {attempts} attempts!")

            # Stop the loop because the player has won
            break

    # Handle invalid input, such as letters instead of numbers
    except ValueError:
        # Display an error message without crashing the game
        print("Invalid input! Please enter a whole number.")

# Display a final message after the game ends
print("\nThanks for playing!")
