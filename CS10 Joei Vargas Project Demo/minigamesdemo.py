import random

def bundemo():
    print "Objective: Teach a friend the how to play Hot Cross Bun on the trmupet.\n\
    You are in treble clef and the key signiture is in 4/4."
    
 
    #Setting up variables to be called on later
    life = 5
    bank = ["edc edc dddd cccc edc", "edc edc dddd cccc edc"]
    word = random.choice(bank)
 
    letters_left = list(set(word)) #creating a list of letters in word
    if ' ' in word:
        letters_left.remove(' ') #removing the space if there is one
             
 
    user_guesses = [''] #More variables
    wrong_answers = 0
    #hidden_phrase = []
    #foo = list(word) 
 
    print ("You currently have 5 chances.")
 
    while life > 0: 
     
        for letter in word:     #This is replacing every letter in the word with a pound symbol
            #hidden_phrase = ()  #If the letter is guessed, it is replaced by the correct letter
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
        
        
#____________________________________________________________________________________
#Players get 10 guesses.
#They must guess a random number.
#It has to be a whole number from 1 to 10
#Tell them if they are too high or too low if they guess wrong
#Tell them how many guesses they have made

def pain():
    import random
    random_number = random.randint(1,10)
    tries = 0
    tries_remaining = 5
    while tries < 5:
        guess = input('Your patient is experiencing some pain. They won\'t tell you\
 unless you guess. Guess a number from 1-10 ')
        tries += 1
        tries_remaining -= 1
    
        try:
            guess_num = int(guess)
        except:
            print("Patient says: That's not a whole number! You suck!! ")
            break
        
        if not guess_num > 0 or not guess_num < 11:
            print("That number is not between 1 and 10. I\'m going to see someone else.")
            break
        
        
        elif guess_num == random_number:
            print("You\'re right Doc!")
            print("It took you {} tries. ".format(tries))
            break
        
        
        elif guess_num < random_number:
            if tries_remaining > 0:
                print("That number is low. You have {} tries..".format(int(tries_remaining)))
                continue
            else:
                print("It feels more like a {}".format(random_number))
                print("I\'m leaving.")
                break
        
        
        
        elif guess_num > random_number:
            if tries_remaining > 0:
                print("That number is too high Doc. You have {} more tries.".format(int(tries_remaining)))
                continue
            else:
                print("My number was {}".format(random_number))
                print("Bye.")
                break


#_____________________________________
def xy():
    print "hello"
    
#_____________________________________
def chipsdemo():
    import random
    random_number = random.randint(1,3)
    tries = 0
    tries_remaining = 2
    while tries < 2:
        guess = input('Pretzels, Lay\'s, or soda?')
        tries += 1
        tries_remaining -= 1
    
        try:
            guess_num = int(guess)
        except:
            print("That's not a whole number! You suck!! ")
            break
        
        if not guess_num > 0 or not guess_num < 11:
            print("That number is not between 1 and 3. ")
            break
        
        
        elif guess_num == random_number:
            print("You\'re right!")
            print("It took you {} tries. ".format(tries))
            break
        
        
        elif guess_num < random_number:
            if tries_remaining > 0:
                print("That number is low. You have {} tries..".format(int(tries_remaining)))
                continue
            else:
                print("I feel more like a {}".format(random_number))
                print("I\'m leaving.")
                break
        
        
        
        elif guess_num > random_number:
            if tries_remaining > 0:
                print("That number is too high. You have {} more tries.".format(int(tries_remaining)))
                continue
            else:
                print("My number was {}".format(random_number))
                print("Bye.")
                break
    