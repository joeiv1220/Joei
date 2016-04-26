#Setting up variables to be called on later
import random
life = 5
bank = ["illuminati confirmed", "slenderman", "guess", "password", "luigi", "king boo", "kevin", "caaaaaarl", "john cena"]
word = random.choice(bank)
 
letters_left = list(set(word)) #creating a list of letters in word
if ' ' in word:
    letters_left.remove(' ') #removing the space if there is one
             
 
user_guesses = [] #More variables
wrong_answers = 0
hidden_phrase = []
foo = list(word) 
 
print ("You currently have 5 lives. Try not to waste them.")
 
while life > 0: #The dreaded while loop
     
 
 
    for letter in word:     #This is replacing every letter in the word with a pound symbol
        hidden_phrase = []  #If the letter is guessed, it is replaced by the correct letter
        if letter in user_guesses:  #Else, it remains a hastag
            print letter,
        elif letter == ' ':
            print letter,
        else:
            print ('#'),
             
             
    current_guess = raw_input("Guess a letter: ") #This takes in raw input
    user_guesses.append(current_guess)
    if current_guess in word: #If guess in word, remove from letters_left
        letters_left.remove(current_guess)              
        #print letters_left
    print user_guesses #Prints guesses so far
    if current_guess not in word: #If you guess wrong, lose life energy
        life -= 1
        wrong_answers += 1
        print ("Oh, how sad. Lost a life. You have ") + str(life) + (" lives.")
     
 
 
     
             
    if len(letters_left) == 0:
        print ("You've won! Don't you feel proud to actually accomplish something?")
        break #Win if the letter_left has nothing in the list