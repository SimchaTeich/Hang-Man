secret_word = input("Please enter a word: ").lower()
word_pattern = "_ " * len(secret_word)

# delete the last space
word_pattern = word_pattern[:-1]

print(word_pattern)
