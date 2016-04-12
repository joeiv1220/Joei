import sys

node = None

class Room:
    def __init__(self, name, n, e, s, w, pickup, putdown, o, descript):
        self.n = n
        self.e = e 
        self.s = s
        self.w = w 
        self.name = name
        self.pickup = pickup
        self.putdown = putdown
        self.o = o
        self.descript = descript
         
    def move(self, direction):
        global node
        node = globals()[getattr(self,direction)] 
 
room1 = Room('Band Room Door:', 'room2', None, None, None, None, None, 'room2', 'This is your starting point.')
room2 = Room('Band Room:', None, None, None, 'room3', None, None, None, 'This is room one. The lovely band room dude. Keep it clean.') 
room3 = Room('Drum Room:', 'roomclear', None, None, None, None, None, None, 'Welcome to the drum room! Once you come in, you can not come out.')
roomclear = Room('', None, None, None, 'object1', None, None, None, '')    
object1 = Room('Locker:', execfile('C:\\Users\\57bl\Dropbox\Music code.py'), None, None, None, None, None, 'object2', 'You: ...are those cymbals?')
object2 = Room('Cymbals:', 'choice1', 'choice1', 'choice1', 'choice1', None, None, None, 'Those belong to the band kids. Do not touch them. We should keep going.')
choice1 = Room('You Decide:', None, None, 'result1', None, 'result2', None, None, 'Pick up or back up?')
result1 = Room('Good Job:', 'come1', 'come1', 'come1', 'come1', 'come1', 'come1', 'come1', '')
result2 = Room('', 'come2', 'come2', 'come2', 'come2', 'come2', 'come2', 'come2', '*CRASH CRASH CRASH CRASH*')
come1 = Room('Drum Room:', 'vaminos', None, None, None, None, None, None, 'The drum room doesn\'t have much for us to see. Let\'s explore the rest of the band room.')
come2 = Room('Drum Room:', 'sorry', None, None, None, None, None, None, 'WOW REALLY DUDE?!? MADRID IS WITH WIND ENSEMBLE RIGHT NOW!')
vaminos = Room('', 'roomclear2', None, None, None, None, None, None, 'Okay, I\'m ready.')  
sorry = Room('', 'roomclear2', None, None, None, None, None, None, 'I\'m so sorry! We should get going.')  
roomclear2 = Room('', None, 'room4', None, None, None, None, None, '') 
room4 = Room('Band Room', None, None, None, None, None, None, None, 'Be really quiet. Madrid is talking to the woodwinds like always.')  


node = room1


while True:
    print 'options: name, n, e, s, w, pickup, putdown, o (open), descript'
    print node.name, node.descript
    command = raw_input()
    if command in ['q', 'exit', 'quit', 'ex']:
            sys.exit(0)
    elif command in ['name', 'n', 'e', 's', 'w', 'pickup', 'putdown', 'o', 'descript']:
        try:
            node.move(command)
        except: 
   
            print 'Invalid option. Input a valid option.'
      
                   
                                
                                             
                                                          
                                                                       
                                                                                    
                                                                                                 
                                                                                                              
                                                                                                                           
                                                                                                                                        
                                                                                                                                                     
                                                                                                                                                                  
                                                                                                                                                                               
                                                                                                                                                                                            
                                                                                                                                                                                                         
                                                                                                                                                                                                                                   
      #  response = raw_input(' ').strip().lower()
        
    #    if response in ['q', 'exit', 'quit']:
    #        sys.exit(0)
      
     #   else:
    #Quit program
      #      sys.exit(0)
