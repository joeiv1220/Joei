import sys
#greeting
def Hello(greeting):
    name = raw_input("Hello, what's your name?")
    return greeting + name



print Hello("Welcome,")
print ("This game will allow you to choose an area of profession e.g. \
(arts, education, computer science, government, health/sciences, law, and \
scientific world) which will link to a major event that has modified history. \
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
print ("2. Computer Science")
print ("3. Health Sciences")
print (25 * '-')
 
# Get input #
choice = raw_input('Enter your choice [1-3] : ')
 
# Convert string to int type #
choice = int(choice)


#Take action as per selected menu-option #
sys.argv = ['C:\\Users\\57bl\Dropbox\John Mauchly.py',\
'C:\\Users\\57bl\Dropbox\FineArts.py',\
'C:\\Users\\57bl\Dropbox\HealthSciences.py']


if choice == 1:
    print ("Fine Arts")
    execfile('C:\\Users\\57bl\Dropbox\FineArts.py')
    
elif choice == 2:
    print ("Computer Science")
    execfile('C:\\Users\\57bl\Dropbox\John Mauchly.py')
    
elif choice == 3:
    execfile('C:\\Users\\57bl\Dropbox\HealthSciences.py')
    print ("Health Sciences")
else:    ## default ##
        print ("Invalid number. Try again...")

#whatbag 

#friends
