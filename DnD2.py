import random
#Lists
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', \
'Ranger', 'Rogue', 'Sorcerer', 'Wizard']
races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-elf', 'Half-orc']
names = ['Alex', 'Chris', 'Renee', 'Jordan', 'Aaron']
gender = ['Male', 'Female']
class_description = {
    'Barbarian': 'text',
    'Bard':'text',
    'Cleric':'text', 
    'Druid':'text',
    'Fighter':'text',
    'Monk':'text',
    'Paladin':'text', 
    'Ranger':'text',
    'Rogue':'text',
    'Sorcerer':'text',
    'Wizard':'text'
    }
    #p21

#Dice code 
def die():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    rolls = [dice1, dice2, dice3, dice4]
    rolls.remove(min(rolls))
    final = sum(rolls)
    return final

#Player dictionary 
player = {
'Name': random.choice(names),
'Gender': random.choice(gender),
'Class': random.choice(classes),
'Race': random.choice(races),
'Gold': 0,
   #Abilities subdictionary  
    "Abilities": {
        'Strength': die(),
        'Dexterity': die(),
        'Constitution': die(),
        'Intelligence': die(),
        'Wisdom': die(),
        'Charisma': die() 
            }
}

#Gold
current_class = player["Class"]
if current_class == 'Barbarian':
    for i in range(4):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Bard':
    for i in range(4):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10 
if current_class == 'Cleric':
    for i in range(5):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Druid':
    for i in range(2):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Fighter':
    for i in range(6):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Monk':
    for i in range(5):
        player['Gold'] += random.randint(1,4)
if current_class == 'Paladin':
    for i in range(6):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Ranger':
    for i in range(6):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Rogue':
    for i in range(5):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Sorcerer':
    for i in range(3):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10
if current_class == 'Wizard':
    for i in range(3):
        player['Gold'] += random.randint(1,4)
    player['Gold'] *= 10

#Abilities 
current_race = player["Race"]
if current_race == 'Dwarf':
    player['Abilities']['Constitution'] += 2
    player['Abilities']['Charisma'] -= 2
if current_race == 'Elf':
    player['Abilities']['Dexterity'] += 2
    player['Abilities']['Strength'] -= 2
if current_race == 'Half-orc':
    player['Abilities']['Strength'] += 2
    player['Abilities']['Intelligence'] -= 2
    player['Abilities']['Charisma'] -= 2
if current_race == 'Halfling':
    player['Abilities']['Dexterity'] += 2
    player['Abilities']['Strength'] -= 2
    
#Printing everything  
print "Name: " + player['Name']
print "Gender: " + player['Gender']
print "Class: " + player['Class'] 
print class_description[player['Class']]
print "Race: " + player['Race']
print "Gold: " + str(player['Gold'])
print "Strength: " + str(player["Abilities"]['Strength'])
print "Dexterity: " + str(player["Abilities"]['Dexterity'])
print "Constitution: " + str(player["Abilities"]['Constitution'])
print "Intelligence: " + str(player["Abilities"]['Intelligence'])
print "Wisdom: " + str(player["Abilities"]['Wisdom'])
print "Charisma: " + str(player["Abilities"]['Charisma'])
