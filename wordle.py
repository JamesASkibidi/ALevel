from colorama import Fore

import requests

import time

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
incorrect_position = []
correct_position = []
not_present = []
word_letters = ''

def letter_checker(word , guess, correct , word_letters):
    
        
    for i in range (5):
        
        output = ''
        
        if guess[i] in word and guess[i] == word[i]:
            #letter in correct position
            print(Fore.GREEN , guess[i], end = "")
            if guess[i] not in correct_position:
                correct_position.append(guess[i])
            elif guess[i] in letters:
                letters.remove(guess[i])
                word_letters[i] = '1'
            elif guess[i] in incorrect_position:
                incorrect_position.remove(guess[i])
                
                
        elif guess[i] in word and guess[i] != word[i]:
            #letter in word
            if guess[i] not in correct_position and guess[i] == word_letters[i]:
                print(Fore.YELLOW , guess[i], end = "")
            else:
                print(Fore.WHITE , guess[i], end = "")
            if guess[i] not in incorrect_position:
                incorrect_position.append(Fore.YELLOW + guess[i])
            elif guess[i] in letters:
                letters.remove(guess[i])
                
                
            
            
        else:
            #letter not in word
            print(Fore.RED , guess[i] , end = "")
            if guess[i] not in not_present:
                not_present.append(guess[i])
            elif guess[i] in letters:
                letters.remove(guess[i])
    
        
    print("")
    return correct and word_letters
        
        
        
correct = False
guessno = 0
word = requests.get(f"https://random-word-api.vercel.app/api?words=1&length=5")

if word.status_code == 200:
    word = str(*word.json())
    
# print(word)

# word = 'apple'

word_letters = word

while guessno < 6 and correct == False:
    
    guess =''
    
    while len(guess) != 5:

        guess = input(Fore.WHITE , )
        
        if len(guess) != 5:
            print('word is invalid')
            
   
    
    guessno = guessno + 1
    
    time.sleep(1)
    
    if guess == word:
        correct = True
        for i in range (5):
            print(Fore.GREEN , guess[i], end = "")
        print("")
        break
        
    
    letter_checker(word , guess, correct , word_letters)

if correct == True:
    
    print('You Won!')
    print(guessno , 'guesses')
    
elif correct == False:
    print('You Failed')
    print('The word was' , word)


