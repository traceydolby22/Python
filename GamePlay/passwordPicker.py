import random
import string

adjectives = ["Happy", "Sad", "Angry", "Excited", "Bored", "Tired", "Confused", "Nervous", "Brave", "Shy"]
nouns = ["Cat", "Dog", "Fish", "Bird", "Mouse", "Hamster", "Rabbit", "Turtle", "Snake", "Frog"]

print("Welcome to the Password Picker!")
while True: 
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char 
    print("your new pasword is : %s" % password)
    response = input(" Do you want anothr passoword? Type y or n: ")
    if response == "n" : 
        break 
