#!/usr/bin/env python3

# dictionary of recommended places to eat in Seattle
foodLocations = {
        "Cheeseburger":"Dicks Drive In",
        "Chicken Wings": "BonChon",
        "Fried Fish": "Seattle Fish Company",
        "Dumplings": "Din Tai Fung",
        "Korean BBQ" : "Meet Korean BBQ",
        "Fillet Mignon": "Purple",
        "Seafood Boil": "Crawfish King",
        "Sushi": "Japonessa Sushi Cocina",
        "Tacos": "Tacos Chukis",
        "American BBQ": "Jack's BBQ"
        }

# putting dictionary keys into a list
foodChoices = foodLocations.keys()

# converting dictionary key list items to lower case
lowerCaseFoodChoices = [x.lower() for x in foodChoices]
print(lowerCaseFoodChoices)

# having user to select their choice based on our suggestions
#userFoodChoice = input("Please select your choice above and we'll recommend places to eat! ").lower()

# validation to see if user inputs right choice
while True:

# having user to select their choice based on our suggestions
    userFoodChoice = input("Please select your choice above and we'll recommend places to eat! ").lower()
    
    # Finding 
    if userFoodChoice == lowerCaseFoodChoices[0]:
        print("Recommendation: " + foodLocations["Cheeseburger"])
        
    if userFoodChoice == lowerCaseFoodChoices[1]:
        print("Recommendation: " + foodLocations["Chicken Wings"])
        
    if userFoodChoice == lowerCaseFoodChoices[2]:
        print("Recommendation: " + foodLocations["Fried Fish"])
        
    if userFoodChoice == lowerCaseFoodChoices[3]:
        print("Recommendation: " + foodLocations["Dumplings"])
        
    if userFoodChoice == lowerCaseFoodChoices[4]:
        print("Recommendation: " + foodLocations["Korean BBQ"])
        
    if userFoodChoice == lowerCaseFoodChoices[5]:
        print("Recommendation: " + foodLocations["Fillet Mignon"])
        
    if userFoodChoice == lowerCaseFoodChoices[6]:
        print("Recommendation: " + foodLocations["Seafood Boil"])
        
    if userFoodChoice == lowerCaseFoodChoices[7]:
        print("Recommendation: " + foodLocations["Sushi"])

    if userFoodChoice == lowerCaseFoodChoices[8]:
        print("Recommendation: " + foodLocations["Tacos"])
        
    if userFoodChoice == lowerCaseFoodChoices[9]:
        print("Recommendation: " + foodLocations["American BBQ"]) 

   # else:
    #    print("Not a valid food choice")
        

