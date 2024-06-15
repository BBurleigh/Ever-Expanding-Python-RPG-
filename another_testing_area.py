world_map_location = " "
local_area_location = " "
in_world_map = True

playerCharacter = ["Rocco Taco", "golden floof", 10, 10, 1, 3, 4, 2, 5, 4, 4, 2]
playerInventory = ["Berries", "Berries", "Rocks"]
currentPosition = " "

world_map = [["P", " ", " ", "To"]]

town_map =[[" ", "m", "h1", "g"],
           ["h2", " ", " ", "a"],
           ["h3", " ", " ", "c"],
           [" ", "e", " ", " "]]

current_map = world_map

def chooseMap():
    global current_map
    global world_map
    global town_map
    if (world_map_location == "To"):
        current_map = town_map
        
def playerActions():
    global in_world_map
    if (in_world_map == True):
        print("---------------------------------------------------------------------------")
        print("\nWorld Map: " + str(world_map))
        print("\nPlayer Stats: " + playerCharacter[0] + "   Class: " + playerCharacter[1] + "  Level: " + str(playerCharacter[4]) + "  HP: " + str(playerCharacter[2]) + "  MP: " + str(playerCharacter[3]))
        print("              | Str " + str(playerCharacter[5]) + " | Dex " + str(playerCharacter[6]) + " | Int " + str(playerCharacter[7]) + " | Agi " + str(playerCharacter[8]) + " | Luck " + str(playerCharacter[9]) + " | Con " + str(playerCharacter[10]) + " | Will " + str(playerCharacter[11]) + "|")
        print("\nPlayer Inventory: " + str(playerInventory) + "\n")
        print("+--------------------------------------------+")
        print("| Go West | Go East | Investigate | Use Item |")
        print("+--------------------------------------------+")
        playerChoice = input("Based on your choices, what do you plan on doing? \n Input: ")
        if (playerChoice == "Go West") or (playerChoice == "GO WEST") or (playerChoice == "go west"):
            travelWest()
        elif (playerChoice == "Go East") or (playerChoice == "GO EAST") or (playerChoice == "go east"):
            travelEast()
        elif (playerChoice == "Investigate") or (playerChoice == "INVESTIGATE") or (playerChoice == "investigate"):
            investigate()
        # elif (playerChoice == "Use Item") or (playerChoice == "USE ITEM") or (playerChoice == "use item"):
        #     useItem()
        else:
            print("That's not an option, whether you are thinking of something silly or incoherently (you spelled something incorrectly). \n")
            playerActions()
    elif(in_world_map == False):
        global current_map
        print("---------------------------------------------------------------------------")
        print("\nLocal Map: " + str(current_map))
        print("\nPlayer Stats: " + playerCharacter[0] + "   Class: " + playerCharacter[1] + "  Level: " + str(playerCharacter[4]) + "  HP: " + str(playerCharacter[2]) + "  MP: " + str(playerCharacter[3]))
        print("              | Str " + str(playerCharacter[5]) + " | Dex " + str(playerCharacter[6]) + " | Int " + str(playerCharacter[7]) + " | Agi " + str(playerCharacter[8]) + " | Luck " + str(playerCharacter[9]) + " | Con " + str(playerCharacter[10]) + " | Will " + str(playerCharacter[11]) + "|")
        print("\nPlayer Inventory: " + str(playerInventory) + "\n")
        print("+---------------------------------------------------------------------------------------+")
        print("| Go West | Go East | Go North | Use South | Enter Building | Use Item | Observe | Exit |")
        print("+---------------------------------------------------------------------------------------+")
        playerChoice = input("Based on your choices, what do you plan on doing? \n Input: ")
        if (playerChoice == "Go West") or (playerChoice == "GO WEST") or (playerChoice == "go west"):
            travelWest()
        elif (playerChoice == "Go East") or (playerChoice == "GO EAST") or (playerChoice == "go east"):
            travelEast()
        # elif (playerChoice == "Go North") or (playerChoice == "GO NORTH") or (playerChoice == "go north"):
        #     travelNorth()
        # elif (playerChoice == "Go South") or (playerChoice == "GO SOUTH") or (playerChoice == "go south"):
        #     travelSouth()
        # elif (playerChoice == "Enter Building") or (playerChoice == "ENTER BUILDING") or (playerChoice == "enter building"):
        #     enterBuilding()
        # elif (playerChoice == "Use Item") or (playerChoice == "USE ITEM") or (playerChoice == "use item"):
        #     useItem()
        elif (playerChoice == "Observe") or (playerChoice == "OBSERVE") or (playerChoice == "observe"):
            observe()
        elif (playerChoice == "Exit") or (playerChoice == "EXIT") or (playerChoice == "exit"):
            chooseMap()
        else:
            print("That's not an option, whether you are thinking of something silly or incoherently (you spelled something incorrectly). \n")
            playerActions()
        
def travelWest():
    global currentPosition
    position = world_map.index("P")
    if (position == 0):
        print("\n There is nothing beyond this point. You cannot travel further west. \n")
        playerActions()
    if (position > 0 ):
        nextArea = world_map[position - 1]
        world_map[position - 1] = "P"
        world_map[position] = currentPosition
        currentPosition = nextArea
        print("\nYou travel a little west before stopping to take a rest.")
        playerActions()
        
def travelEast():
    global currentPosition
    for x in len(world_map):
        for y in len(world_map[x]):
            if(world_map[x][y] == "P"):
                position = world_map[x][y].index("P")
                print(position)
        if (position < len(world_map[x]) - 1):
            print(len(world_map[x]))
            nextArea = world_map[x][position + 1]
            world_map[x][position + 1] = "P"
            world_map[x][position] = currentPosition
            currentPosition = nextArea
            print("\nYou travel a little east before stopping to take a rest.")
            playerActions()
        elif (position == len(world_map[x]) - 1):
            print("\n There is nothing beyond this point. You cannot travel further east. \n")
            playerActions()
        
    
        
def investigate():
    global currentPosition
    global in_world_map
    if (in_world_map == True):
        if (currentPosition == " ") or (currentPosition == "F"):
            # randomEvent()
            print("You're in the plains. Or a forest. It doesn't matter.")
        # elif (currentPosition == "H"):
        #     print("You have stumbled upon the witch's hut!\n")
        #     witchHutEvent()
        elif (currentPosition == "To"):
            enterTown = input("You approach the edge of a town. It appears to be a simple community with a dozen or so huts and a couple of shops. Do you want to enter? \nInput (Yes or No): ")
            if (enterTown == "Yes") or (enterTown == "YES") or (enterTown == "yes"):
                chooseMap()
            elif (enterTown == "No") or (enterTown == "NO") or (enterTown == "no"):
                print("You decide to not enter the town presently.\n")
                playerActions()
            else:
                print("You step away from the town. You need a moment to collect your thoughts and think about your next action.\n")
                playerActions()
                
playerActions()