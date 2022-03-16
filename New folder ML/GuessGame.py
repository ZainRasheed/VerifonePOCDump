# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:53:40 2020

@author: MohammedS2
"""
import time
import random

name = ''
randValue = 0
chances = 3
userValue = 0
retry = True
won = False


def theGuessGame():
    global retry
    init()
    while(retry):
        guessLogic()
        retry =  playAgain()
        resetVars()
        test()
    
def rest():
    time.sleep(1)

def init():
    print("Enter you name Player!!")
    initVars(input("Name: "), random.randrange(11))
    rest()
    bitArt()
    rest()   
    print("\nWelcome to the game "+name)    
    
def bitArt():
    print("  ___  __  __  ____  ___  ___     ___    __    __  __  ____ ")
    print(" / __)(  )(  )( ___)/ __)/ __)   / __)  /__\  (  \/  )( ___)")
    print("( (_-. )(__)(  )__) \__ \\__ \  ( (_-. /(__)\  )    (  )__) ")
    print(" \___/(______)(____)(___/(___/   \___/(__)(__)(_/\/\_)(____)")

def resetVars():
    global randValue
    global chances
    global userValue
    global won
    randValue = 0
    chances = 3
    userValue = 0
    won = False
    
def initVars(_name, _randValue):
    global name
    global randValue
    name = _name
    randValue = _randValue

def guessLogic():
    intro()
    guessSequence()
    outro()
 
def intro():
    print("\nLet's begin " + name)
    rest()
    print("Can you correctly guess the number that I selected? (!_!)")
    print("It is one among 0 to 10")
    rest()
    rest()
    rest()
    print("Let me give you 3 chances B-)")

def guessSequence():
    global userValue
    global chances
    while(won == False and chances >= 0): 
        print("\nChances "+str(chances))
        userValue = input("Guess the number: ")
        chances = chances - 1
        evaluatePlayer()

def evaluatePlayer():
    #global userValue
    #global randValue
    global won
    if(int(userValue) == randValue):
        print("Congratulations "+name+" you guessed it righttt!!! (*o*)")
        won = True
    elif(int(userValue) > randValue):
        print("MmmHmm... "+name+" you guessed a higher value, try again")
    elif(int(userValue) < randValue):
        print("OooHooo... "+name+" you guessed a lower value, try again")
  
def outro():
    if(not(won)):
        rest()
        print("Oh Dammit!")
        print("The correct answer was "+str(randValue))
        

def playAgain():
    answer = ''
    rest()
    rest()
    while(answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
        print("\nwanna play again? xD")
        answer = input("(Y/N):")
        if(answer == 'y' or answer == 'Y'):
            return True
        return False

def test():
    print(">>>>> THIS IS TEST")
    print(name, randValue)
        
theGuessGame()