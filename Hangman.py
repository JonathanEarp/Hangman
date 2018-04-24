import random

x = 1
wordlist = ["apple","pear","glasses","crow","orange"]

while x==1:
    print("welcome to Hangman!\n")
    print("|---------         \n")
    print("|        |         \n")
    print("|                  \n")
    print("|                  \n")
    print("|                  \n")
    print("|                  \n")
    print("|                  \n")
    print("|__________________\n")


    word = wordlist[random.randint(0,4)] #pulls a word out of the wordlist
    n = len(word) #The len function gets the number of items in a list or string

    print(n * " _ ") #Shows the user how many letters there are in the word
    print("\n")
    
    guess = str(input("Guess a letter:")) #define as string for index/count
    c = word.count(guess)
    guessword = [] #guessword stores lacation values of guessed letters
    j = 0 # variable to fill guessword
    
    for n in word: #trying to find multiple instances of guess in a string
        i = word.index(guess)
        guessword[j] = i
        j += 1
        word.remove(i)
    print(guessword)

    
        
    
