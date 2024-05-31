"""
Aurelio Amparo
MyUtilities
"""
import random
import os

def diceRoll(times,sides):           
    total = 0
    for i in range(times):                  #This function takes the amount of times you want to roll and how many sides the die should be.             
        roll = random.randint(1,sides)      #for example a diceRoll(1,6) will roll once witha 6 sided dice and add that number to the total value.
        total += roll                       
    return total                            # then returns total (what you rolled)


 

def targetRoll(times,sides,target):
    outcome = 0                             #This function requires a targetnumber, number of sides of die, and how many times you roll
    for i in range(times):                  #for the amount of times you roll it will roll a die that has input sides
        rollDice = random.randint(1,sides)
        if rollDice >= target:              #then it compares the number you rolled to the target number
            outcome += 1                    # if it hits target # or higher it will store it in outcome
    return outcome
   
def ClearScreen():
    #windows
    if os.name == 'nt':                     
        os.system('cls')
    #mac and linux
    else:
        os.system('clear')

