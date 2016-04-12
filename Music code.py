def HotCrossBun():
    print "Objective: Teach a friend the how to play Hot Cross Bun on the trmupet.\n\
You are in treble clef and the key signiture is in 4/4."
import random  #Importing for later
 
#Setting up variables to be called on later
life = 10
bank = ["edc edc dddd cccc edc", "edc edc dddd cccc edc"]
word = random.choice(bank)
 
letters_left = list(set(word)) #creating a list of letters in word
if ' ' in word:
    letters_left.remove(' ') #removing the space if there is one
             
 
user_guesses = [''] #More variables
wrong_answers = 0
hidden_phrase = []
foo = list(word) 
 
print ("You currently have 10 chances.")
 
while life > 0: 
     
    for letter in word:     #This is replacing every letter in the word with a pound symbol
        hidden_phrase = ()  #If the letter is guessed, it is replaced by the correct letter
        if letter in user_guesses:  #Else, it remains a hastag
            print letter,
        elif letter == ' ':
            print letter,
        else:
            print ('-'),
             
             
    current_guess = raw_input("Guess a note: ") # takes in raw input
    user_guesses.append(current_guess)
    if current_guess in word: #If guess in word, remove from letters_left
        letters_left.remove(current_guess)              
        #print letters_left
        
    print user_guesses #Prints guesses so far
    if current_guess not in word: #If you guess wrong, lose 
        life -= 1
        wrong_answers += 1
        print ("Oh, you have ") + str(life) + (" chances.")
     
     
    if len(letters_left) == 0:
        print word
        print 'Hot cross buns,\nHot cross buns,\nOne a penny,\nTwo a penny,\nHot cross buns.'
        print ("Mmm bunssssss!")
        break #Win if the letter_left has nothing in the list