import time
import random

# get a random weapon
weapon = random.choice(['powerful sword', 'bow and arrow', 'large spear'])
# get a random monster
monster = random.choice(['dragon', 'ogre', 'witch'])

# start with just a dagger
items = ['dagger']


# print text with a pause
def print_pause(prompt):
    print(prompt)
    time.sleep(2)


# check for valid input
def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            return choice
        elif option2 in choice:
            return choice
        else:
            print_pause("Sorry, I don't understand.")


# intro prompt
def intro():
    print_pause("You find yourself standing in the middle of a forest.")
    print_pause("You've recently heard a rumor that there is a chest"
                "full of riches hidden somewhere within these woods.")
    print_pause("On your hip is your trusty dagger."
                " It's pretty rusted and has a crack in the blade,"
                "ready to break any minute.")
    two_paths()


# describe the two paths and have the player choose one
def two_paths():
    print_pause("In front of you is a shabby cabin.")
    print_pause("To your left is a cave entrance.")
    print_pause("Enter 1 to knock on the door of the cabin.")
    print_pause("Enter 2 to enter the cave.")
    choice = valid_input("What would you like to do?\n(Please enter 1 or 2)\n",
                         '1', '2')
    if choice == '1':
        cabin()
    elif choice == '2':
        cave()


# enter the cabin and find a weapon
def cabin():
    print_pause("You knock on the door.")
    print_pause("With no response, you enter the cabin and"
                "begin looking around.")
    if weapon in items:
        print_pause("You've been here before, and there is nothing interesting"
                    "left in the cabin.")
        print_pause("You walk out of the cabin and back into the forest.")
        two_paths()
    else:
        print_pause("While searching the cabin, something in the corner "
                    "of the room catch your eye.")
        print_pause(f"You've found a {weapon}! ")
        print_pause(f"You quickly ditch your dagger and pick up"
                    "the new weapon.")
        items.append(weapon)
        print_pause("You walk out of the cabin and back into the forest.")
        two_paths()


# enter the cave and encounter a monster in front of the treasure
def cave():
    print_pause("You cautiously enter the cave.")
    print_pause("Walking towards the back of the cave, "
                "you can see a glistening light. ")
    print_pause("The light is coming from a treasure chest. "
                "You've found it!")
    print_pause(f"As you approach the chest, a {monster} "
                "appears and attacks you!")

    if weapon not in items:
        print_pause("You feel a bit unprepared for a fight "
                    "with your little dagger.")

    choice = valid_input("What would you like to (1) fight or (2) run away?\n",
                         '1', '2')
    if choice == '1':
        fight()
    elif choice == '2':
        run_away()


def fight():
    if weapon in items:
        print_pause(f"You attack the {monster} with your {weapon}.")
        die_roll = random.randint(1, 6)
        if die_roll <= 3:
            print_pause(f"Your attack damaged the {monster} and "
                        "they stumble back. "
                        "You take the opportunity to strike again.")
            print_pause(f"The second hit defeated the {monster} entirely!")
        else:
            print_pause(f"It deals critical damage, defeating the {monster}!")
        print_pause("You are victorious and the treasure is yours!")
        play_again()
    else:
        print_pause(f"Your dagger was no match for the {monster}.")
        print_pause("You have been defeated.")
        play_again()


def run_away():
    print_pause("You quickly run out of the cave and back into the forest.")
    print_pause("You do not appear to have been followed.")
    two_paths()


def play_again():
    choice = valid_input("Would you like to play again? (y/n)\n", 'y', 'n')
    if choice == 'y':
        print_pause("Great! Restarting the game now...")
        items.remove(weapon)
        play_game()
    elif choice == 'n':
        print_pause("Thanks for playing!")


def play_game():
    intro()


play_game()
