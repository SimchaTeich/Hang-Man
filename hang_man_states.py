from termcolor import colored

GREEN = "green"

HANGMAN_PHOTOS = {
0:r"""
    x-------x""",
1:r"""
    x-------x
    |
    |
    |
    |
    |""",

2:r"""
    x-------x
    |       |
    |       0
    |
    |
    |""",

3:r"""
    x-------x
    |       |
    |       0
    |       |
    |
    |""",

4:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |""",

5:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""",

6:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""}

def print_hangman(num_of_tries):
    print(colored(HANGMAN_PHOTOS[num_of_tries], GREEN))

print_hangman(6)

