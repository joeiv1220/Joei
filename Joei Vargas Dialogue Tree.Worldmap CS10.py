import sys

INTRO = 'Intro'
dialog_node = INTRO
npc_name = '    MJ'
def display_options(node):
    print '\n    Options:'
    for i,p in enumerate(node['PATHS']):
        print '\t%d: "%s"' % (i, p[2])

def player_says(destination, text):
    global dialog_node
    print '    You say: "%s"' % text
    dialog_node = destination

Intro = 'You wake up to find yourself trapped in a room with a woman.\
You both are wearing traditional striped pajamas. She is now waking up.\
Find your way out, with or without her. Good luck.'
print Intro
the_dialog = {
    INTRO : {
    'DIALOG' :  'Who are you?! What am I doing here?! Where are we?!',
        'PATHS' : [
        (player_says, 'lost_mental','If I could answer those\
 questions, I would. I\'ve forgotten everything. Are you hurt?'),
        (player_says, 'mutual','I should be asking you the same.')
        ]
    },
    'lost_mental' : {
        'DIALOG' : 'No. I\'m just a bit dizzy..',
        'PATHS' : [
        (player_says, 'move_now','Well we should get moving.\
 Help me bust the door down.')
            ]
        },
    'move_now' : {
        'DIALOG': 'That was somewhat simple. Now, which way?',
        'PATHS' : [
            (player_says, 'go_right','Let\'s go right.'),
            (player_says, 'go_left','Let\'s go left.') 
        ] 
        }, 
    'go_left' : {
    'DIALOG' : 'This is a long hallway.',
    'PATHS' : [
        (player_says, 'give_name','It is. May I have your name?'),
        (player_says, 'do_you','True. Wait.. Do you see that door?!')
            ]
        },          
    'do_you' : {
    'DIALOG' : 'I do! Hurry let\'s go!',
   # 'PATHS' : [
      #  (player_says, 'my_name','My name is'),
      #  (player_says, 'imig','Whatever then.')
      #      ]
        },        
    'give_name' : { 
    'DIALOG' : 'Just call me MJ for now.'
   # 'PATHS' : [
    #    (player_says, 'my_name','My name is'),
        #(player_says, 'imig','Whatever then.')
      #      ]
        },  
    'mutual' : {
    'DIALOG' : 'I\'m just scared. I\'m sorry..',
    'PATHS' : [
        (player_says, 'fine','It\'s okay. I understand.')
        ]
        },
         
    'fine' : {
    'DIALOG' : 'Thanks. I appreciate it. My name is MJ by the way.',
  
        },
          
        }
       # 'move_now' : {
    #    'DIALOG': 'That was somewhat simple. Now, which way?',
    #    'PATHS' : [
     #       (player_says, 'curious_0','True true. I never got your name?'),
    #        (player_says, 'end_convo_1','I think we should turn back.')        
  #  ]
 #  }, 
  #  'curious_0' : { 
  #  'DIALOG' : 'I can\'t tell you that. I hardly know you.',
#    'PATHS' : [
#        (player_says, 'understand','I know this is\
 #all confusing but I\'m sure we\'ll get out.'),
  ##         ]
    #    },  

  # 'end_convo_1' : {
   #     'DIALOG' : 'We can\'t. What if whoever put us in that room come back?',
       # 'PATHS' : [
        #(player_says, 'my_name','My name is'),
       # (player_says, 'imig','Whatever then.')
        #    ]
     #   },
            
 #   'fine' : {
  #  'DIALOG' : 'Thanks. I appreciate it. My name is MJ by the way.',
  
   #     },
        
 #   'understand' : {
#    'DIALOG' : 'I know. Thanks for not leaving me behind back there.',
   # 'PATHS' : [
    #    (player_says, 'my_name','My name is'),
    #    (player_says, 'imig','Whatever then.')
   #         ]
 #      },


while True:
    node = the_dialog[dialog_node]
    
    #NPC talks
    print '%s says: %s' % (npc_name, node['DIALOG'])
    if 'PATHS' in node:
        display_options(node)
        
        #ask for input
        response = raw_input('> ').strip().lower()
        
        if response in ['q', 'exit', 'quit']:
            sys.exit(0)
        try:
            path = node['PATHS'][int(response)]
            function = path[0]
            args = path[1: ]
            function(*args)
            
        except: 
            print 'Invalid option. Input a valid number.'
        
    else:
    #Quit program
        sys.exit(0)
