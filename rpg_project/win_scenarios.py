import rpg
import threading
import os

# calling rpg moves
rpg.moves()

# function to determine winner or loser
def decision():
   
    ## Define how a player can win

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
       

    if currentRoom == 'Kitchen' and humanEnergy >= 75:
        print("You ate and gain strength to fight monster")
        print("Your energy level is off the charts! " + str(humanEnergy))

    if currentRoom == 'Master' and 'gun' in inventory:
        demogorgonEnergy -= 25
        print("You shot the demogorgon: " + "Demogorgon Energy Level: " + str(demogorgonEnergy))
        print("You can now escape using the main entrace of the house")


