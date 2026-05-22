import random

lives = 9 
words = ["pizza", "fairy", "teeth" , "shirt", "otter", "plane", "horse", "table", "chair", "couch", "mouse", "house", "bread", "water", "plant", "light", "phone", "clock", "watch", "glass"]
secret_word = random.choice(words)
clue = []
index = 0 
while index < len(secret_word) : 
    clue.append("?")
    index = index + 1

heart_symbol = u'\u2764'
guessed_word_correctly = False 
unknown_letters = len(secret_word)

def update_clue(guessed_letter, secret_word, clue, unknown_letters) : 
    index = 0 
    while index < len(secret_word) : 
        if guessed_letter == secret_word[index] : 
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters

difficulty = input("Choose your difficulty level (type 1, 2 or 3):\n1. Easy (9 lives)\n2. Medium (6 lives)\n3. Hard (3 lives)\n")
difficulty = int(difficulty)

if difficulty == 1 : 
    lives = 9
elif difficulty == 2 :
    lives = 6
else :
    lives = 3

while lives > 0 : 
    print(clue)
    print("lives left: " + heart_symbol * lives)
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word :
        guessed_word_correctly = True 
        print("Congratulations! You guessed the word: " + secret_word)
        break
    
    if guess in secret_word :
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else :
        print("Incorrect, you lose a life")
        lives = lives - 1   
    
    if unknown_letters == 0: 
        guess_word_correctly = True
        print("Congratulations! You guessed the word: " + secret_word)
        break

    