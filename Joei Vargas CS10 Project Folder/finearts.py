import sys
#import random
import pickle

from minigames import bun, chips, xy, ab, imdead


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
        elif woo == chips:
            chips()
            node = room5
        elif woo == xy:
            xy()
            node = room10y
        elif woo == ab:
            ab()
            node = room26
        else:
            node = woo
        
         
room0 = FineArts('Band Room:\n','An oboe would like to play your trumpet. What do you say? To the right is the office.\n','"That\'s such a cool trumpet!! Can I play it?"\n', 'bun', None, None, None, 'bun', 'room1n')   
room1y = FineArts('Band Room:\n','Good job!\n','"Haha maybe I\'ll give up oboe."\n', None, None, 'room2', None, None, None)
room1n = FineArts('Band Room:\n','\n','"I understand. Maybe I\'ll just switch to trumpet!"\n', None, None, 'room2', None, None, None)
room2 = FineArts('Office:\n','There\'s a substitute today. He\'s complaining.\n','"These kids are giving me a headache. I can\'t understand how their teacher does it."\n', None, None, None, 'room3', None, None)  
room3 = FineArts('Storage Room:\n','Mr. Ticheli left some snacks for you. He knew you\'d become tired of running the class.\n','\n', 'room4', None, None, None, None, None)     
room4 = FineArts('Box of Snacks:\n','\n','There\'s pretzels, Lay\'s, and a somewhat cold soda. The expiration date for each reads 04/15/1997, 02/13/1998, and 11/15/1990. The soda "expires" in 10 days.. interesting.\n', 'chips', 'chips', 'chips', 'chips', 'chips', 'chips')   
room5 = FineArts('Storage Room:\n','\n','\n', None, 'room6', None, None, None, None)
room6 = FineArts('Office:\n','\n','\n', None, None, 'room7', None, None, None) 
room7 = FineArts('Band Room:\n','\n','\n', None, None, None, 'room8', None, None)
room8 = FineArts('Band Room:\n','You are in the pathway coming into the band room.\n','\n', None, None, 'room9', None, None, None)
room9 = FineArts('Fridge:\n','\n','Open the fridge?\n', None, None, None, None, 'xy', 'room10n')
room10y = FineArts('Clean Fridge:\n','\n','RRRRRRRRIIIIIIIINNNNNNNNGGGGGGGGGGGGGGGGGG Sub: "Class is dismissed." Mom wants you home early.You should get going.\n', 'room11', 'room11', 'room11', 'room11', 'room11', 'room11')
room10n = FineArts('Fridge:\n','\n','RRRRRRRIIIIIIIINNNNNNNNGGGGGGGGGGGGGGGGGG Sub: "Class is dismissed." Mom wants you home early. You should get going.\n', 'room11', 'room11', 'room11', 'room11', 'room11', 'room11')
room11 = FineArts('SAVE YOUR GAME\n','\n','\n', 'room12', 'room12', 'room12', 'room12', 'room12', 'room12')
room12 = FineArts('Bedroom:\n','The majestic sunrise, possesses an orange glow seeping over the horizon. Powerful rays flood over the landscape lighting every blade of grass. \n','\n', 'room13', 'room13', 'room13', 'room13', 'room13', 'room13')
room13 = FineArts('Bedroom:\n','You are in bed.\n','You can hear your mother\'s alarm clock going off. The radio plays Celine Dion\'s "My Heart Will Go On". It is March 28th.\n', 'room14', 'room14', 'room14', 'room14', 'room14', 'room14')
room14 = FineArts('Bedroom:\n','You are in bed.\n','\n', 'room15', None, None, None, None, None)
room15 = FineArts('Bedroom:\n','You are out of bed.\n','\n', 'room16', None, None, None, None, None)
room16 = FineArts('Bedroom:\n','You are standing up.\n','\n', None, None, 'room17', None, None, None)
room17 = FineArts('Shelf:\n','It\'s dark. You can\'t see what\'s on the shelf.\n','\n', None, None, 'room18', None, None, None) 
room18 = FineArts('Door\n','...\n','...\n', None, None, 'room19', None, None, None)
room19 = FineArts('Wall:\n','You feel a lightswitch.\n','Would you like to turn the light on?\n', None, None, None, None, 'room20', None)
room20 = FineArts('Lightswitch:\n','The light is on.\n','\n', None, 'room21', None, None, None, None)
room21 = FineArts('Bedroom:\n','\n','You should go look at the shelf.\n', 'room22', None, None, None, None, None) 
room22 = FineArts('Shelf:\n','There is a note.\n','Read it?\n', None, None, None, None, 'room23', None) 
room23 = FineArts('Note:\n','\n','Hey Robbie, please pick up around the house before you go to school. I\'ll have dinner ready once you come home. Have a great day. Love, Mom.\n', None, 'room24', None, None, None, None)
room24 = FineArts('Shelf:\n','...\n','...\n', None, None, None, 'room25', None, None)  
room25 = FineArts('Clothes:\n','laundry basket\n','Get dressed.\n', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab') 
room26 = FineArts('Bedroom:\n','\n','Almost time for school. \n', None, None, None, None, None, None) 
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
           
           
    
    if node == bun:
        node = room1y
          

    
    
