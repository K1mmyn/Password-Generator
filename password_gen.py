import random
import string
from simple_colors import *

letters = list(string.ascii_letters)
special_letters = ["!", '@', "#", "$", "%", "^", "&", '*', "(", ")", "-", "_", "+", "=", '{', "}", "[", "]", ":", ";", "'", '"', '<', ">", "?", "/", "|", "\\", ",", "."]
passwordlist = []
H = 0
ask = int(input("\nMininum Numbers: "))
ask2 = int(input("\nMininum Speical Letters: "))
how_many = int(input("\nPassword Length: "))

x = ask + 2
y = ask2 + 2

for number in range(0, x):
    passwordlist += str(random.randint(0, 10))
    H += 1

for number in range(0, y):
    passwordlist += random.choice(special_letters)
    H += 1

ask3 = how_many - H
z = ask3 + 1

for number in range(z):
    passwordlist += random.choice(letters)

random.shuffle(passwordlist)
password = ("".join(passwordlist))
print(f"\nYour Randomly generated password is: {password} \n")
