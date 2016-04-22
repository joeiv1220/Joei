import sys
import random

from minigames import bun

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
        if woo == bun:
            bun()
            node = room1y
        else:
            node = woo
 
room0 = FineArts('Band Room:\n','An oboe would like to play your trumpet. What\
 do you say?:\n','"That\'s such a cool trumpet!! Can I play it?"\n', 'room1n', None,\
None, None, 'bun', 'room1n')   
room1y = FineArts('Band Room:\n',':\n','"Haha maybe I\'ll give up oboe."\n',\
 None, None, 'room2', None, None, None)
room1n = FineArts('Band Room:\n',':\n','"I understand. Maybe I\'ll just switch\
to trumpet!"\n',
 None, None, 'room2', None, None, None)
room2 = FineArts('Office:\n',':\n','There\'s a substitute today. He\'s\
 complaining."These kids are giving me a headache. I can\'t understand how\
 their teacher does it."\n', None, None, None, 'room3', None, None)  
room3 = FineArts('Small Room:\n', ':\n','Mr. Ticheli left some snacks for you.\
 He knew you\'d become tired of running the class.\n', 'room4', None, None,\
 None, None, None)     
room4 = FineArts('Box of Snacks:\n',':\n','There\'s pretzels, Lay\'s and a\
 somewhat cold soda.\n', 'room5', 'room5', 'room5', 'room5', 'room5', 'room5')   
room5 = FineArts(':\n',':\n','\n', None, None, None, None, None, None)
room6 = FineArts(':\n',':\n','\n', None, None, None, None, None, None) 
room7 = FineArts(':\n',':\n','\n', None, None, None, None, None, None)
room8 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room9 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room10 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room11 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room12 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room13 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room14 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room15 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room16 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room17 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room18 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room19 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room20 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
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
room38 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room39 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room40 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room41 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)     
room42 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room43 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room44 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room45 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room46 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room47 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room48 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room49 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)     
room50 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)  
room51 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room52 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room53 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room54 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room55 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room56 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room57 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)
room58 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room59 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None) 
room60 = FineArts(':\n',':\n',':\n', None, None, None, None, None, None)



node = room0


while True:
    print '\n options: name, location, dialogue, f(foward), b(backward), r(right),\
 l(left), yes, no\n'
    print node.name, node.location, node.dialogue
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name','location','dialogue','f', 'b', 'r', 'l', 'yes', 'no']:
        try:
            node.move(command)
        except:
           print 'Invalid option. Input a valid option.'