import sys

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
    def __init__(self, name, descript, f, b, r, l, yes, no):
        self.name = name
        self.descript = descript
        self.f = f
        self.b = b 
        self.r = r
        self.l = l  
        self.yes = yes
        self.no = no
         
    def move(self, direction): 
        global node
        node = globals()[getattr(self,direction)]
#____________________________________________________________________________
def game1():
    print 'Okay I am one'
def game2():
    print 'Okay I am two'
def game3():
    print 'Okay I am three'    
#____________________________________________________________________________
room0 = FineArts('Band Class:\n', 'It\'s first period. The oboe player would like\
 to play your trumpet. Do you teach them?', \
None, None, None, None, game1, 'roomN1')
#roomY1 = FineArts('Band Class:', 'They sneezed on your trumpet! Ew! You should\
# go clean it.', 'roomY2', None, None, None, 'roomY2', None)
roomN1 = FineArts('Band Class:\n', 'You told them no and they understood.\
Time for a playing test.', 'roomN2', None, None, None, None, None)
#roomY2 = FineArts('Office:', 'Find the mouthpiece spray', game2, None,\
 #None, None, game2, None)
roomN2 = FineArts('Office:\n', '"Sightread this piece and then you can go."',
 game3, None, None, None, game3, None)
room3 = FineArts(None, None, None, None,\
 None, None, None, None)
room4 = FineArts(None, None, None, None,\
 None, None, None, None)
room5 = FineArts(None, None, None, None,\
 None, None, None, None)
room6 = FineArts(None, None, None, None,\
 None, None, None, None)
room7 = FineArts(None, None, None, None,\
 None, None, None, None)
room8 = FineArts(None, None, None, None,\
 None, None, None, None) 
room9 = FineArts(None, None, None, None,\
 None, None, None, None)
room10 = FineArts(None, None, None, None,\
 None, None, None, None)
room11 = FineArts(None, None, None, None,\
 None, None, None, None)
room12 = FineArts(None, None, None, None,\
 None, None, None, None)
room13 = FineArts(':\n', None, None, None, None, None, None, None) 
room14 = FineArts(':\n', None, None, None, None, None, None, None) 
room15 = FineArts(':\n', None, None, None, None, None, None, None)
room16 = FineArts(':\n', None , None, None, None, None, None, None)  
room17 = FineArts(':\n', None, None, None, None, None, None, None)  
room18 = FineArts(':\n', None, None, None, None, None, None, None)  
room19 = FineArts(':\n', None, None, None, None, None, None, None)     
room20 = FineArts(':\n', None, None, None, None, None, None, None)  
room21 = FineArts(':\n', None, None, None, None, None, None, None) 
room22 = FineArts(':\n', None, None, None, None, None, None, None) 
room23 = FineArts(':\n', None, None, None, None, None, None, None)
room24 = FineArts(':\n', None, None, None, None, None, None, None)  
room25 = FineArts(':\n', None, None, None, None, None, None, None) 
room26 = FineArts(':\n', None, None, None, None, None, None, None) 
room27 = FineArts(':\n', None, None, None, None, None, None, None)
room28 = FineArts(':\n', None, None, None, None, None, None, None)  
room29 = FineArts(':\n', None, None, None, None, None, None, None) 
room30 = FineArts(':\n', None, None, None, None, None, None, None) 
room31 = FineArts(':\n', None, None, None, None, None, None, None)    
room32 = FineArts(':\n', None , None, None, None, None, None, None)    
room33 = FineArts(':\n', None, None, None, None, None, None, None)     
room34 = FineArts(':\n', None, None, None, None, None, None, None)  
room35 = FineArts(':\n', None, None, None, None, None, None, None) 
room36 = FineArts(':\n', None, None, None, None, None, None, None) 
room37 = FineArts(':\n', None, None, None, None, None, None, None)
room38 = FineArts(':\n', None , None, None, None, None, None, None)  
room39 = FineArts(':\n', None, None, None, None, None, None, None)  
room40 = FineArts(':\n', None, None, None, None, None, None, None)  
room41 = FineArts(':\n', None, None, None, None, None, None, None)     
room42 = FineArts(':\n', None, None, None, None, None, None, None)  
room43 = FineArts(':\n', None, None, None, None, None, None, None) 
room44 = FineArts(':\n', None, None, None, None, None, None, None) 
room45 = FineArts(':\n', None, None, None, None, None, None, None)
room46 = FineArts(':\n', None , None, None, None, None, None, None)  
room47 = FineArts(':\n', None, None, None, None, None, None, None)  
room48 = FineArts(':\n', None, None, None, None, None, None, None)  
room49 = FineArts(':\n', None, None, None, None, None, None, None)     
room50 = FineArts(':\n', None, None, None, None, None, None, None)  
room51 = FineArts(':\n', None, None, None, None, None, None, None) 
room52 = FineArts(':\n', None, None, None, None, None, None, None) 
room53 = FineArts(':\n', None, None, None, None, None, None, None)
room54 = FineArts(':\n', None, None, None, None, None, None, None)  
room55 = FineArts(':\n', None, None, None, None, None, None, None) 
room56 = FineArts(':\n', None, None, None, None, None, None, None) 
room57 = FineArts(':\n', None, None, None, None, None, None, None)
room58 = FineArts(':\n', None, None, None, None, None, None, None)  
room59 = FineArts(':\n', None, None, None, None, None, None, None) 
room60 = FineArts(':\n', None, None, None, None, None, None, None)  
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
            