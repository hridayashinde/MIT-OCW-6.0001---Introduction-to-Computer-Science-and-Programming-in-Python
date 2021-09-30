# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:42:33 2020

@author: Hridaya
"""
# Problem Set 2, hangman.py
# Name: Hridaya Shinde
# Collaborators: -
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random



WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    
    
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    res=""
    for b in secret_word:
        if b not in res:
            res=res+b
            
            
    l=len(res)      
    count=0     
            
    for a in letters_guessed:
        if a in res:
            count +=1
        
    if count==l:
        return True
    else:
        return False
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_so_far=""
    for a in secret_word:
        if a in letters_guessed:
            guessed_so_far=guessed_so_far+a+" "
        else :
            guessed_so_far=guessed_so_far+"_"+" "
    return guessed_so_far



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s=string.ascii_lowercase
    not_been_guessed=""
    
    for a in letters_guessed:
        if a in s:
            ind=s.index(a)
            s=s[0:ind]+s[ind+1:]
    return s
        




def hangman(secret_word):
    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print("Welcome to the game of Hangman!")
    
    lenght=len(secret_word)
    print("I am thinking of a word that is ",lenght," long.")
    print("_______________________")
    num_guess=6
    letters_guessed=[]
    vowels="aeiou"
    warn=3
    s=string.ascii_letters

    while not is_word_guessed(secret_word,letters_guessed) and num_guess>=0 and warn>=0:
        print("_________________________________________")
        print("                                          ")
        print("you have",num_guess," guesses left")
        print("Available letters:",get_available_letters(letters_guessed))
        a=str(input("Please guess a letter: "))
        
        if a not in s:
            warn -=1
            print("Oops! This is not a valid letter. You have",warn," warnings left:",get_guessed_word(secret_word,letters_guessed))
        else:
            
            a=a.lower()
        
            if a in letters_guessed:
                warn -=1
                print("Oops! you have already guessed that letter.You have",warn,"warning left:")
                print(get_guessed_word(secret_word,letters_guessed))
            elif a in secret_word:
                letters_guessed.append(a)
                
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                
            elif a in vowels:
                print("Oops! That letter is not in my word")
                letters_guessed.append(a)
                print(get_guessed_word(secret_word,letters_guessed))
                num_guess=num_guess-2
            
            else:
                print("Oops! That letter is not in my word")
                letters_guessed.append(a)
                print(get_guessed_word(secret_word,letters_guessed))
                num_guess=num_guess-1
                
                
                
            if warn==0:
                num_guess -=1
            if num_guess==0 or warn<0:
                print("You have lost the game")
                print("The word you were guessing was:",secret_word)
                break
            print("                                                ")
            
        
    if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations, you won!")
        score=num_guess*lenght
        print("your total score for the game is:",score)





secret_word=choose_word(wordlist)
hangman(secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
