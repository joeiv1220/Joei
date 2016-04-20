import sys

from minigames import xy

print 'Background:'

node = None

class computerscience:
    def __init__(self, name, description, dialogue, f, b, r, l, yes, no):
        self.name = name
        self.description = description
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
 
room0 = computerscience(':\n',':\n',':\n', 'room1', None, None, None, 'xy', None)  
room1 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room2 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room3 = computerscience(':\n', ':\n',':\n',None, None, None, None, None, None)     
room4 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)   
room5 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room6 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room7 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room8 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room9 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room10 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room11 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room12 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room13 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room14 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room15 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room16 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room17 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room18 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room19 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room20 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room21 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room22 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room23 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room24 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room25 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room26 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room27 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room28 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room29 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room30 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room31 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room32 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)   
room33 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)     
room34 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room35 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room36 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room37 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room38 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room39 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room40 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room41 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)     
room42 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room43 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room44 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room45 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room46 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room47 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room48 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room49 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)     
room50 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)  
room51 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room52 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room53 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room54 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room55 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room56 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room57 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)
room58 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room59 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None) 
room60 = computerscience(':\n',':\n',':\n', None, None, None, None, None, None)



node = room0


while True:
    print 'options: name, description,  f(foward), b(backward), r(right),\
 l(left), yes, no\n'
    print node.name, node.description
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name','description', 'dialogue','f', 'b', 'r', 'l', 'yes', 'no']:
        try:
            node.move(command)
        except:
            print 'Invalid option. Input a valid option.'