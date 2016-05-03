import sys
import pickle
from minigames import pain


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
        else:
            node = woo
 
room0 = HealthSciences(':\n',':\n',':\n', 'room1', None, None, None, 'pain', None)  
room1 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room2 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room3 = HealthSciences(':\n', ':\n',':\n',None, None, None, None, None, None)     
room4 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)   
room5 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room6 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room7 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room8 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room9 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room10 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room11 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room12 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room13 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)


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