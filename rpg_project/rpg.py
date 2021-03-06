#!/usr/bin/python3

import random

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
  print("All enery levels measured in percentage")

def showStatus():
  
  #print the player's current status
  print('----------------------------------')
  print('You are in the ' + currentRoom)

  # print room directions
  print('North: ' + rooms[currentRoom]['north'])
  print('South: ' + rooms[currentRoom]['south'])
  print('East: ' + rooms[currentRoom]['east'])
  print('West: ' + rooms[currentRoom]['west'])

  print("")
  for x in rooms[currentRoom]["edibles"]:
    print('Edibles: ' + x)

  print() 
  print(rooms[currentRoom]["description"])

  print()

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
                  'north' : '',
                  'item'  : ['key','statue'],
                  'edibles' : [],
                  'description': 'Description: Starting point of the game',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : '',
                  'west'  : 'Master',
                  'east'  : 'Dining Room',
                  'item'  : ['knife','bowl','lighter'],
                  'edibles' : ['steak','chicken','beans', 'rice', 'eggs'],
                  'description': 'Description: Contains edibles and inedibles. Player has to pick edibles to eat to gain energy',   
                },
            'Dining Room' : {
                  'east' : '',
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'north' : 'Pantry',
                  'item'  : ['potion','fruits','plates','chair','table'],
                  'edibles' : [],
                  'description': 'Description: Neutral ground where player can also pick potion for treatment and fruits to stay healthy',
               },
            'Garden' : {
                  'east' : '',
                  'west'  : '',
                  'south' : '',
                  'north' : 'Dining Room',
                  'item'  : ['shovel','wheelbarrow'],
                  'edibles' : [],
                  'description': 'Description: Must get key and potion in inventory to win',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'east' : '',
                  'west'  : '',
                  'north' : '',
                  'item'  : ['cookie','chips','beans', 'spaghetti', 'dog food','secret hideout'],
                  'edibles' : [],
                  'description': 'Description: This has a secret hideout and player can access to hide',
            },
            'Master' : {
                   'east' : 'Hall',
                   'south': 'Kitchen',
                   'north' : '',
                   'west' : '', 
                   'item' : ['purse', 'gun','shoe','pants'],
                   'edibles' : [],
                   'description': 'Description: Has a gun! Player can decide to type command shoot gun to fight the demogorgon',
            },
            'Balcony' : {
                   'north' : 'Hall',
                   'south' : 'Master',
                   'east'  : 'Dining',
                   'west' : '',
                   'item'  : ['chair','table','ludo game', 'rope'],
                   'edibles' : [],
                   'description': 'Description: Has a rope to flee building',

            },
            'Living Room'  : {
                   'south' : 'Kitchen',
                   'north' : '',
                   'east'  : '',
                   'west'  : '',
                   'item'  : ['Television','painting','PlayStation','XBOX', 'demogorgon'],
                   'edibles' : [],
                   'description': 'Description: This part of house is occupied by the demogorgon. Do not enter or teleport',

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
        # here's the problem-- when you use "del" to get rid of item, you get rid of the whole key pair
        # try .remove instead
        rooms[currentRoom]['item'].remove(move[1])
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
      if currentRoom == "Master" and "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] == 'gun':
        # decide to shoot the demogorgon with a specified period of time
        print("SHOOOOOOOT!")
        demogorgonEnergy -= 25
        print("Demogorgon energy: " + str(demogorgonEnergy))
      else:
        humanEnergy -=15
        print("your energy: " + str(humanEnergy))
        print("you got overpowered")

    # Teleport: This randomly takes the user anywhere and their faith is unknown :) 
    if move[0] == 'teleport' and move[1] == 'to':
      currentRoom = random.choice(list(rooms.keys()))
      print("You Teleported")
      print(currentRoom)

    #Win scenarios
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
      print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
      break

    # if in the garden and player has key and a potion, they excape
    if currentRoom == 'Garden' and not 'key' in inventory and not 'potion' in inventory:
      print("You didn't get a key or potion")
      print("The beast got you...")
      break

    # in any situation if humanEnergy is greater than 75 percent they'll win
    if humanEnergy >= 75:
      print("You ate and gain strength to fight monster")
      print("Your energy level is off the charts! " + str(humanEnergy))
      print("You overpowered the demogorgon. You WIN!!!!!!!")
      break

    # if the player is in kichen and want to eat something that's not available to eat they lose and their energy goes dowm
    if humanEnergy < 50:
      print("You dont have energy to fight")
      print("You got eaten by the demogorgon")
      print("You LOST!!")
      break

    # if player in master and has gun in inventory, if the player types shoot gun, they win
    if demogorgonEnergy <= 25:
        
        print("You shot the demogorgon: " + "Demogorgon Energy Level: " + str(demogorgonEnergy))
        print("You WIN!!!")
        print("You can now escape using the main entrace of the house")
        break
    
    # if currentRoom == 'Master' and demogorgonEnergy > humanEnergy:
    #   print("You lost!")
    #   print("You energy is " + humanEnergy + " is less than " + demogorgonEnergy)

   

        
moves()
