def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
            and letter_guessed not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        print(" -> ".join(sorted(old_letters_guessed)))

    return False

old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(old_letters)
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
print(old_letters)
