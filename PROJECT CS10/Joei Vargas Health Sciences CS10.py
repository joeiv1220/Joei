import sys
from jvminics10 import pain


print ' Introduction: \n To win, successfully cure ? with background knowledge and skill.\
 Good luck.\n'

node = None

class HealthSciences:
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
        if woo == pain:
            pain()
        else:
            node = woo
 
room0 = HealthSciences(':\n',':\n',':\n', 'room1', None, None, None, 'pain', None)  
room1 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room2 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room3 = HealthSciences(':\n', ':\n',':\n',None, None, None, None, None, None)     
room4 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)   
room5 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room6 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None) 
room7 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room8 = HealthSciences  (':\n',':\n',':\n', None, None, None, None, None, None)
room9 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room10 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room11 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room12 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room13 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room14 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room15 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room16 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room17 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None) 
room18 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room19 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room20 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room21 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room22 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room23 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room24 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room25 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room26 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room27 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room28 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room29 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room30 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room31 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room32 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)   
room33 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)     
room34 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room35 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room36 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room37 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room38 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room39 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room40 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room41 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)     
room42 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room43 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room44 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room45 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room46 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)  
room47 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room48 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room49 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)     
room50 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room51 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room52 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None) 
room53 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room54 = HealthSciences  (':\n',':\n',':\n', None, None, None, None, None, None)
room55 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room56 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room57 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)
room58 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None) 
room59 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None) 
room60 = HealthSciences (':\n',':\n',':\n', None, None, None, None, None, None)



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