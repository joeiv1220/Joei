import sys
from Minigames import pain


print ' Introduction: "HIV (human immunodeficiency virus) is a virus that attacks\
 the immune system, the body\'s natural defense system. Without a strong\
 immune system, the body has trouble fighting off disease. Both the virus\
 and the infection it causes are called HIV. White blood cells are an important\
 part of the immune system."- Google\n\
 \n To win, successfully cure HIV with background knowledge and skill.\
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
        temp = globals()[getattr(self,direction)] 
        if temp == pain:
            pain()
        else:
            node = temp
 
room0 = HealthSciences(':\n', None , 'room1', None, None, None, 'pain', None)  
room1 = HealthSciences('hello:\n', None, None, None, None, None, None, None)
room2 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room3 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room4 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room5 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room6 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room7 = HealthSciences(':\n', None, None, None, None, None, None, None)
room8 = HealthSciences(':\n', None , None, None, None, None, None, None)  
room9 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room10 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room11 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room12 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room13 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room14 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room15 = HealthSciences(':\n', None, None, None, None, None, None, None)
room16 = HealthSciences(':\n', None , None, None, None, None, None, None)  
room17 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room18 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room19 = HealthSciences(':\n', None, None, None, None, None, None, None)     
room20 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room21 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room22 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room23 = HealthSciences(':\n', None, None, None, None, None, None, None)
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
room54 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room55 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room56 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room57 = HealthSciences(':\n', None, None, None, None, None, None, None)
room58 = HealthSciences(':\n', None, None, None, None, None, None, None)  
room59 = HealthSciences(':\n', None, None, None, None, None, None, None) 
room60 = HealthSciences(':\n', None, None, None, None, None, None, None) 



node = room0


while True:
    print 'options: name, description, f(foward), b(backward), r(right),\
 l(left), yes, no\n'
    print node.name, node.descript 
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name', 'f', 'b', 'r', 'l', 'description', 'yes', 'no']:
        try:
            node.move(command)
        except:
            print 'Invalid option. Input a valid option.'
