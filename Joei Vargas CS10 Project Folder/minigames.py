#MINIGAMES
import random

def bun():
    print "Objective: Teach a friend the how to play Hot Cross Bun on the trmupet.\n\
    You are in treble clef and the key signiture is in 4/4."
    
 
    #Setting  up variables to be called on later
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
'''
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
'''

#_____________________________________

 
#_____________________________________
# Tic Tac Toe
def tic():


    X = "X"
    O = "O"
    EMPTY = " "
    TIE = "TIE"
    NUM_SQUARES = 9
    
    
    def display_instruct():
        """Display game instructions."""  
        print(
        """
        The fridge is yucky.  
    
        You will move the items by entering a number, 0 - 8.  The number 
        will correspond to the fridge position as illustrated:
    
                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
    
        Prepare yourself. Input 'n' or 'y' to start the game\n
        """
        )
    
    
    def ask_yes_no(question):
        """Ask a yes or no question."""
        response = None
        while response not in ('y', 'n'):
            response = input(question).lower()
        return response
    
    
    def ask_number(question, low, high):
        """Ask for a number within a range."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response
    
    
    def pieces():
        """Determine if player or computer goes first."""
        go_first = ask_yes_no("Do you require the first move? (y/n): ")
        if go_first == "y":
            print("\nThen take the first move.  You will need it.")
            human = X
            computer = O
        else:
            print("\n I\'ll help you out.")
            computer = X
            human = O
        return computer, human
    
    
    def new_board():
        """Create new game board."""
        board = []
        for square in range(NUM_SQUARES):
            board.append(EMPTY)
        return board
    
    
    
    def display_board(board):
        """Display game board on screen."""
        print"", board[0], ' |', board[1], '|', board[2]
        print"--------------"
        print "",board[3], ' |', board[4], '|', board[5]
        print"--------------"
        print"",board[6], ' |', board[7], '|', board[8]
        print" ",    '0 | 1 | 2'
        print" ",    '---------'
        print" ",    '3 | 4 | 5'
        print" ",    '---------'
        print" ",    '6 | 7 | 8'
    def legal_moves(board):
        """Create list of legal moves."""
        moves = []
        for square in range(NUM_SQUARES):
            if board[square] == EMPTY:
                moves.append(square)
        return moves
    
    
    def winner(board):
        """Determine the game winner."""
        WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    
        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner
    
        if EMPTY not in board:
            return TIE
    
        return None
    
    
    def human_move(board, human):
        """Get human move."""  
        legal = legal_moves(board)
        move = None
        while move not in legal:
            move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
            if move not in legal:
                print("\nThat square is already occupied. Choose another.\n")
        print("Fine...")
        return move
    
    
    def computer_move(board, computer, human):
        """Make computer move."""
        # make a copy to work with since function will be changing list
        board = board[:]
        # the best positions to have, in order
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    
    
    
        # if computer can win, take that move
        for move in legal_moves(board):
            board[move] = computer
            if winner(board) == computer:
                print(move)
                return move
            # done checking this move, undo it
            board[move] = EMPTY
    
        # if human can win, block that move
        for move in legal_moves(board):
            board[move] = human
            if winner(board) == human:
                print(move)
                return move
            # done checkin this move, undo it
            board[move] = EMPTY
    
        # since no one can win on next move, pick best open square
        for move in BEST_MOVES:
            if move in legal_moves(board):
                print(move)
                return move
    
    
    def next_turn(turn):
        """Switch turns."""
        if turn == X:
            return O
        else:
            return X
    
    
    def congrat_winner(the_winner, computer, human):
        """Congratulate the winner."""
        if the_winner != TIE:
            print(the_winner, "Nice!")
        else:
            print("We did it!")
    
        if the_winner == computer:
            print("As I predicted, I know fridges more than you.  \n" \
                "Proof that computers are superior to humans in all regards.")
    
        elif the_winner == human:
            print("No, no! It cannot be! Somehow you organized faster than me, human. \n" \
                "But never again! I, the computer, so swear it!")
    
        elif the_winner == TIE:
            print("You were most lucky, human, and somehow we worked together  \n" \
                "Celebrate today... for this is the best we will ever achieve.")
    
    
    def main():
        display_instruct()
        computer, human = pieces()
        turn = X
        board = new_board()
        display_board(board)
    
        while not winner(board):
            if turn == human:
                move = human_move(board, human)
                board[move] = human
            else:
                move = computer_move(board, computer, human)
                board[move] = computer
            display_board(board)
            turn = next_turn(turn)
    
        the_winner = winner(board)
        congrat_winner(the_winner, computer, human)
    
    
    # start the program
    main()
    input("\n\nPress the enter key.")
#_____________________________________

def ab():
    print "Laundry is all over the place. Hurry to get to school."
    
 
    #Setting  up variables to be called on later
    life = 15
    bank = ["shirt", "pants", "sweater", "tank", "socks"]
    word = random.choice(bank)
 
    letters_left = list(set(word)) #creating a list of letters in word
    if ' ' in word:
        letters_left.remove(' ') #removing the space if there is one
             
 
    user_guesses = [''] #More variables
    wrong_answers = 0
    #hidden_phrase = []
    #foo = list(word) 
 
    print ("You currently have 15 chances.")
 
    while life > 0: 
     
        for letter in word:     #This is replacing every letter in the word with a pound symbol
            #hidden_phrase = ()  #If the letter is guessed, it is replaced by the correct letter
            if letter in user_guesses:  #Else, it remains a hastag
                print letter,
            elif letter == ' ':
                print letter,
            else:
                print ('-'),
             
             
        current_guess = raw_input("What do I need today? ") # takes in raw input
        user_guesses.append(current_guess)
        if current_guess in word: #If guess in word, remove from letters_left
            letters_left.remove(current_guess)              
        #print letters_left
       
        print user_guesses #Prints guesses so far
        if current_guess not in word: #If you guess wrong, lose 
            life -= 1
            wrong_answers += 1
            print ("Time\'s flushing away. Only ") + str(life) + (" chances.")
     
     
        if len(letters_left) == 0:
            print word
            print 'Time to get to school.'
            break #Win if the letter_left has nothing in the list
        
    

#_____________________________________
def chips():
    import random
    print ' Input 1, 2, or 3.'
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
        
        if not guess_num > 0 or not guess_num < 4:
            print("That number is not between 1 and 3. ")
            break
        
        
        elif guess_num == random_number:
            print("You\'re right!")
            print("Good job. ({} number(s) inputed.) ".format(tries))
            break
        
        
        elif guess_num < random_number:
            if tries_remaining > 0:
                print("That number is low. You have {} try..".format(int(tries_remaining)))
                continue
            else:
                print("I feel more like a {}".format(random_number))
                print("")
                break
        
        
        
        elif guess_num > random_number:
            if tries_remaining > 0:
                print("That number is too high. You have {} more try.".format(int(tries_remaining)))
                continue
            else:
                print("Correct answer: {}".format(random_number))
                print("Nevermind. I\'m not hungry.")
                break
    