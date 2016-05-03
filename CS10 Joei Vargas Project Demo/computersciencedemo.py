import sys
import pickle
from minigamesdemo import xy

print 'Background: In your spare time, you passionitely research developments\
 of the tech world. Your goal is too..'

node = None

class computerscience:
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
        if woo == xy:
            xy()
        else:
            node = woo
 
room0 = computerscience('Bedroom:\n','To the left is your door.\n','"GET UP MY CHILD!!!! IT\'S TIME TO\
 CLEEEEEAAAAAANNNN!!!!!" Mom is up.\n', None, None, None, 'room1', 'xy', None)  
room1 = computerscience('Hall:\n','This is the hall. The stairs are to the\
 right.\n','\n', None, None, 'room2', None, None, None)
room2 = computerscience('Stairs:\n','\n','"GRAB THE MOP HONEY!!!" Mom is singing The Best\
 Man..\n', 'room3', 'room1', None, None, None, None)  
room3 = computerscience('Underneath the Attic Entrance:\n', 'You are underneath\
 the attic. Would you like to enter?\n','\n',None, None, None, None, 'room4', 'room5')     
room4 = computerscience('Ladder:\n','up....up.....up....\n','\n', 'room5', None, None, None, None, None)   
room5 = computerscience('END:\n','Thank you for playing through my demo version of\
 The Fine Arts. For more information talk to me. I will also be raffling off\
 my cups.\n','\n', None, None, None, None, None, None)



node = room0

def save():
    global node, room1
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