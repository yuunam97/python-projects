# Walks the player through a captivating mini-game adventure! 
# In each step of the adventure, the player should be presented
# with 2 or more options on where to go next.

# Mini-RPG with hp(health points) vs npc(non-playing character)

import time
import os
import sys

def start_screen():
    print("==============================")
    print("|      Python Code Soul      |")
    print("==============================")


def dead_screen(self):
    """
    ⠀⠀⠀⠀⠀⠀⣀⣀⣀⠤⠤⠒⠒⠒⠒⠲⠦⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡠⠐⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀
⠀⢀⡶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀
⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄
⢸⠁⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⡏⢠⠁⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⡞⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠤⢀⠀⠀⠀⠀⠀⢀⡠⠀⠘⢆⢻
⡗⡇⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⢀⣀⡠⠖⠒⠒⠢⣄⠁⠀⢀⢀⣠⠞⠉⠑⠢⣜⠀
⢠⠃⠀⠀⠀⠈⣆⠀⠀⠀⠀⢠⣿⡏⠀⠀⠀⢀⣀⠈⠆⠐⠁⠈⡏⠀⠀⢀⣤⡜⡆
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣿⣿⡆⠀⠀⠀⣛⣿⡇⣤⠀⠀⠀⠑⡀⠀⠘⣘⣃⠃
⠀⢇⠀⠀⡀⠀⠀⠀⠀⠀⠀⠸⣇⠙⢦⣀⠀⠈⣉⡴⠃⠀⢀⡴⡆⠳⡤⠤⠆⡇⠀
⠀⠈⣏⠈⠉⢦⡀⠀⠀⠀⠀⠀⠙⠒⠈⠉⠛⡛⣫⠆⠀⢠⣾⣷⣷⠀⠀⠢⢠⠇⠀
⠀⠀⠘⣧⣄⠀⣩⠢⣄⠀⠀⠀⠠⠤⠴⠚⠉⠺⠃⠀⢀⡟⣿⠙⢿⢀⣄⣤⡞⠀⠀
⠀⠀⠀⠀⠙⢳⣬⠀⢼⣷⡀⢄⣤⣤⣴⣦⠴⠁⠀⠐⡜⣆⠸⣆⣘⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠟⠀⠀⠙⣯⠉⠉⢒⣯⣿⠀⠀⠀⠀⠀⠈⠉⠙⠛⠈⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡀⢀⣀⣈⣇⣴⣿⢏⣼⣦⡈⠑⠲⠤⣤⣀⣀⡠⠺⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠉⠉⢻⣵⣿⣿⣿⣿⢷⢠⣤⣀⣈⣀⠈⠜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢣⡀⢀⡀⠀⠙⢿⣿⣿⢏⠎⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠙⠢⣕⣤⠙⠓⢋⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠶⢦⠭⣽⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    """
    print("You died! Game Over!")

def win_screen(self):
    """
     .-'''''-.
   .'    |    '.
  /      |      \
 ;       |       ;
 ;      /|\      ;
  \    / | \    /
   '. /  |  \ .'
     '-..|..-'

    """
    
def console_clear():
    clear = lambda: os.system('cls')
    clear()

def start_page():
    decision = input("What difficulty?: Noob, Meh, Souls \n")
    
    if decision.lower() == "noob":
        print("You chose Noob! You are entering the World of Code Souls")
        time.sleep(1)
        print("Loading the world: ")
    elif decision.lower() == "meh":
        print("You chose Meh! You are entering the World of Code Souls")
        time.sleep(1)
        print("Loading the world: ")
    else:
        print("You chose Souls! You are entering the World of Code Souls")
        time.sleep(1)
        print("Loading the world: ")

# Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    
    # Call in a loop to create terminal progress bar
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # Print New Line on Complete
    if iteration == total: 
        print()

def introduction():
    
    print("You are in the World of Python Code Souls, filled with lots of adventures and fun! \n")
    time.sleep(1)

    print("Objective: You have to defeat the evil Wizard and save the world! \n")
    time.sleep(1)

    print("You woke up as a Warrior in a dungeon, a classic class that is adept at navigating this forsaken world. \n")
    time.sleep(1)

    print("You see a door straight ahead, a chest on the left and a way downstairs on the right. \n")
    time.sleep(1)

def option_chest():
    print("You found a Durandal, the legendary sword!")
    time.sleep(1)
    print("You picked up the sword and put it in your inventory")
    time.sleep(1)
    
    next = input("What do you want to do next? (Open Door/Go Downstairs) \n")
    if next.lower() == "open door":
        option_door()
    elif next.lower() == "go downstairs":
        final_boss()

def option_door():
    print("You opened the door and found a room full of monsters!")
    time.sleep(1)

    activation = input("Do you wanna fight them? (Yes/No) \n")
    if activation.lower() == "yes" and inventory > 0:
        print("You used your Durandal and sliced through the monster like it's a piece of butter! \n")
        time.sleep(1)
        print("You gained 1000 exp!")
        time.sleep(1)
        print("You leveled up!")
        time.sleep(1)
        print("You learned 'Magic Beam'!")
        time.sleep(2)
        final_boss()
    elif activation.lower() == "yes" and inventory == 0:
        print("You used your bare hands and tried to bulldoze through the monsters! \n")
        time.sleep(1)
        print("However, you failed!")
        time.sleep(1)
        print("You died!")
        time.sleep(1)
        print("Game Over!")
        time.sleep(1)
        print(dead_screen.__doc__)
        time.sleep(2)
        restart()
    elif activation.lower() == "no":
        print("You tried to run away but the monsters caught you!")
        time.sleep(1)
        print(dead_screen.__doc__)
        time.sleep(2)
        restart()
    else:
        print("Oops! Your warrior is super confused! Please try again.")
        option_door()

def final_boss():
    print("You went downstairs and face a boss named 'Zuck, the ordained Lizard'!")
    
    if inventory > 0: 
        attack = input("What do you do? (Attack/Magic Beam/Run Away) \n")
        if attack.lower() == "attack":
            print("You attacked Zuck with your Durandal, he bleeds and withers in fear!!")
            time.sleep(1)
            attack1 = input("What do you do next? (Magic Beam/Run Away) \n")
            if attack1.lower() == "magic beam":
                print("You used magic beam and Zuck got obliterated!")
                time.sleep(1)
                print("You defeated Zuck and saved the world!")
                time.sleep(1)
                print("You won!")
                print(win_screen.__doc__)
                restart()   

            elif attack1.lower() == "run away":
                print("You tried to run away but Zuck caught you!")
                time.sleep(1)
                print(dead_screen.__doc__)
                time.sleep(2)
                restart()
            else:
                print("Oops! Your warrior is super confused! Please try again.")
                final_boss()

        elif attack.lower() == "magic beam":
            print("You used magic beam and Zuck got a big gaping hole in his chest!")
            time.sleep(1)
            attack1 = input("What do you do next? (Attack/Run Away) \n")
            if attack1.lower() == "attack":
                print("You attacked Zuck with your Durandal, he bleeds and withers in fear!!")
                time.sleep(1)
                print("You defeated Zuck and saved the world!")
                time.sleep(1)
                print("You won!")
                print(win_screen.__doc__)

            elif attack1.lower() == "run away":
                print("You tried to run away but Zuck caught you!")
                time.sleep(1)
                print(dead_screen.__doc__)
                time.sleep(2)
                restart()

            else:
                print("Oops! Your warrior is super confused! Please try again.")
                final_boss()

        elif attack.lower() == "run away":
            print("You tried to run away but Zuck caught you!")
            time.sleep(1)
            print(dead_screen.__doc__)
            time.sleep(2)
            final_boss()

        else:
            print("Oops! Your warrior is super confused! Please try again.")
            final_boss()
    
    if inventory == 0:
        attack = input("What do you do? (Attack/Run Away) \n")
        if attack.lower() == "attack":
            print("You attacked Zuck with your bare hands, he bleeds!!")
            time.sleep(1)

            attack1 = input("What do you do next? (Attack/Run Away) \n")
            if attack1.lower() == "attack":
                print("You tried attack Zuck, but he evades and slices you in half!")
                time.sleep(1)
                print("You Lose!")
                print(dead_screen.__doc__)
                restart()
                
            elif attack1.lower() == "run away":
                print("You tried to run away but Zuck caught you!")
                time.sleep(1)
                print(dead_screen.__doc__)
                time.sleep(2)
                restart()

            else:
                print("Oops! Your warrior is super confused! Please try again.")
                final_boss()

        elif attack1.lower() == "run away":
                print("You tried to run away but Zuck caught you!")
                time.sleep(1)
                print(dead_screen.__doc__)
                time.sleep(2)
                restart()
        else:
            print("Oops! Your warrior is super confused! Please try again.")
            final_boss()

    elif attack.lower() == "run away":
        print("You tried to run away but Zuck caught you!")
        time.sleep(1)
        print(dead_screen.__doc__)
        time.sleep(2)
        restart()

    else:
        print("Oops! Your warrior is super confused! Please try again.")
        final_boss()

def restart():
    print("Restarting the game...")
    restart = input("Do you want to restart the game? (Yes/No) \n")
    if restart.lower() == "yes":
        console_clear()
        start_screen()
        progressbar()
        introduction()
        inventory = 0

        door = input("what do you want to do? (Open Chest/Open Door/Go Downstairs) \n")
        time.sleep(2)

        while door.lower() != "open chest" and door.lower() != "open door" and door.lower() != "go downstairs":
            print("Oops! Your warrior is super confused! Please try again.")
            door = input("what do you want to do? (Open Chest/Open Door/Go Downstairs) \n")
            time.sleep(2)

        if door.lower() == "open chest":
            console_clear()
            inventory += 1
            option_chest()
        elif door.lower() == "open door":
            console_clear()
            option_door()
        elif door.lower() == "go downstairs":
            console_clear()
            final_boss()

    elif restart.lower() == "no":
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Oops! Your warrior is super confused! Please try again.")
        restart()


start_screen()
start_page()

# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.05)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

time.sleep(2)
console_clear()

introduction()

inventory = 0

door = input("what do you want to do? (Open Chest/Open Door/Go Downstairs) \n")
time.sleep(2)

while door.lower() != "open chest" and door.lower() != "open door" and door.lower() != "go downstairs":
    print("Oops! Your warrior is super confused! Please try again.")
    door = input("what do you want to do? (Open Chest/Open Door/Go Downstairs) \n")
    time.sleep(2)

if door.lower() == "open chest":
    console_clear()
    inventory += 1
    option_chest()
elif door.lower() == "open door":
    console_clear()
    option_door()
elif door.lower() == "go downstairs":
    console_clear()
    final_boss()