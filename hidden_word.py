def show_hidden_word(secret_word, old_letters_guessed):
    return " ".join(l if l in old_letters_guessed else '_' for l in secret_word)

