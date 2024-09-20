import random

def load_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
        words = [word.strip() for word in words]
        return words
    except FileNotFoundError:
        return ['python', 'django', 'hangman', 'developer', 'ai', 'intelligence', 'programming']

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = load_words('words.txt')
    
    while True:
        word = choose_word(words).lower()
        guessed_letters = []
        incorrect_guesses = 0
        max_incorrect_guesses = 6
        
        print("\nWelcome to Hangman Game!")
        print("The word has", len(word), "letters.")
        
        while incorrect_guesses < max_incorrect_guesses:
            print("\nWord:", display_word(word, guessed_letters))
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
            
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                print(f"Good guess! '{guess}' is in the word.")
                guessed_letters.append(guess)
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                guessed_letters.append(guess)
                incorrect_guesses += 1
            
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the correct word:", word)
                break
        
        else:
            if incorrect_guesses == max_incorrect_guesses:
                print("\nYou've run out of guesses. The word was:", word)
        
        play_again = input("\nDo you want to guess a new word? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing Hangman!")
            break

hangman()
