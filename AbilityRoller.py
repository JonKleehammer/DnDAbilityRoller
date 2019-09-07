# Program by Jonathan Kleehammer
# September 7th 2019
# Program is designed to randomly choose abilities for skill checks and saving throws
# The idea is that I feel like I was using a lot of similar skills while ignoring others
# By randomly choosing skills I try to work them into my sessions so that all skills are represented

# strength skills
str = {'athletics'}
# dexterity skills
dex = {'acrobatics', 'sleight of hand', 'stealth'}
# constitution "skills"
con = {}
# intelligence skills
int = {'arcana', 'history', 'investigation', 'nature', 'religion'}
# wisdom skills
wis = {'animal handling', 'insight', 'medicine', 'perception', 'survival'}
# charisma skills
cha = {'deception', 'intimidation', 'performance', 'persuasion'}

# putting all the abilities and their skills into an array of abilities
abilities = {str, dex, con, int, wis, cha}

# Getting input from user? Just press enter to use default
# TODO: implement this, leaving it out for faster testing
print("How many saving throws and skill checks would you like? (default: 1 3)")
saveCount = 1
skillCount = 3
