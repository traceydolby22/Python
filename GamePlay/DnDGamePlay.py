direction = input("""Your name is Saraphena. You are a trained killer, you've been taken by the Primal of Death,  
                  You are on your way back to your room after breakfast, as you pass his study, you see the door ajar, do you go in or keep walking?
                  Type 'Go in' or 'Keep walking':        
                  """)
#enter_study()
#keep_walking()

def enter_study():
    if direction == "Go in":
        print("You slowly peek inside, and see noone is inside. You see a book on the table, do you read it or leave it alone? Type 'read' or 'leave'")
        action = input()
        if action == "read":
            print("You read the ledger and see that it's an account of names, names that written in his handwriting, you see your brother's name on the liset and smile ")
        elif action == "leave":
            print("You went back to your room only to grow bored, so you go to the balcony and look down at the courtyard, you see the Primal training with his men, do you go down and join? Type 'yes' or 'no'")
        else:
            print("Not a valid option. Try again.")
def keep_walking() :
    if direction == "Keep walking":
        print("You went back to your room only to grow bored, so you go to the balcony and look down at the courtyard, you see the Primal training with his men, do you go down and join? Type 'yes' or 'no'")
        action = input()
        if action == "yes":
            print("""You clammor down the balcony and demand to join the training, the primal looks at you and says 
                  'no', you insist and look for a weapon, do you take it from the weapon rack or do you take it from his hand? Type 'rack' or 'hand'""")
        elif action == "no":
            print("""You decide to go to the library to read some books, you find a book on the history of the primal, 
                  do you read it or leave it alone? Type 'read' or 'leave'""")
        else:
            print("Not a valid option. Try again.") 