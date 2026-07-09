import random

# ============================================
# HANGMAN GAME
# ============================================

WORD_LIST = ["python", "coding", "program", "keyboard", "display"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]


def select_random_word():
    return random.choice(WORD_LIST)


def display_game_state(word, guessed_letters, wrong_guesses):
    print("\n" * 2)
    print(HANGMAN_STAGES[wrong_guesses])
    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"\nWord: {display}")
    print(f"\nWrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
    
    if guessed_letters:
        print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")
    
    print("-" * 40)


def get_player_guess(guessed_letters):
    while True:
        guess = input("\nGuess a letter: ").strip().lower()
        
        if guess == "":
            print("Please enter a letter!")
            continue
        
        if len(guess) != 1:
            print("Please enter only ONE letter!")
            continue
        
        if not guess.isalpha():
            print("Please enter a valid letter (a-z)!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue
        
        return guess


def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play_again():
    while True:
        choice = input("\nPlay again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y', 'no', 'n']:
            return choice in ['yes', 'y']
        print("Please enter 'yes' or 'no'!")


def play_hangman():
    print("=" * 40)
    print("   HANGMAN GAME")
    print("=" * 40)
    print("\nGuess the word one letter at a time.")
    print(f"You can make {MAX_WRONG_GUESSES} wrong guesses.")
    
    word = select_random_word()
    guessed_letters = []
    wrong_guesses = 0
    
    while wrong_guesses < MAX_WRONG_GUESSES:
        display_game_state(word, guessed_letters, wrong_guesses)
        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"\nCorrect! '{guess}' is in the word!")
            if check_win(word, guessed_letters):
                display_game_state(word, guessed_letters, wrong_guesses)
                print("\n" + "=" * 40)
                print("   CONGRATULATIONS!")
                print(f"   Word was: {word.upper()}")
                print("=" * 40)
                return True
        else:
            print(f"\nWrong! '{guess}' is not in the word.")
            wrong_guesses += 1
    
    display_game_state(word, guessed_letters, wrong_guesses)
    print("\n" + "=" * 40)
    print("   GAME OVER")
    print(f"   Word was: {word.upper()}")
    print("=" * 40)
    return False


def main():
    while True:
        play_hangman()
        if not play_again():
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()