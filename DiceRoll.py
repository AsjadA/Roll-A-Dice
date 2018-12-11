import random
def Roll(sides):
    number = random.randint(1,sides)
    print("You rolled " + str(number))

def RollDice():
    decision = input("Ready to roll? Enter Y or N: ")
    sides = int(input("Enter number of sides on dice: "))
    while decision == "Y":
        Roll(sides)
        decision = input("Roll Again? Enter Y or N: ")
    print("Thanks for playing")
    
#RollDice()