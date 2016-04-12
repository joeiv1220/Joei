import sys

print "Introduction:"

node = None

class John_Mauchly:
    def __init__(self, name, descript, f, b, r, l):
        self.name = name
        self.f = f
        self.b = b 
        self.r = r
        self.l = l
        self.descript = descript
         
    def move(self, direction):
        global node
        node = globals()[getattr(self,direction)] 
 
room0 = John_Mauchly(':\n', None , None, None, None, None, None, None)  
room1 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room2 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room3 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room4 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room5 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room6 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room7 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room8 = John_Mauchly(':\n', None , None, None, None, None, None, None)  
room9 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room10 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room11 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room12 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room13 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room14 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room15 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room16 = John_Mauchly(':\n', None , None, None, None, None, None, None)  
room17 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room18 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room19 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room20 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room21 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room22 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room23 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room24 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room25 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room26 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room27 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room28 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room29 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room30 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room31 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room32 = John_Mauchly(':\n', None , None, None, None, None, None, None)    
room33 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room34 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room35 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room36 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room37 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room38 = John_Mauchly(':\n', None , None, None, None, None, None, None)  
room39 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room40 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room41 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room42 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room43 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room44 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room45 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room46 = John_Mauchly(':\n', None , None, None, None, None, None, None)  
room47 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room48 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room49 = John_Mauchly(':\n', None, None, None, None, None, None, None)     
room50 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room51 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room52 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room53 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room54 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room55 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room56 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room57 = John_Mauchly(':\n', None, None, None, None, None, None, None)
room58 = John_Mauchly(':\n', None, None, None, None, None, None, None)  
room59 = John_Mauchly(':\n', None, None, None, None, None, None, None) 
room60 = John_Mauchly(':\n', None, None, None, None, None, None, None) 


node = room0


while True:
    print 'options: name, description, f(foward), b(backward), r(right),\
 l(left)'
    print node.name, node.descript
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name, f, b, r, l, descript']:
        try:
            node.move(command)
        except: 
   
            print 'Invalid option. Input a valid option.'
            