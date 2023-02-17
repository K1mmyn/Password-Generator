import random
import string
from simple_colors import *

letters = list(string.ascii_letters)
special_letters = ["!", '@', "#", "$", "%", "^", "&", '*', "(", ")", "-", "_", "+", "=", '{', "}", "[", "]", ":", ";", "'", '"', '<', ">", "?", "/", "|", "\\", ",", "."]
passwordlist = []
H = 0
while True:
    ask = int(input("\nMininum Numbers: "))
    ask2 = int(input("Mininum Speical Letters: "))
    how_many = int(input("Password Length: "))
    while True:
        if ask + ask2 >= how_many:
            print(red("\nPlease enter a lower amount of number or speical letters ", 'bold'))
            break

        for number in range(random.randint(ask, (ask + 2))):
            passwordlist += str(random.randint(0, 10)); H += 1

        for number in range(random.randint(ask, (ask + 2))):
            passwordlist += random.choice(special_letters); H += 1

        ask3 = how_many - H; z = ask3 + 1

        for number in range(z):
            passwordlist += random.choice(letters)

        random.shuffle(passwordlist)
        password = ("".join(passwordlist))
        print(f"\nYour Randomly generated password is: {password} \n"); quit()
