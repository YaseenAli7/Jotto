"""
Author: Yaseen Ali, ali166@purdue.edu
Date: 04/19/2022

Description:
    This program replicates a precursor to the game Wordle, called "Jotto"
"""
import random

def getInput():

    print("\n----- Main Menu -----\n1. New Game\n2. See Hall of Fame\n3. Quit\n")
    inputVal = input("What would you like to do? ")

    while (not inputVal.isnumeric() or not (0 < int(inputVal) < 4)): # only accepts input of integers 1, 2, or 3
        print("\nInvalid choice. Please try again.\n")
        print("----- Main Menu -----\n1. New Game\n2. See Hall of Fame\n3. Quit\n")
        inputVal = input("What would you like to do? ")
    return int(inputVal)

def pick_game_words(lines): # creates a list of three words that are read in from the words.txt file
    wordList = []
    three = [1, 2, 3]

    for i in three:
        word = random.choice(lines)
        wordList.append(word)

    return(wordList)

def showHighScores(): # formatted output of the high score table 
    print("\n--- Hall of Fame ---\n ## : Score : Player")
    for index, (score, name) in enumerate(zip(highScoreList, highScoreNames)):
        print(f" {index + 1: >2d} :    {score:2d} : {name}")

def playGame():
    global highScoreList
    global highScoreNames

    name = str(input("Enter your player name: "))
    guessList = [1, 2, 3, 4, 5, 6]
    rounds = [1, 2, 3]
    words = ['Impossible', 'Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
    totalPoints = 0 # Total number of points acquired by the user in a game of 3 rounds

    text = open('words.txt', 'r') # opens text file and reads it
    lines = text.readlines() # assigns variable to thecontent of the file
    lines = list(map(str, lines))
    text.close()

    wordsToGuess = pick_game_words(lines)
    x = 0 # The number of rounds

    for i in wordsToGuess: # chooses a word for each round and is responsible for iterating through each round
        print(f"\nRound {rounds[x]}:")
        word = i
        letter_dict = {}
        for i in range(26):
                letter_dict[chr(i + 97)] = ' '

        for j in guessList: # responsible for iterating through each user's guess, as well as all features of the game within each round
            guess = input(f"{j}? ")
            guess = guess.lower()
            while (guess.isalpha() != True or len(guess) > 5 or len(guess) < 5):
                if (len(guess) > 5 or len(guess) < 5):
                    print("\nInvalid guess. Please enter exactly 5 characters.\n")
                elif (guess.isalpha() != True):
                    print("\nInvalid guess. Please only enter letters.\n")
                guess = input(f"{j}? ")
                guess = guess.lower()

            inWord = ''
    
            for i in range(len(guess)): # responsible for adding indicators as to whether the guessed letters are in the word, in the correct spots, or not
                if guess[i] in word[i]: 
                    inWord += "!"
                    letter_dict[guess[i]] = "!"
                elif guess[i] in word and letter_dict[guess[i]] != "!": 
                    letter_dict[guess[i]] = "?"
                    inWord += "?"
                elif letter_dict[guess[i]] != "!" and guess[i] not in word:
                    letter_dict[guess[i]] = "X"
                    inWord += 'X'              
            letter_str = ""
            for i in range(26):
                if chr(i + 97) in letter_dict.keys():
                    letter_str += letter_dict[chr(i + 97)]
                else:
                    letter_str += " "
            print(f"   {inWord}     {letter_str}")
            print(f"   {guess}     abcdefghijklmnopqrstuvwxyz")
            if inWord == "!!!!!":
                points = 2 ** (6-j)
                totalPoints += points
                print(f"{words[j]}! You earned {points} points this round.")  
                break           
        if inWord != "!!!!!":
            print(f"You ran out of tries.\nThe word was {word}.")
        x = x+1

    print(f"\nWay to go {name}!\nYou earned a total of {totalPoints} points and made it into the Hall of Fame!\n")

    if len(highScoreList) > 10: # responsible for appending the highscore list and properly arranging it
        indexOf = highScoreList.index(min(highScoreList))
        for i in highScoreList:
            if totalPoints > i:
                highScoreList.pop(indexOf)
                highScoreNames.pop(indexOf)
                highScoreList.append(totalPoints)
                highScoreNames.append(name)
        
        
    highScoreList.append(totalPoints)
    highScoreNames.append(name)
    highScoreList, highScoreNames = (list(t) for t in zip(*sorted(zip(highScoreList, highScoreNames), reverse=True)))
        
    print("--- Hall of Fame ---\n ## : Score : Player")
    for index, (score, name) in enumerate(zip(highScoreList, highScoreNames)):
        print(f" {index + 1: >2d} :    {score:2d} : {name}")
    return (totalPoints, name)


def main():
    print("Welcome to PyWord.")
    global highScoreList
    global highScoreNames

    highScoreList = []
    highScoreNames = []

    with open('hall_of_fame.txt', "r") as f:
        for line in f:
            data = line.rstrip("\n").split(",")
            highScoreList.append(int(data[0]))
            highScoreNames.append(data[1][1:])

    totalPoints = 0
    name = 0

    while (input := getInput()) != 3:
        if int(input) == 1: 
            totalPoints, name = playGame() 

        if int(input) == 2:
            showHighScores()

    
    print("Goodbye.")
    if name != 0:
        with open("hall_of_fame.txt", 'a') as text:
            text.write(f'{totalPoints}, {name:<}\n')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
