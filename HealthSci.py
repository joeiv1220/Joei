import sys
from Minigames import pain


print ' Introduction: \n To win, successfully cure ? with background knowledge and skill.\
 Good luck.\n'

node = None

class HealthSciences:
    def __init__(self, name, description, f, b, r, l, yes, no):
        self.name = name
        self.description = description
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
 
room0 = HealthSciences(':\n',':\n',':\n', None , 'room1', None, None, None, 'pain', None)  
room1 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)
room2 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)  
room3 = HealthSciences(':\n', ':\n',':\n',None, None, None, None, None, None)     
room4 = HealthSciences(':\n',':\n',':\n', None, None, None, None, None, None)   
room5 = HealthSciences 
room6 = HealthSciences
room7 = HealthSciences
room8 = HealthSciences  
room9 = HealthSciences
room10 = HealthSciences  
room11 = HealthSciences  
room12 = HealthSciences  
room13 = HealthSciences 
room14 = HealthSciences
room15 = HealthSciences
room16 = HealthSciences
room17 = HealthSciences
room18 = HealthSciences 
room19 = HealthSciences   
room20 = HealthSciences
room21 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room22 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room23 = HealthSciences
room24 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room25 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room26 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room27 = HealthSciences(':\n', None, None, None, None, None, None, None)
room28 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room29 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room30 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room31 = HealthSciences(':\n', None, None, None, None, None, None, None)
room32 = HealthSciences(':\n', None , None, None, None, None, None, None)    
room33 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room34 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room35 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room36 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room37 = HealthSciences(':\n', None, None, None, None, None, None, None)
room38 = HealthSciences(':\n', None , None, None, None, None, None, None)  
room39 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room40 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room41 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room42 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room43 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room44 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room45 = HealthSciences(':\n', None, None, None, None, None, None, None)
room46 = HealthSciences(':\n', None , None, None, None, None, None, None)  
room47 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room48 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room49 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room50 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room51 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room52 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room53 = HealthSciences(':\n', None, None, None, None, None, None, None)
room54 = HealthSciences  
room55 = HealthSciences
room56 = HealthSciences 
room57 = HealthSciences
room58 = HealthSciences  
room59 = HealthSciences
room60 = HealthSciences 



node = room0


while True:
    print 'options: name, description, f(foward), b(backward), r(right),\
 l(left), yes, no\n'
    print node.name, node.descript 
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name', 'f', 'b', 'r', 'l', 'descript', 'yes', 'no']:
        try:
            node.move(command)
        except:
            print 'Invalid option. Input a valid option.'
