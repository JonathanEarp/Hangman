import random

x = 1
wordlist = ["apple","pear","glasses","crow","orange"]

def list_duplicates_of(seq,item): #if a letter has multiple instances in a word
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

while x==1: #main loop
    print("welcome to Hangman!\n")
    print("|---------         \n")
    print("|        |         \n")
    print("|        0         \n")
    print("|       -|-        \n")
    print("|       / \        \n")
    print("|                  \n")
    print("|                  \n")
    print("|__________________\n")


    word = wordlist[random.randint(0,4)] #pulls a word out of the wordlist
    n = len(word) #The len function gets the number of items in a list or string
    answer = [' _ '] *n
    score = 6

    print(answer) #Shows the user how many letters there are in the word
    print("\n")

    y = 1
    while y==1: #guess loop
        guess = str(input("Guess a letter:")) #define as string for index/count
        
        location_of_guessed_letters = list_duplicates_of(word,guess)
        i = 0
        if location_of_guessed_letters == []: #if guess is not in word
            print(guess + " is not in the word, try again\n")
            score -= 1
            if score <= 0:
                print("You lose!")
                break
            else:
                continue
        else: #if guess is in word
            for letter in location_of_guessed_letters:
                specific_location = location_of_guessed_letters[i]
                answer.remove(' _ ')
                answer.insert(specific_location, guess)
                i+=1
            answer_word = "".join(answer)
            print(answer_word)
            if answer_word == word:
                print("you win")
                break
            continue
        
                
                
    

    
        
    
