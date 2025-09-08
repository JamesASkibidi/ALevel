from colorama import Fore

import requests

import time

def letter_checker(word , guess, correct):
    
    for i in range (5):
        
        output = ''
        
        if guess[i] in word and guess[i] == word[i]:
            #letter in correct position
            print(Fore.GREEN , guess[i], end = "")
        elif guess[i] in word and guess[i] != word[i]:
            #letter in word
            print(Fore.YELLOW , guess[i], end = "")
            
        else:
            #letter not in word
            print(Fore.RED , guess[i] , end = "")
    
        
    print("")
    return correct
        
        
        
correct = False
guessno = 0
word = requests.get(f"https://random-word-api.vercel.app/api?words=1&length=5")

if word.status_code == 200:
    word = str(*word.json())
    
# print(word)

while guessno < 6 and correct == False:

    guess = input()
    guessno = guessno + 1
    
    time.sleep(2)
    
    if guess == word:
        correct = True
        for i in range (5):
            print(Fore.GREEN , guess[i], end = "")
        print("")
        break
        
    
    letter_checker(word , guess, correct)

if correct == True:
    
    print('You Won!')
    print(guessno , 'guesses')
    
elif correct == False:
    print('You Failed')
    print('The word was' , word)
    
