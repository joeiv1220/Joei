import random 

print('What time would you like to meet with your patient, Doctor?\
 Tomorrow, you are free from at 9:00AM, 12:30PM, 2:00PM,\
 3:00PM, 4:30PM, and 5:00PM.') 

times = ('9:00', '12:30', '2:00','3:00', '4:30', '5:00')
time = random.choice(times) 
guess1 = input('At ') 

if guess1 == times: 
    print("YOU WIN WELL DONE") 
else: 
    print("sorry try again") 
    print("YOU HAVE 2 GUESSES REMAINING") 
guess2 = input('Then.. ') 

if guess2 == times: 
    print("WOW YOUR AMAZING YOU WIN") 
else: 
    print("Sorry, one more try") 
    print("YOU HAVE ONE FINAL GUESS REMAINING") 

