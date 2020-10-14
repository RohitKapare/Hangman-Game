# Assignment no. : 2 
# Rohit Anil Kapare (305A035)
# Title : Hangman Game
# Word file url : 
import random
import sys
import re
import string

wordToGuessList = list()
wordToGuess = ''
wordList = list()
difficulty = {'B': 4, 'I': 6, 'E': 8}
level = 'NotSelected'
fhand = ''
totalWords = 0
trials = 9

HANGMANPICS = ['''
    +-----+
    |     |
    O     |
          |
          |
          |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
    |     |
          |
          |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|     |
          |
          |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
          |
          |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
    |     |
          |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
    |     |
   /      |
          | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
    |     |
   /      |
  /       | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
    |     |
   / \    |
  /       | 
  =========
''','''
    +-----+
    |     |
    O     |
   \|/    |
    |     |
   / \    |
  /   \   | 
  =========
''']

def fileHandler(level):
    try:
        fhand = open('words.txt')
        wordList = list()
        wordToGuess = list()
        totalWords = 0
        for line in fhand:
            line = line.rstrip().upper()
            wordList.append(line)
        for word in wordList:
            if(len(word) == difficulty[level] and totalWords < 30):
                wordToGuess.append(word)
                totalWords += 1       
            if(totalWords == 30):
                break 
        return wordToGuess
    except:
        print('File cannot be opened : words.txt')
    finally:
        fhand.close()

def showHints(trials, wordToGuess):
    j = 0
    print("\nTotal TRIALS : ", trials, '\n')
    print('HINTS=>')
    for word in wordToGuess:
        if(j < 6):
            print(word, '| ', end = "")
            j +=1
        else: 
            print('\n', end = "")
            print(word, '| ', end = "")
            j = 1
    print("\n")       

def getRandomWord(wordToGuessList):
    wordIndex = random.randint(0, len(wordToGuessList) - 1)
    return wordToGuessList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, wordToGuess):
    print(HANGMANPICS[len(missedLetters)], '\n')
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(wordToGuess)
    
    for i in range(len(wordToGuess)):
        if wordToGuess[i] in correctLetters:
            blanks = blanks[:i] + wordToGuess[i] + blanks[i+1:]
        
    print("Correct Guesses: ========>{   ", end="")
    for letter in blanks:
        print(letter, end=' ')
    print("  }<========", end="")      
    print("\n\n|----------|----------|----------|----------|----------|----------|----------|----------|")
    
def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter : ')
        guess = guess.upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess
        
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().upper().startswith('Y')
    
def main():
    while True:
        # Print Welcome
        
        print('''
        #######################
        #      WELCOME TO     #
        #       HANGMAN       #
        #        GAME         #
        #######################
        
        Difficuilty Settings :
        -> Beginner(B)
        -> Intermediate(I)
        -> Expert(E)
        ''')
        
        # Set Difficuilty
        gameIsDone = False        
        while True:
            level = input("Type in Difficulty settings(B / I / E) : ")
            if(level.isalpha()):
                level = level.upper()
            if (level == 'B' or level == 'I' or level == 'E'):
                break
            else:
                print("Please choose option from : B / I / E ")
            
        # Show Hints
                
        wordToGuessList = fileHandler(level)
        showHints(trials, wordToGuessList)
        
        # Core game mechanics    
        
        missedLetters = ''
        correctLetters = ''        
        wordToGuess = getRandomWord(wordToGuessList)
        
        while True:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, wordToGuess)
                
            # User input
            guess = getGuess(missedLetters + correctLetters)
            
            if guess in wordToGuess:
                correctLetters = correctLetters + guess
                print("Missed Letters Type : ", type(missedLetters))
                # Check if the player has won
                foundAllLetters = True
                
                for i in range(len(wordToGuess)):
                    if wordToGuess[i] not in correctLetters:
                        foundAllLetters = False
                        break            
                if foundAllLetters:
                    displayBoard(HANGMANPICS, missedLetters, correctLetters, wordToGuess)
                    print('Yes! The secret word is "' + wordToGuess + '"! You have won!')
                    gameIsDone = True
                    
            else:
                missedLetters = missedLetters + guess        
            # Check if player has guessed too many times and lost
                if len(missedLetters) == len(HANGMANPICS) - 1:
                    displayBoard(HANGMANPICS, missedLetters, correctLetters, wordToGuess)
                    print("You have run out of guesses!\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses,' the word was " + wordToGuess + "")
                    gameIsDone = True
                    
            # Ask the player if they want to play again (but only if the game is done).
            if gameIsDone:
                break
        if playAgain():       
            gameIsDone = False
        else:
            print("Exited . . .")
            break
            
main()



"""
--------------[Output]--------------

        #######################
        #      WELCOME TO     #
        #       HANGMAN       #
        #        GAME         #
        #######################
        
        Difficuilty Settings :
        -> Beginner(B)
        -> Intermediate(I)
        -> Expert(E)
        
Type in Difficulty settings(B / I / E) : I

Total TRIALS :  9 

HINTS=>
SEARCH | ONLINE | PEOPLE | HEALTH | SHOULD | SYSTEM | 
POLICY | NUMBER | PLEASE | RIGHTS | PUBLIC | SCHOOL | 
REVIEW | UNITED | CENTER | TRAVEL | REPORT | MEMBER | 
BEFORE | HOTELS | OFFICE | DESIGN | POSTED | WITHIN | 
STATES | FAMILY | PRICES | SPORTS | COUNTY | ACCESS | 


    +-----+
    |     |
    O     |
          |
          |
          |
          | 
  =========
 

Missed letters: 
Correct Guesses: ========>{   _ _ _ _ _ _   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : A

    +-----+
    |     |
    O     |
    |     |
          |
          |
          | 
  =========
 

Missed letters: A 
Correct Guesses: ========>{   _ _ _ _ _ _   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : P

    +-----+
    |     |
    O     |
   \|     |
          |
          |
          | 
  =========
 

Missed letters: A P 
Correct Guesses: ========>{   _ _ _ _ _ _   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : R
Missed Letters Type :  <class 'str'>

    +-----+
    |     |
    O     |
   \|     |
          |
          |
          | 
  =========
 

Missed letters: A P 
Correct Guesses: ========>{   R _ _ _ _ _   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : W
Missed Letters Type :  <class 'str'>

    +-----+
    |     |
    O     |
   \|     |
          |
          |
          | 
  =========
 

Missed letters: A P 
Correct Guesses: ========>{   R _ _ _ _ W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : H

    +-----+
    |     |
    O     |
   \|/    |
          |
          |
          | 
  =========
 

Missed letters: A P H 
Correct Guesses: ========>{   R _ _ _ _ W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : T

    +-----+
    |     |
    O     |
   \|/    |
    |     |
          |
          | 
  =========
 

Missed letters: A P H T 
Correct Guesses: ========>{   R _ _ _ _ W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : E
Missed Letters Type :  <class 'str'>

    +-----+
    |     |
    O     |
   \|/    |
    |     |
          |
          | 
  =========
 

Missed letters: A P H T 
Correct Guesses: ========>{   R E _ _ E W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : V
Missed Letters Type :  <class 'str'>

    +-----+
    |     |
    O     |
   \|/    |
    |     |
          |
          | 
  =========
 

Missed letters: A P H T 
Correct Guesses: ========>{   R E V _ E W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Guess a letter : i
Missed Letters Type :  <class 'str'>

    +-----+
    |     |
    O     |
   \|/    |
    |     |
          |
          | 
  =========
 

Missed letters: A P H T 
Correct Guesses: ========>{   R E V I E W   }<========

|----------|----------|----------|----------|----------|----------|----------|----------|
Yes! The secret word is "REVIEW"! You have won!
Do you want to play again? (yes or no)
No
Exited . . .

"""

