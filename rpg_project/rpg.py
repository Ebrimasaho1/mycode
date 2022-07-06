#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  for items in rooms[currentRoom]["item"]:
    print("You see a " + items)

    print("---------------------------")

#an inventory, which is initially empty
inventory = []

# default energy for human and demogorgon
# defining a variable and declaring it global are two different things.
humanEnergy = 50
demogorgonEnergy = 50

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Master',
                  'item'  : ['key','statue'],
                  'edibles' : [],
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'west'  : 'Master',
                  'East'  : 'Dining Room',
                  'item'  : ['knife','bowl','lighter'],
                  'edibles' : ['steak','chicken','beans', 'rice', 'eggs']
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'north' : 'Pantry',
                  'item'  : ['potion','fruits','plates','chair','table'],
                  'edibles' : [],
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item'  : ['shovel','wheelbarrow'],
                  'edibles' : [],
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item'  : ['cookie','chips','beans', 'spaghetti', 'dog food'],
                  'edibles' : [],
            },
            'Master' : {
                   'east' : 'Hall',
                   'South': 'Kitchen', 
                   'item' : ['purse', 'gun','shoe','pants'],
                   'edibles' : [],
                   
            },
            'Balcony' : {
                   'North' : 'Hall',
                   'South' : 'Master',
                   'East'  : 'Dining',
                   'item'  : ['chair','table','ludo game'],
                   'edibles' : [],
            },
            'Living Room'  : {
                   'South' : 'Kitchen',
                   'item'  : ['Television','painting','PlayStation','XBOX'],
                   'edibles' : [],
            },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
def moves():
  # we need the moves() function to treat these variables globally
  # so we declare them as global here
  global currentRoom
  global inventory
  global rooms
  global demogorgonEnergy
  global humanEnergy

  while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
      move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
      #check that they are allowed wherever they want to go
      if move[1] in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
      #there is no door (link) to the new room
      else:
          print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
      #if the room contains an item, and the item is the one they want to get
      if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
        inventory += [move[1]]
        #display a helpful message
        print(move[1] + ' got!')
        #delete the item from the room
        del rooms[currentRoom]['item']
      #otherwise, if the item isn't there to get
      else:
        #tell them they can't get it
        print('Can\'t get ' + move[1] + '!')

    #if they type "eat first
    if move[0] == 'eat' :
        # check if current room is kitchen and they have items in kitchen to cook
        if currentRoom == "Kitchen" and move[1] in rooms[currentRoom]['edibles']:
            humanEnergy += 25
            print("You ate " + move[1] + " and have " + str(humanEnergy) + " percent energy" + " to run away from the demogorgon")
              
      
        # else, you meed to restock to be able to cook
        else:
            humanEnergy -= 15
            print(move[1] + " not available to eat!" " Energy level " + str(humanEnergy))
            print("You don't have enough energy to run")
            print("The demogorgon got you")

    # master bedroom scanario
    if move[0] == 'shoot':
      # check if the current room is the master and check if the person gets a gun
      if currentRoom == "Master" and "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        # decide to shoot the demogorgon with a specified period of time
        print("SHOOOOOOOT!")
        print("")

    

