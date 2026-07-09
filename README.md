```markdown
🎮 # Hangman Game

A simple, interactive text-based Hangman game built entirely with Python. The player guesses a hidden word one letter at a time before running out of attempts.

---

 📋 Overview

Hangman is a classic word-guessing game. The program selects a random word from a predefined list and displays it as blank spaces. The player must guess letters to reveal the word. For every wrong guess, a part of the hangman is drawn. The game ends when the player either guesses the full word or makes 6 incorrect guesses.

---

 🎯 # Features

- **Random Word Selection:** Picks a random word from a list of 5 predefined words.
- **Visual Progress:** Displays a text-based hangman figure that updates with each wrong guess.
- **Input Validation:** Ensures the player only enters single alphabetic characters and prevents duplicate guesses.
- **Guess Tracking:** Keeps track of all previously guessed letters and displays remaining wrong guesses.
- **Replayability:** Prompts the player to play again without restarting the script.

---

 🛠️# Key Concepts Used

This project is designed to practice fundamental Python concepts:

| Concept | How it is used in the code |
|---------|----------------------------|
| **`random` module** | `random.choice(WORD_LIST)` is used to pick a random word at the start of the game. |
| **`while` loop** | Keeps the main game running until the player wins or loses. |
| **`if-else`** | Checks if the guessed letter is in the word (correct/wrong logic). |
| **`strings`** | Builds the hidden word display using underscores (`_`) and spaces. |
| **`lists`** | Stores the `WORD_LIST` and tracks `guessed_letters`. |
| **Functions** | Breaks the code into reusable blocks (e.g., `get_player_guess()`, `display_game_state()`). |

---

 📁 # Project Structure

```text
hangman_game/
│
├── hangman.py          # Main Python script containing all game logic
└── README_hangman.md   # Documentation file (you are reading this)
```

---

 🚀# How to Run

### Prerequisites
- Python 3.x installed
- VS Code (recommended) or any text editor
- Terminal/Command Prompt

### Steps
1. Open terminal in the project folder
2. Run the following command:

```bash
python hangman.py
```

*(Alternatively in VS Code: Open `hangman.py` and press `Ctrl + F5`)*

---

 🎮# How to Play

1. The game starts and shows a blank word (e.g., `_ _ _ _ _`) and an empty hangman gallows.
2. Type a single letter (a-z) and press **Enter**.
3. If the letter is in the word, it will be revealed in the correct positions.
4. If the letter is NOT in the word, you lose one of your 6 lives, and the hangman drawing progresses.
5. Continue guessing until you either reveal the entire word (WIN) or run out of 6 lives (LOSE).
6. Type `yes` or `no` when asked if you want to play again.

---

 💻 # Code Architecture

The script is divided into modular functions for clean code structure:

- **`WORD_LIST`**: A list containing 5 words: `"python"`, `"coding"`, `"program"`, `"keyboard"`, `"display"`.
- **`HANGMAN_STAGES`**: A list of 7 multi-line strings representing the visual stages of the hangman.
- **`select_random_word()`**: Uses `random.choice()` to return a random string from `WORD_LIST`.
- **`display_game_state()`**: Prints the current hangman figure, the masked word, and remaining guesses.
- **`get_player_guess()`**: A `while` loop that forces the user to input a valid, unguessed letter.
- **`check_win()`**: An `if` statement loop that checks if all letters in the word are in the `guessed_letters` list.
- **`play_hangman()`**: The core function that ties all the above functions together into the game loop.
- **`main()`**: The entry point that allows the user to restart the game.

---

 📸 # Sample Output

```text
========================================
   🎮  HANGMAN GAME  🎮
========================================

Guess the word one letter at a time.
You can make up to 6 wrong guesses.
Good luck!



       ------
       |    |
       O    |
      /|    |
            |
            |
    ==========


Word: p _ _ _ _ _ 

Wrong guesses left: 4
Letters guessed: a, p, t
----------------------------------------

Guess a letter: 
```

---

 ❓# Troubleshooting

| Issue | Solution |
|-------|----------|
| `python is not recognized as an internal or external command` | Python is not added to your system PATH. Reinstall Python and ensure you **check the box** that says "Add Python to PATH". |
| `No module named random` | This should not happen as `random` is built into Python. Ensure your file is named `hangman.py` and not `random.py`. |
| `IndentationError: unexpected indent` | Python relies on strict spacing. Make sure you copied the code exactly without changing the spaces/tabs. |
| The game inputs multiple letters at once | The `get_player_guess()` function prevents this. If it happens, ensure you are running the latest version of the provided code. |

---

 📝 # License

This project is created strictly for educational purposes and learning fundamental Python programming.

---

 👨‍💻# Developed By

**Faisal Khalid**
CodeAlpha Internship
