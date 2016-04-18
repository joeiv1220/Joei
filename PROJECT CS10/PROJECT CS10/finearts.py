import sys

from jvminics10 import hbc

print 'Background:\n Mr. Robert M. Madrid is from the northern\
 San Joaquin Valley where he graduated from Tokay High School in\
 Lodi, CA in 2001. He received his Bachelor of Arts in Music Education\
 from Fresno State in 2005 and his Masters of Music in Instrumental Conducting\
 from the American Band College of Sam Houston State University in 2013.\
 During his studies at the American Band College Mr. Madrid worked under the\
 baton of famed composers and conductors such as Frank Ticheli, Johan DeMeij,\
 Robert W. Smith, and Col. Arnald Gabriel.\n \n Mr. Madrid comes from Terronez\
 Middle School where he led the band and orchestra program for 7 years. Under\
 his direction, the Terronez Music Program thrived and grew to record numbers.\
 The ensembles consistently placed in marching band competitions and his concert\
 ensembles received consistent unanimous superior ratings including the CMEA All\
 State Band and Orchestra Festival.\n \n Mr. Madrid made the descision to join\
 the Edison Music Program two years back. The once Edison Highschool\
 Tigerband and Colorguard is now the Edison Golden Brigade.\
 They have had successful and stressful times through marching\
 season 2015-2016. Your objective is to "direct" the band to their\
 first sweepstakes win at the Fresno Fair. You will travel back to\
 Madrid\'s highschool years in hope of following the "correct" path.\
 Use your outside knoweldge and most of all, A the P!\n'

node = None

class FineArts:
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
        if woo == hbc:
            hbc()
        else:
            node = woo
 
room0 = FineArts(':\n',':\n',':\n', 'room1', None, None, None, 'hbc', None)  
room1 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room2 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room3 = FineArts(':\n', ':\n',':\n',None, None, None, None, None, None)     
room4 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)   
room5 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room6 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None) 
room7 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room8 = FineArts  (':\n',':\n',':\n', None, None, None, None, None, None)
room9 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room10 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room11 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room12 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room13 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room14 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room15 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room16 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room17 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None) 
room18 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room19 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room20 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room21 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room22 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room23 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room24 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room25 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room26 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room27 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room28 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room29 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room30 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room31 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room32 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)   
room33 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)     
room34 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room35 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room36 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room37 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room38 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room39 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room40 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room41 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)     
room42 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room43 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room44 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room45 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room46 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)  
room47 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room48 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room49 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)     
room50 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room51 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room52 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room53 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room54 = FineArts  (':\n',':\n',':\n', None, None, None, None, None, None)
room55 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room56 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room57 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)
room58 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None) 
room59 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None) 
room60 = FineArts (':\n',':\n',':\n', None, None, None, None, None, None)



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
