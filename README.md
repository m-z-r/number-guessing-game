# 🎯 Number Guessing Game in Python

A simple and interactive **Number Guessing Game built with Python** using the built-in `random` module. The computer selects a secret number between 1 and 100, and the player tries to guess it with hints along the way.

## ✨ Features

- 🎲 Random number generation between 1 and 100
- 🔍 Helpful hints when your guess is too high or too low
- 🔢 Tracks the number of valid guesses
- ⚠️ Handles invalid input without crashing
- 🏆 Displays a congratulatory message when you win
- 🐍 Beginner-friendly Python code with comments

## 🛠️ Technologies Used

- **Python 3**
- **Random Module** — generates the secret number
- **While Loop** — keeps the game running
- **Conditional Statements** — checks the player's guess
- **Exception Handling** — handles invalid input

## 📂 Project Structure

```text
number-guessing-game/
│
├── number_guessing_game.py
└── README.md
```

## 🚀 How to Run the Game

### 1. Install Python

Download Python 3 from [python.org](https://www.python.org/downloads/) if it isn't already installed.

### 2. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 3. Open the Project Folder

```bash
cd number-guessing-game
```

### 4. Run the Game

```bash
python number_guessing_game.py
```

**No additional libraries are required!** The `random` module comes pre-installed with Python.

## 🎮 How to Play

1. Run the Python program.
2. The computer chooses a secret number between 1 and 100.
3. Enter your guess when prompted.
4. Follow the hints:
   - **Too low!** Try a higher number.
   - **Too high!** Try a lower number.
5. Keep guessing until you find the correct number.
6. See how many attempts you needed to win!

## 💻 Example Output

```text
================================
     NUMBER GUESSING GAME
================================
I have chosen a number between 1 and 100.
Can you guess it?

Enter your guess: 25
Too low! Try a higher number.

Enter your guess: 75
Too high! Try a lower number.

Enter your guess: 52
Congratulations! You guessed it!
The secret number was 52.
You got it in 3 attempts!

Thanks for playing!
```

*Note: The secret number and hints will vary each time you play.*

## 📚 What You'll Learn

By building this project, beginners can practice:

- Generating random numbers with `random.randint()`
- Using `while` loops
- Applying `if`, `elif`, and `else` statements
- Getting user input with `input()`
- Converting strings into integers with `int()`
- Handling errors with `try` and `except`
- Using `break` to exit a loop
- Counting attempts with variables

## 🔮 Future Improvements

Want to make the game even better? Try adding:

- 🎚️ Different difficulty levels
- ❤️ A limited number of guesses
- 🔄 An option to play again
- 🏅 A high-score system
- 🖥️ A graphical interface using Tkinter

## 📄 License

This project is open-source and available for learning and personal use. Add a license file to your repository if you want to specify formal reuse and distribution terms.

---

**Enjoy coding and happy guessing!** If you're learning Python, this is a great first project to practice programming fundamentals.
