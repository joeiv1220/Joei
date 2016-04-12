import random
vocab = ('n', 'e', 's', 'w', 'u', 'd', 'yes', 'no', 'pick up','throw away','throw','pink slip', 'yes','no')
PL = 'Parking Lot'
G = 'Gate'
FO = 'Front Office'
IO = 'Inside Office'
SASS = ('Is your head okay?', 'You done goofed. Try again.', 'Happy to know you like hugging walls.')
world_map = {
    G : {
        'DESCRIPTION' : "You are standing in front of the school's gate.",
        'PATHS' : {
            'n' : 'Parking Lot'
        }
    },
    
    PL : {
        'DESCRIPTION' : "This is the parking lot. There's a pink slip on the\
 ground.",
        'PATHS' : {
        's' : 'Gate',
        'n' :'Parking Lot',
        'n' :'Front Office'
        
        }
    },
    
    FO : {
        'DESCRIPTION' : "Here is the front office. It's empty and the doors\
 seem to be untouched.",
        'PATHS' : {
        'n' : 'Inside Office', 
        's' : 'Parking Lot'
    
    },
    IO : {
        'DESCRIPTION' : "There is nobody here. Go explore.",
        'PATHS' : {
        's' :  execfile('C:\\Users\\57bl\Dropbox\Music code.py')
    
    
            },
        }
    }
}

PSL = 'Gate'
while True:
    room = world_map[PSL]
    print PSL

    print room['DESCRIPTION']
    
   
    command = raw_input('...').strip().lower()
    
   
    if command in vocab:
        if command in room['PATHS']:
            PSL = room['PATHS'][command]
        else:
            print random.choice(SASS)
    else:
        print "I don't recognize \"%s\".\n\n" % command

   