def is_valid_input(letter_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha()

print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input('ab'))
print(is_valid_input('app$'))
