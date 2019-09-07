# Program by Jonathan Kleehammer
# September 7th 2019
# Program is designed to randomly choose abilities for skill checks and saving throws
# The idea is that I feel like I was using a lot of similar skills while ignoring others
# By randomly choosing skills I try to work them into my sessions so that all skills are represented

import random

# strength skills
str = {
    'name': 'strength',
    'skills': ['athletics']
}
# dexterity skills
dex = {
    'name': 'dexterity',
    'skills': ['acrobatics', 'sleight of hand', 'stealth']
}
# constitution "skills"
con = {
    'name': 'constitution',
    'skills': []
}
# intelligence skills
int = {
    'name': 'intelligience',
    'skills': ['arcana', 'history', 'investigation', 'nature', 'religion']
}
# wisdom skills
wis = {
    'name': 'wisdom',
    'skills': ['animal handling', 'insight', 'medicine', 'perception', 'survival']
}
# charisma skills
cha = {
    'name': 'charisma',
    'skills': ['deception', 'intimidation', 'performance', 'persuasion']
}

# putting all the abilities and their skills into an array of abilities
abilities = [str, dex, con, int, wis, cha]

# Getting input from user? Just press enter to use default
# TODO: implement this, leaving it out for faster testing
print("How many saving throws and skill checks would you like? (default: 1 3)")
saveCount = 1
skillCount = 3

# equal probabilty for everything? Hmm... This might be changed later

# generate our requested number of saves
randomSaves = []
for i in range(saveCount):
    saveIndex = random.randrange(0, len(abilities), 1)
    saveName = abilities[saveIndex]['name']

# creating a list of all skills
# TODO: We may want to implement different probabilities for each skill
allSkills = []
for i in range(len(abilities)):
    for j in range(len(abilities[i]['skills'])):
        skill = abilities[i]['skills'][j]
        allSkills.append(abilities[i]['skills'][j])
