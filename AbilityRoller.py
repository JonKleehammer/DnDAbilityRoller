# Program by Jonathan Kleehammer
# September 7th 2019
# Program is designed to randomly choose abilities for skill checks and saving throws
# The idea is that I feel like I was using a lot of similar skills while ignoring others
# By randomly choosing skills I try to work them into my sessions so that all skills are represented

import random
import sys

# strength skills
strength = {
    'name': 'strength',
    'skills': ['athletics']
}
# dexterity skills
dexterity = {
    'name': 'dexterity',
    'skills': ['acrobatics', 'sleight of hand', 'stealth']
}
# constitution "skills"
constitution = {
    'name': 'constitution',
    'skills': []
}
# intelligence skills
intelligence = {
    'name': 'intelligience',
    'skills': ['arcana', 'history', 'investigation', 'nature', 'religion']
}
# wisdom skills
wisdom = {
    'name': 'wisdom',
    'skills': ['animal handling', 'insight', 'medicine', 'perception', 'survival']
}
# charisma skills
charisma = {
    'name': 'charisma',
    'skills': ['deception', 'intimidation', 'performance', 'persuasion']
}

# putting all the abilities and their skills into an array of abilities
abilities = [strength, dexterity, constitution, intelligence, wisdom, charisma]

# generating a list of skills based on the previous data
allSkills = []
for i in range(len(abilities)):
    for j in range(len(abilities[i]['skills'])):
        skill = abilities[i]['skills'][j]
        allSkills.append(abilities[i]['skills'][j])

# Getting input from user? Just press enter to use default
saveCount = 1
skillCount = 3

if len(sys.argv) == 3:
    saveCount = int(sys.argv[1])
    skillCount = int(sys.argv[2])

    # ensuring that we aren't generating more abilities than how many exist
    if saveCount > len(abilities):
        print("Requested more ability saves than what exists, we will return all saves")
        saveCount = len(abilities)

    # ensuring that we aren't generating more skills than how many exist
    if skillCount > len(allSkills):
        print("Requested more skills than what exists, we will return all skills")
        skillCount = len(allSkills)
elif len(sys.argv) != 1:
    print("Incorrect usage, use 0 arguments for default values or 2 arguments to choose")
    exit(1)

# equal probabilty for everything? Hmm... This might be changed later

# generate our requested number of saves
randomSaves = []
for i in range(saveCount):
    while 1:
        saveIndex = random.randrange(0, len(abilities), 1)
        saveName = abilities[saveIndex]['name']
        if saveName not in randomSaves:
            break
    randomSaves.append(saveName)

# creating a list of all skills
# TODO: We may want to implement different probabilities for each skill


# picking skills randomly from the list of all skills
randomSkills = []
for i in range(skillCount):
    while 1:
        skillIndex = random.randrange(0, len(allSkills), 1)
        skillName = allSkills[skillIndex]
        if skillName not in randomSkills:
            break
    randomSkills.append(skillName)

print("Try to use these saves next session!")
print(randomSaves)
print("\nTry to use these skills next session!")
print(randomSkills)
