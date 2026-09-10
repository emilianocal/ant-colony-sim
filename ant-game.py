


# The instructions
# def is used to define a personalized function (like function() in r)
def showInstructions():
    # print the main menu
    print('''
Feed your ant sister simulator
============
Commands:
    go [direction]
    get [item]
    (and a few secret ones)
          ''')


def status():
    print("------------------")
    print(f"Current Room: {currentRoom}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
            room_item = rooms[currentRoom]["item"]
            print(f"You see a {room_item}!")

    print("------------------")

# Creating the inventory so we can have items
inventory   = []

# Trash to get rid of items
trash       = []

# Below I will create a "dictionary" that maps out where 
# rooms are, relative to each other
rooms = {
            "Nest mound"    :   {
                                 "down" : "Entrance",
                                 "item" : "person"
                                },   
            "Entrance"      :   {
                                 "up"   : "Nest mound",
                                 "down" : "Brood Chamber",
                                 "item" : "friend"
                                },
            "Brood Chamber" :   {
                                 "up"   : "Entrance",
                                 "left" : "Food Chamber 1",
                                 "down" : "Food Chamber 2",
                                 "right": "Food Chamber 3",
                                 "item" : "L1 larva"
                                },
            "Food Chamber 1":   {
                                 "back" : "Brood Chamber",
                                 "item" : "fungus"
                                },

            "Food Chamber 2":   {
                                 "up"   : "Brood Chamber",
                                 "down" : "Cemetary",
                                 "item" : "nectar"
                                },
            "Food Chamber 3":   {
                                 "back" : "Brood Chamber",
                                 "item" : "cheeto dust"
                                },

            "Cemetary"      :   {
                                 "up"   : "Food Chamber 2",
                                 "item" : "dead sister"
                                }
        }

# Here is the room that the individual is currently in, player starts in entrance
currentRoom = "Entrance"

showInstructions()


# "while" loop used here to continuously update the individual's location
while True:
    status()
# input() is a function that allows the user to type something 
# that will then affect a future line of code
    move = ''
    while move == '':
        move = input(">")


# split() allows the code to take the move variable from before, and split it into two 
# parts, so that it becomes more usable later to actually do anything
# BUT there could be a case where an item has 2 words "golden sword", so we only want the
# split to occur for the first word and everything else 
    move = move.split(" ", 1)

# the first element is the verb (get, move, etc)
# the second element is the object (sword, north, etc)

    if move[0] == "go":
    # this line says that the movement has to be in the dictionary
        if move[1] in rooms[currentRoom]:
    # then overwrite the currentroom
            currentRoom = rooms[currentRoom][move[1]]
            print(f"You are in {currentRoom}")
        else:
            print(f"You cannot go {move[1]}")

    if move[0] == "get":
# If in the room's dictionary, at the value of the current room & value of key item
# is that value the same as the vaule that the player wants to pick up? If yes, they get it
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
        # append will take whatever is in the parentheses and add it to the inventory list
            inventory.append(move[1])
# the f before the "" means that the curly brackets will be treated as a variable
            print(f"You got a {move[1]}!")
        # now I want to rewrite the room "item" dictionary to remove 
        # the item that the player picked up
            rooms[currentRoom]["item"] = ""
        else:
            print(f"You do not see a {move[1]} here!")

    if move[0] == "call":
        if move[1] in inventory:
            trash.append(move[1])
            print(f"{move[1]} discarded")
        else:
            print("test failed")


# Victory condition 1
    if "nectar" in inventory and currentRoom == "Brood Chamber":
        print("You fed your sister some yummy nectar!")
        print("Look at how happy she is:")
        print("      _.._        ")
        print("    .'    '.      ")
        print("   /•  _   •\     ")
        print("  :          |    ")
        print("  :          |    ")
        print("  |          :    ")
        print("  |          :    ")
        print("   \        /     ")
        print("    `'--..-'      ")
        print("\033[32mYOU WIN!\033[0m")
        break



# Loss condition 1
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "person":
        print("You were squished by a \033[91mperson\033[0m")
        print("   |         J                           ")
        print("   |         J                           ")
        print("   |         J                           ")
        print("   |         J                           ")
        print("   |         |                           ")
        print("   F         |                           ")
        print("   F         I                           ")
        print("   F          7                          ")
        print("  J            ;:.                       ") 
        print(" /   .          ::::...                  ")
        print(" J   :               ::::...             ")
        print(" F   `                       *-..___     ")
        print(" J        ___.....____             `*J   ")
        print(" **----*              **----****---^     ")
        print("                                         ")
        print("                    \/                   ")
        print("       <(###)-(  )(x_x)                  ")
        print("             '//'\                       ")
        print("\033[91mGame Over!\033[0m")
        break

# Loss condition 2
    if "nectar" in inventory and move[0] == "drink" and move[1] == "nectar":
        print("You drank the nectar!")
        print("Your sister won't be able to eat now :(")
        print("\033[91mGame Over!\033[0m")
        break
