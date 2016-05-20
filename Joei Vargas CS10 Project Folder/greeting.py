import sys
#greeting
def Hello(greeting):
    name = raw_input("Hello, what's your name?")
    return greeting + name
 
print Hello("Welcome,")
print ("This game which will link to a major event that has modified history. \
Through a structured simulation,you will be in the executive position of \
modifying the historical event that the category includes. Each historic event \
simulation will include fictional and real humans in the real world. The \
objective is to discover the reality of the historic event. You can either win \
or lose depending your actions throughout the game.")

# Show menu #
print (25 * '-')
print ("  M A I N - M E N U  ")
print (25 * '-')
print ("1. Fine Arts")
print (25 * '-')
 
# Get input #
choice = raw_input('Enter your choice [1-3] : ')
 
# Convert string to int type #
choice = int(choice)

#Take action as per selected menu-option #
sys.argv = ['C:\\Users\\57bl\Documents\GitHub\Joei\Joei Vargas CS10 Project Folder\\finearts.py']

if choice == 1:
    print ("Fine Arts")
    execfile('C:\\Users\\57bl\Documents\GitHub\Joei\Joei Vargas CS10 Project Folder\\finearts.py')
    
else:    ## default ##
        print ("Invalid number. Try again...")
#whatbag 
#friends


















