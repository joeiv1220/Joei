import sys
#import random
import pickle

from minigamesdemo import bundemo, chipsdemo

print 'Background:\n Mr. Robert M. Madrid is from the northern\
 San Joaquin Valley where he graduated from Tokay High School in\
 Lodi, CA in 2001... Your objective is..\n'

node = None
room1n = None

class FineArts:
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
        if woo == bundemo:
            bundemo()
            node = room1y 
        elif woo == chipsdemo:
            chipsdemo()
            node = room5
        else:
            node = woo
        
        
room0 = FineArts('Band Room:\n','An clarinet would like to play your trumpet.\
 What do you say? To the right is the office.\n',\
 '"That\'s a shiny trumpet!! Can I play it?"\n', 'room1n',\
 None, None, None, 'bundemo', 'room1n')   
room1y = FineArts('Band Room:\n','You did it!\n','"Haha maybe\
 I\'ll give up clarinet."\n', None, None, 'room2', None, None, None)
room1n = FineArts('Band Room:\n','\n','"Whatever.\
 Maybe I\'ll just switch."\n', None, None,\
 'room2', None, None, None)
room2 = FineArts('Office:\n','There\'s a substitute today.\
 He\'s having a rough time.\n','"I NEED ADVIL RIGHT NOW!\
 I can\'t understand how their teacher does it."\n', None, None,\
 None, 'room3', None, None)  
room3 = FineArts('Storage Room:\n', 'Mr. Ticheli left some snacks for you.\
 He knew you\'d become hungry.\n','\n', 'room4', None,\
 None, None, None, None)     
room4 = FineArts('Box of Snacks:\n','There\'s pretzels, Lay\'s, and a\
 somewhat cold soda.\n','\n', 'chipsdemo', 'chipsdemo', 'chipsdemo',\
 'chipsdemo', 'chipsdemo', 'chipsdemo')   
room5 = FineArts('END:\n','Thank you for playing through my demo version of\
 The Fine Arts. For more information talk to me. I will also be raffling off\
 my cups.\n','\n', None, None, None, None, None, None)




node = room0

def save():
    global node, room1n
    with open ('savegame.dat','wb') as f:
        pickle.dump([node, room1n],f, protocol=2)
    print "Game successfully saved."
    
def load():  
    global node, room1n
    with open('savegame.dat','rb') as f:
        node, room1n = pickle.load(f)
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
           
           
    
    if node == bundemo:
        node = room1y
          

    
