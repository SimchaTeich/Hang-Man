# for input more then one letter but still alphabetic string
ERROR_1 = "E1"

# for one char than not alphabetic string
ERROR_2 = "E2"

# this is a combine of error 1 and error 2
ERROR_3 = "E3"

guessed_letter = input("Guess a letter: ").lower()

if len(guessed_letter) > 1 and guessed_letter.isalpha():
    print(ERROR_1)
elif len(guessed_letter) > 1:
    print(ERROR_3)
elif len(guessed_letter) == 1 and not guessed_letter.isalpha():
    print(ERROR_2)
else:
    print(guessed_letter)
