from room import Room
from player import Player 
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

axe = Item('axe', 'cut stuff')
sword = Item('sword', 'a long knife')
gold = Item('gold', 'one of the precious elements')
diamond = Item('diamond', 'one of the precious elements')
ruby = Item('ruby', 'one of the precious elements')

room['foyer'].item.append(axe)
room['treasure'].item.append(gold)
room['treasure'].item.append(diamond)
room['outside'].item.append(sword)

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside']) # setting player's initial location
player_item = player.item
room_item = player.location.item
# print('Welcome to my adventure game')
# print('You will move from room to room using the "wasd" keys')
# print('If you wish to quit: just press "q"')

# print(room_item)
print(player.location)
print('Your Items:', player.item)

# user choices
def get_item():
    for r_item in room_item:
        gotten_item = input('Get item from this room? Get: (press [Enter] or type "no" to skip) ')
        if gotten_item == '' or gotten_item == 'no':
            pass
        elif gotten_item == r_item.name:
            (player_item).append(gotten_item)
            room_item.remove(r_item)
            print(player_item)
        else:
            print('pick again')
            get_item()

def drop_item():
    print('Your inventory: ', player_item)
    dropped_item = input("Would you like to drop item from inventory?: ")
    if dropped_item == '' or dropped_item == 'no':
        pass
    else:
        for item in player_item:
            if dropped_item == item:
                player_item.remove(dropped_item)
                room_item.append(dropped_item)
            else:
                print('not part of inventory')
                drop_item()
                
get_item()
user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
# Write a loop that:
#
while not user == 'q':
    if user == 'w':
        try:
            player.location = player.location.n_to
            print(player.location)
            print('Your Items:', player_item)
        except:
            print('choose another direction')
        get_item()
        drop_item()
        user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 's':
        try:
            player.location = player.location.s_to
            print(player.location)
            print('Your Items:', player_item)
        except:
            print('choose another direction')
        get_item()
        drop_item()
        user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 'd':
        try:
            player.location = player.location.e_to
            print(player.location)
            print('Your Items:', player_item)
        except:
            print('choose another direction')
        get_item()
        drop_item()
        user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 'a':
        try:
            player.location = player.location.w_to
            print(player.location)
            print('Your Items:', player_item)
        except:
            print('choose another direction')
        get_item()
        drop_item()
        user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    else:
        print('Not a direction')
        user = input("[w] North  [s] South  [d] East  [a] West  [q] Quit\n")
print('game over')
        
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
