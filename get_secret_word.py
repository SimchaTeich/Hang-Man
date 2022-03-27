def choose_word(file_path, index):
    words = []
    with open(file_path, "r") as f:
        words = f.read().split()

    num_of_diff_words = len(list(dict.fromkeys(words)))

    return num_of_diff_words, words[(index-1) % len(words)]

