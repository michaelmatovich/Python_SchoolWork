# Pwn the Python is an rpg written by Michael J. Matovich
import time
import sys

from textwrap import wrap

def slow_display(sentence):
    for i in sentence:
        print(i, end = "")
        sys.stdout.flush()
        time.sleep(.01)
    return sentence    
    
def introduction():
    
    slow_display("For years the Python has ruled the lands.")
    time.sleep(3)
    print()
    slow_display("The very mention of his name strikes fear into the hearts of even the bravest warriors in the land.")
    time.sleep(3)
    print()
    slow_display("It has been nearly a decade since the mighty KC led an assault on the monstrous beast.")
    time.sleep(3)
    print()
    slow_display("All hope was lost on that dark day... Can you bring light back into this world?")
    time.sleep(3)
    print()
    print("Please enter the name of your hero: ")
    name = input()
    print()
    return name
    




class_nums = ["none","Ranger","Bard","Druid","Warlock","Paladin","Barbarian"]


sentence = ('Pwn the Python')
width = 30

print('+-' + '-' * width + '-+')

for line in wrap(sentence, width):
    print('| {0:^{1}} |'.format(line, width))

print('+-' + '-'*(width) + '-+')

level_one_map = [[1,2,3],[1,2,3]]


#Introduction
# slow_display("For years the Python has ruled the lands.")
# time.sleep(2)
# print()
# slow.display("The very mention of his name strikes fear into the hearts of even the bravest warriors in the land.")
# time.sleep(2)
# slow.display("It has been nearly a decade since the mighty KC led an assault on the monstrous beast.")
# time.sleep(2)
# slow.display("All hope was lost on that dark day... Can you bring light back into this world?")

user_name = introduction()


user_class = 0
# while(user_class != 1 or user_class != 2 or user_class != 3 or user_class != 4 or user_class != 5 or user_class != 6):
print("Please select your class:\n1. Ranger - A master of the bow. Swift, cunning, and deadly at range.\n2. Bard - A virtuoso in combat. Harmless looking, yet wielding melodies of mysterious power. \n3. Druid - Guardians of nature. A lean, green, fighting machine. Unmatched in strength, intelligence, skill, power, looks... basically everything. \n4. Warlock - Artisan of arcane magic. Knows the full power of the dark side. \n5. Paladin - Noble icon of strength, courage, and virtue. The ultimate balanced fighting machine. \n6. Barbarian - Unmatched fighting skill and dexterity, reaching the apex of weapon masteries.")
user_class = input()
print(user_class)

user_class = class_nums[int(user_class)]
current_line = f"On this day, let it be known that the {user_class} {user_name} has accepted the challenge to defeat the Mighty Python!"
slow_display(current_line)









