# DnDAbilityRoller
## Program for personal use
A program to randomly select 'm' saving throws and 'n' skill checks from the available skill checks and saving throws from Dungeons and Dragons 5th edition

### The Problem
I felt that my sessions were using a lot of the same skill checks such as persuasion or perception, while simultaneously other skills were hardly ever used such as sleight of hand or performance.
To help with this I created this program to randomly select skills and saving throws for me to try to work into my sessions.

I created this program to help diversify the skills and saving throws I use in my dungeons and dragons sessions as the DM.

For instance, soon the party will be speaking with someone of high status, requiring them to do a performance check to see how well they can follow the high standards for manners while talking to someone of high status is an idea I thought of while trying to use the skills that I haven't been using as much


### Running the program

To run the program download the 'DnDAbilityRoller.py' file
With a terminal move into the same directory as the .py file
You can run the program with either python or python3 via the following commands

`python AbilityRoller.py`

`python3 AbilityRoller.py`

Using the previous commands will use the default values of how many ability saves and skill checks to generate, if you would like to specify how many of each you'd like to use then you can pass in 2 additional arguments (first agument is the number of saves, 2nd argument is the number of skill checks). For Example:

`python AbilityRoller.py 2 6`

The previous command will generate 2 ability saves and 6 skills

### Example Output
```
Try to use these saves next session!
['constitution']

Try to use these skills next session!
['performance', 'religion', 'acrobatics']
```
