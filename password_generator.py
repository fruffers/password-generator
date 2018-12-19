#password generator
#uses mix of lowercase, uppercase, numbers, and symbols
#based off http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#passwords are random
#generates a new password each time the user asks for one
#choice between a strong or weak password
#weak password picks a word or 2 from a list

import random, time, string

def greeting():
    print("Welcome to the password generator.")
    password_type = input("Do you want a strong or weak password? Type 1 for weak, 2 for strong: ")

    return password_type

def choosing_strength(password_type):
    if password_type == "1":
        weak_pass()
    else:
        strong_pass()

def weak_pass():
    dictionary = [
        "chandler",
        "telethermometer",
        "pithoi",
        "unsought",
        "treenware",
        "calcined",
        "convert",
        "laddie",
        "concorporated",
        "patripassianist",
        "effigy",
        "imbruted",
        "cairngorm",
        "emblematist",
        "malaceous",
        "nonaddict",
        "humidity",
        "prelibation",
        "duologue",
        "inflator"
        ]

    dictionary_len = len(dictionary)
    rand_index = random.randint(0, dictionary_len)

    word = dictionary[rand_index]
    word2 = dictionary[rand_index]

    while word2 == word:
        rand_index = random.randint(0, dictionary_len)
        word2 = dictionary[rand_index]

    str(word)
    str(word2)

    password = word + word2

    print("Your weak password is: ")
    print("\n" + password)

def strong_pass():
    symbols = '!"£$%^&*()_+{}[]@~#/?,.¬`|<>\='
    password = ''.join(random.choice(string.ascii_letters + string.digits + symbols) for ele in range(12))

    print("Your strong password is: ")
    print("\n" + password)

def go_again():
    choice = input("\nWould you like to go again? y/n: ")
    if choice == "y":
        password_type = greeting()
        choosing_strength(password_type)
        go_again()
    else:
        exit()


#main loop
password_type = greeting()
choosing_strength(password_type)
go_again()
