HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
HANGMAN_PHOTOS = {
0:r"""
    x-------x""",
1:r"""
    x-------x
    |
    |
    |
    |
    |
    """,

2:r"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,

3:r"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,

4:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    """,

5:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    """,

6:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    """
}

def check_win(secret_word, old_letters_guessed):
    """
    function return True if player win.
    win is when all secret_word letters is 
    in the old_letters_guessed.
    """
    return '_' not in show_hidden_word(secret_word, old_letters_guessed)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    function return a pattern of the secret_word.
    Example: secret_word is "hangman" and old_letters_guessed
    is ['a', 'g'] so what return is "_ a _ g _ a _"
    """
    return " ".join(l if l in old_letters_guessed else '_' for l in secret_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    function return True if letter_guessed is valid.
    letter is valid if is one alphbetic char, and was
    not found in the old_letters_guessed.
    """
    letter_guessed = letter_guessed.lower()
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
            and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    function append new guess letter_guessed to list
    old_letters_guessed if guess is valid, and return True.
    else, print the old_letters_guessed and return False.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        if old_letters_guessed:
            print(" -> ".join(sorted(old_letters_guessed)))

    return False


def choose_word(file_path, index):
    """
    function extract a the secret word
    from file of word at file_path,
    and the correct place index by index.
    """
    words = []
    with open(file_path, "r") as f:
        words = f.read().split()

    num_of_diff_words = len(list(dict.fromkeys(words)))

    return num_of_diff_words, words[(index-1) % len(words)]


def print_hangman(num_of_tries):
    """
    function prints the hangman according
    to the level state by num_of_tries
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def print_open_screen():
    """
    function print the game start logo
    """
    print(HANGMAN_ASCII_ART + '\n' + str(MAX_TRIES))


def main():
    """
    This is the main function of game
    """
    print_open_screen()
    
    # init the game
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    old_letters_guessed = []
    secret_word = choose_word(file_path, index)[1]
    num_of_tries = 0
    
    # start game
    print()
    print("Let’s start!")
    print_hangman(num_of_tries)
    num_of_tries += 1
    print(show_hidden_word(secret_word, old_letters_guessed))
    
    # play while user does not lost the game or he wins
    while num_of_tries <= MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        
        # get some guess
        letter_guessed = input("Guess a letter: ").lower()
        
        # check for valid of the guess
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            
            # print the hangman if guess is valid but uncorrect
            if letter_guessed not in secret_word:
               print(":(")
               print_hangman(num_of_tries)
               num_of_tries += 1
            
            print(show_hidden_word(secret_word, old_letters_guessed))
    
    # final msg about win of the game
    print("WIN") if num_of_tries <= MAX_TRIES else print("LOSE")


if __name__ == "__main__":
    main()

