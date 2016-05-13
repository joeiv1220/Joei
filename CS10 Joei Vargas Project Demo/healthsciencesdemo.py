 import sys
import pickle
from minigamesdemo import pain


print ' Introduction: \n To win, successfully cure... with\
background knowledge and skill. Good luck.\n'

node = None

class HealthSciences:
    def __init__(self, name, location, dialogue, f, b, r, l, yes, no):
        self.name = name
        self.location = location
        self.dialogue = dialogue
        self.f = f
        self.b = b 
        self.r = r
        self.l = l   
        self.yes = yes
        self.no = no
         
    def move(self, direction):
        global node
        woo = globals()[getattr(self,direction)] 
        if woo == pain:
            pain()
            node = room4
        else:
            node = woo
 
room0 = HealthSciences('Lab:\n', 'Professor Hill is becoming frustrated with the class. The sink\
 is to the right.\n','"YOU ARE ALL STUPID!! SOMEONE GRAB ME SOME WATER!!!"\n', None , None, 'room1', None, None None)  
room1 = HealthSciences('Sink:\n', 'Grab water?\n','"NOW!!!"\n', None, None, None, None, 'room2', 'room2n')
room2 = HealthSciences('Water:\n', 'You have spilled the water.\n','"WAY TO GO DOCTOR SPILLY\
 !!! NOW GET OVER HERE AND PARTICIPATE"\n', 'pain', 'pain', 'pain', 'pain', 'pain', 'room3')  
room2n = HealthSciences('Water:\n', 'You are standing alone\n','"OHHHHHH DOCTORRRRRR!!!"\n', 'pain', 'pain', 'pain', 'pain'\
 , 'pain', 'pain')  
room3 = HealthSciences('You Said What???:\n', 'Yikes.\n','"Now I want everyone to say goodbye too our fellow\
 classmate." "Goodbye!" "Bye dude." "I\'ll make sure your parents know the real story! Don\'t worry!"\
 "Would you like to go as well, Jeanu?.. No? Of course not."\n','room5', 'room5', 'room5', 'room5', 'room5', 'room5')     
room4 = HealthSciences('Post:\n', 'Okay. Nice.\n','"Well done."\n', 'room5', 'room5', 'room5', 'room5', 'room5', 'room5')   
room5 = HealthSciences('END:\n', 'Thank you for playing through my demo version of\
 Health Sciences. For more information talk to me. I will also be raffling off\
 my cups.\n',':\n', None, None, None, None, None, None)


node = room0

def save():
    global node, room1n
    with open ('savegame.dat','wb') as f:
        pickle.dump([node, room1],f, protocol=2)
    print "Game successfully saved."
    
def load():  
    global node, room1
    with open('savegame.dat','rb') as f:
        node, room1 = pickle.load(f)
    print "Game successfully loaded."

while True:
    print '\noptions: name, location, dialogue, f(foward), b(backward), r(right),\
 l(left), yes, no, save, load\n'
    print node.name, node.location, node.dialogue
    command = raw_input().strip().lower()
    if command in ['q', 'exit', 'quit', 'ex']:
        sys.exit(0)
    elif command in ["save"]:
          save()
    elif command in ["load"]:
          load()
    elif command in ['name','location','dialogue','f', 'b', 'r', 'l', 'yes', 'no']:
        try:
            node.move(command)
        except:
           print 'Invalid option. Input a valid option.'
