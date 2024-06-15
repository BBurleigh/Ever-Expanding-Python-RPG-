import random
from Resources.opponent_constructor import Opponent, BadBunny, HungryHobo, SneakySparrow, PersnicketyPrairieDog, BusyBigBee, CrosseyedCat, LumpyLadybug, RascallyRaccoon

firstVisit = True
greenGemQuest = True
plotCount = 0

playerCharacter = ["Rocco Taco", "golden floof", 10, 10, 1, 3, 4, 2, 5, 4, 4, 2]
worldMap = ["P", " ", " ", "F", "F", "H"]
playerInventory = ["Berries", "Berries", "Rocks"]
currentPosition = " "

itemList = {
    # "Item": ["name", "damage value", "heal value"]
    "Berries": ["Berries", 0, 3],
    "Apple": ["Apple", 0, 5],
    "Grapes": ["Grapes", 0, 8],
    "Thorns": ["Thorns", 2, 0],
    "Rocks": ["Rocks", 4, 0],
    "Bomb": ["Bomb", 10, 0],
    "Veggie Soup": ["Veggie Soup", 0, 12],
    "Green Gem": ["Green Gem", 0, 0]
}

opponent = []

def newAdventure():
    playerActions()
    
def playerActions():
    print("---------------------------------------------------------------------------")
    print("\nWorld Map: " + str(worldMap))
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
    elif (playerChoice == "Use Item") or (playerChoice == "USE ITEM") or (playerChoice == "use item"):
        useItem()
    else:
        print("That's not an option, whether you are thinking of something silly or incoherently (you spelled something incorrectly). \n")
        playerActions()

# This function determines whether the player can move west or not, and it stores the previous value of the
# index (the current area/terrain) inside the global variable currentPosition, which is updated when the player moves --> also prevents the player from # moving out-of-bounds
def travelWest():
    global currentPosition
    position = worldMap.index("P")
    if (position == 0):
        print("\n There is nothing beyond this point. You cannot travel further west. \n")
        playerActions()
    if (position > 0 ):
        nextArea = worldMap[position - 1]
        worldMap[position - 1] = "P"
        worldMap[position] = currentPosition
        currentPosition = nextArea
        print("\nYou travel a little west before stopping to take a rest.")
        playerActions()

# This function determines whether the player can move east or not, and it stores the previous value of the
# index (the current area/terrain) inside the global variable currentPosition, which is updated when the player moves --> also prevents the player from # moving out-of-bounds
def travelEast():
    global currentPosition
    position = worldMap.index("P")
    if (position == 0):
        currentPosition = " "
    if (position < len(worldMap) - 1):
        nextArea = worldMap[position + 1]
        worldMap[position + 1] = "P"
        worldMap[position] = currentPosition
        currentPosition = nextArea
        print("\nYou travel a little east before stopping to take a rest.")
        playerActions()
    elif (position == len(worldMap) - 1):
        print("\n There is nothing beyond this point. You cannot travel further east. \n")
        playerActions()

# Depending upon the current space that the player is in (currentPosition), they will either trigger a random
# event (either find an item, wander/nothing, or encounter a foe) or interact with the witch in her hut
def investigate():
    global currentPosition
    if (currentPosition == " ") or (currentPosition == "F"):
        randomEvent()
    elif (currentPosition == "H"):
        print("You have stumbled upon the witch's hut!\n")
        witchHutEvent()
 
# This function determmines, based one the value of currentPosition, what "event" will occur based on the
# value of event --> this could either involve finding an item, an encounter with a foe, or nothing        
def randomEvent():
    global currentPosition
    global opponent
    global playerInventory
    global greenGemQuest
    event = random.randint(75, 80)
    if (currentPosition == " "):
        if (event <= 25):
            randomItem = random.randint(1, 2)
            if (randomItem == 1):
                foundItem = itemList["Berries"][0]
                playerInventory.append(foundItem)
            else:
                foundItem = itemList["Rocks"][0]
                playerInventory.append(foundItem)
            print("While searching through the open fields, you have discovered some " + str(foundItem) + "! You place it in your inventory. \n")
            playerActions()
        elif (event > 25 and event <= 85):
            randomOpponent = random.randint(1, 10)
            if (randomOpponent <= 3):
                opponent = BadBunny()
                print(opponent)
            elif (randomOpponent > 3 and randomOpponent <= 6):
                opponent = HungryHobo()
                print(opponent)
            elif (randomOpponent > 6 and randomOpponent <= 9):
                opponent = SneakySparrow()
                print(opponent)
            elif (randomOpponent == 10):
                opponent = PersnicketyPrairieDog()
                print(opponent)
            print("\nYou have encountered a " + opponent.name + "!\n")
            combat()
        elif (event > 85):
            print("\nAs you search around the open plains, you admire the scenery and take comfort in the gentle breeze that wafts across you. As the tallgrass shimmers like golden waves, you sit and relax.\n")
            if (greenGemQuest == True):
                trapdoorChoice = input("As you search through the open fields for the " + itemList["Green Gem"][0] + ", you discover a rotted trapdoor that is nearly invisible under a thicket. It does not appear locked or guarded, and you are unsure where it leads. What will you do?\nInput (yes or no): ")
                if (trapdoorChoice == "Yes") or (trapdoorChoice == "YES") or (trapdoorChoice == "yes"):
                    exploreTrapdoor()
                elif (trapdoorChoice == "No") or (trapdoorChoice == "NO") or (trapdoorChoice == "no"):
                    print("You decide that it would be best to come back more prepared. You do not know what could lie under the worn trapdoor.\n")
                else:
                    print("You take a step back, unable to properly get your thoughts together. It may be best to return to this area when you can better think things through.\n")
            playerActions()
    if (currentPosition == "F"):
        if (event <= 50):
            randomItem = random.randint(1, 3)
            if (randomItem == 1):
                foundItem = itemList["Apple"][0]
                playerInventory.append(foundItem)
            elif (randomItem == 2):
                foundItem = itemList["Grapes"][0]
                playerInventory.append(foundItem)
            elif (randomItem == 3):
                foundItem = itemList["Thorns"][0]
                playerInventory.append(foundItem)
            print("While searching through the underbrush of the forest, you have discovered some " + str(foundItem) + "! You place it in your inventory. \n")
            playerActions()
        elif (event > 50 and event <= 80):
            randomOpponent = random.randint(1, 10)
            if (randomOpponent <= 3):
                opponent = BusyBigBee()
                print(opponent)
            elif (randomOpponent > 3 and randomOpponent <= 6):
                opponent = CrosseyedCat()
                print(opponent)
            elif (randomOpponent > 6 and randomOpponent <= 9):
                opponent = LumpyLadybug()
                print(opponent)
            elif (randomOpponent == 10):
                opponent = RascallyRaccoon
                print(opponent)
            print("You have encountered a " + opponent.name + "!\n")
            combat()
        elif (event > 80):
            print("\nAs you search around the forest, you admire the dense foliage and trickles of light that shimmer through the treetops. Everything is calm as you listen to the birds chirp in the trees, the bugs flit from flower to flower, and other small critters scurry in the underbrush.\n")
            playerActions()

# This function denotes combat between a randomly generated enemy and the player 
# While turn = True, the player can select what to do from a list of actions
# The list of actions: attack with melee (str), attack with range (dex), attack with magic (int), use an item,
# investigate/see a foe's stats, or flee from battle
# While turn = False, the opponent "decides" which action that they will take: attack with melee (str), attack
# with range (dex), attack with magic (int), or flee from battle
# Once either the player's HP or opponent's HP reaches zero, then the battle calculations are made
def combat():
    turn = True
    print("---------------------------------------------------------------------------")
    while ((playerCharacter[2] > 0) or (opponent.starting_HP > 0)) and (turn == True):
        print("What action do you plan on taking against " + opponent.name + "?\n")
        print("\n Opponent Information: " + opponent.name + "   Class: " + opponent.class_ + "  Level: " + str(opponent.level) + "  HP: " + str(opponent.starting_HP) + "  MP: " + str(opponent.starting_MP) + "\n")
        print("+---------------------------------------------------+")
        print("| Melee | Range | Magic | Use Item | Inspect | Flee |")
        print("+---------------------------------------------------+")
        print("\nPlayer Stats: " + playerCharacter[0] + "   Class: " + playerCharacter[1] + "  Level: " + str(playerCharacter[4]) + "  HP: " + str(playerCharacter[2]) + "  MP: " + str(playerCharacter[3]))
        print("              | Str " + str(playerCharacter[5]) + " | Dex " + str(playerCharacter[6]) + " | Int " + str(playerCharacter[7]) + " | Agi " + str(playerCharacter[8]) + " | Luck " + str(playerCharacter[9]) + " | Con " + str(playerCharacter[10]) + " | Will " + str(playerCharacter[11]) + "|")
        print("\nPlayer Inventory: " + str(playerInventory) + "\n")
        action = input("Decide which action you would like to take?\n Input: ")
        if (action == "Melee") or (action == "MELEE") or (action == "melee"):
            damage = playerCharacter[5] - opponent.constitution
            ("With your weapon in hand, you strike the " + opponent.name + "for " + str(damage) + " damage! \n")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Range") or (action == "RANGE") or (action == "range"):
            damage = playerCharacter[6] - opponent.constitution
            ("Getting a little distance, you strike the " + opponent.name + " from afar and for " + str(damage) + " damage! \n")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Magic") or (action == "MAGIC") or (action == "magic"):
            damage = playerCharacter[7] - opponent.willpower
            ("Muttering a small chant under your breath, you send a small burst of magic at " + opponent.name + " and hit your foe for " + str(damage) + " damage! \n")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Use Item") or (action == "USE ITEM") or (action == "use item"):
            itemInCombat()
        elif (action == "Inspect") or (action == "INSPECT") or (action == "inspect"):
            inspectionChance = random.randint(1, 10)
            if (playerCharacter[9] > inspectionChance):
                print("In the midst of combat, you are able to glean valuable information about the" + opponent.name + ".\n")
                print("Opponent Stats: " + opponent.name + "   Class: " + opponent.class_ + "  Level: " + str(opponent.level) + "  HP: " + str(opponent.starting_HP) + "  MP: " + str(opponent.starting_MP))
                print("Experience Points: " + str(opponent.EXP) + " | Money Dropped: " + str(opponent.money) + " Common Drop: " + opponent.commonItem + " | Rare Drop: " + opponent.rareItem + "|")
                print("              | Str " + str(opponent.strength) + " | Dex " + str(opponent.dexterity) + " | Int " + str(opponent.intelligence) + " | Agi " + str(opponent.agility) + " | Luck " + str(opponent.luck) + " | Con " + str(opponent.constitution) + " | Will " + str(opponent.willpower) + "|")
            else:
                print("In the midst of combat, you are unable to focus enough to infer any vital information about the " + opponent.name + ".\n")
        elif (action == "Flee") or (action == "FLEE") or (action == "flee"):
            if (playerCharacter[8] > opponent.agility):
                print("Seeing an opening, you manage to escape from your foe.\n")
                playerActions()
            else:
                print("You stumbled in your effort to escape, and your foe blocks your path.\n")
        print("\n---------------------------------------------------------------------------")
        turn = False
        while ((playerCharacter[2] > 0) or (opponent.starting_HP > 0)) and (turn == False):
            enemyAction = random.randint(1, 17)
            if (enemyAction <= 6):
                damage = opponent.strength - playerCharacter[10]
                if (damage < 0):
                    damage = 0
                print(opponent.melee_attack + "You receive " + str(damage) + " damage!\n")
                playerCharacter[2] = playerCharacter[2] - damage
                turn = True
            elif (enemyAction > 6 and enemyAction <= 11):
                damage = opponent.dexterity - playerCharacter[10]
                if (damage < 0):
                    damage = 0
                print(opponent.range_attack + "You receive " + str(damage) + " damage!\n")
                playerCharacter[2] = playerCharacter[2] - damage
                turn = True
            elif (enemyAction > 11 and enemyAction <= 16):
                damage = opponent.intelligence - playerCharacter[11]
                if (damage < 0):
                    damage = 0
                print(opponent.magic_attack + "You receive " + str(damage) + " damage!\n")
                playerCharacter[2] = playerCharacter[2] - damage
                turn = True
            elif (enemyAction == 17):
                print(opponent.flee)
                playerActions()
        if (playerCharacter[2] <= 0) or (opponent.starting_HP <= 0):
            victoryConditions()
        combat()

# This function determines how a player uses an item during combat
# If the player uses a healing item, then it restores HP
# If the player uses a damaging item, then it damages an opponent
def itemInCombat():
    chooseItem = input("You open your satchel and rummage through your items. Think of which item you would like to use. \n Input: ")
    if (len(playerInventory) > 0):
        if (chooseItem == "Berries") or (chooseItem == "BERRIES") or (chooseItem == "berries"):
            chooseItem = "Berries"
        elif (chooseItem == "Apple") or (chooseItem == "APPLE") or (chooseItem == "apple"):
            chooseItem = "Apple"
        elif (chooseItem == "Grapes") or (chooseItem == "GRAPES") or (chooseItem == "grapes"):
            chooseItem = "Grapes"
        elif (chooseItem == "Thorns") or (chooseItem == "THORNS") or (chooseItem == "thorns"):
            chooseItem = "Thorns"
        elif (chooseItem == "Rocks") or (chooseItem == "ROCKS") or (chooseItem == "rocks"):
            chooseItem = "Rocks"
        elif (chooseItem == "Bomb") or (chooseItem == "BOMB") or (chooseItem == "bomb"):
            chooseItem = "Bomb"
        if (chooseItem == "Berries") or (chooseItem == "Apple") or (chooseItem == "Grapes"):
            print("Going through your bag, you pull out " + chooseItem + ". You take a couple of bites, and it partially fills your stomach and heals you.\n")
            playerCharacter[2] = playerCharacter[2] + itemList[chooseItem][2]
            playerInventory.remove(chooseItem)
        elif (chooseItem == "Thorns") or (chooseItem == "Rocks") or (chooseItem == "Bomb"):
            damage = itemList[chooseItem][1]
            print("Going through your bag, you pull out " + chooseItem + ". You hurl it at the " + opponent.name + ", causing " + str(damage) + ".\n")
            opponent.starting_HP = opponent.starting_HP - damage 
            playerInventory.remove(chooseItem)
    elif (len(playerInventory) == 0):
        print("Your satchel is empty. So, you did not find anything useful for combat. \n")
    else:
        print("As you rummage through your satchel in search of " + chooseItem + ", you discover quickly that the rush of combat has clouded your judgment. You cannot recall exactly what you were looking for.\n")
        
# This function checks whether or not the player or the opponent has been defeated
# If the both have more than 0 HP, then the battle continues
# If the player reaches 0 HP, then it is "game over"
# If the opponent reaches 0 HP, then the player wins the battle (and eventually earns from EXP)
def victoryConditions():
    global opponent
    global currentPosition
    if(playerCharacter[2] <= 0):
        print(opponent.defeat)
        opponent = []
        print("-------------------- GAME OVER --------------------\n")
        # homescreen()
    elif(opponent.starting_HP <= 0):
        print(opponent.victory)
        opponent = []
        if (currentPosition == "C"):
            searchCave()
        playerActions()
        
# When the player "investigates" the witch's hut, when on this space and depending on which visit -
# determined by firstVisit being false or True            
def witchHutEvent():
    global firstVisit
    knockKnock = input("\nDo you dare to knock on the witch's door (yes or no)?\n Input: ")
    if (knockKnock == "Yes") or (knockKnock == "YES") or (knockKnock == "yes"):
        print("You knock on the old wood door.\n")
        print("???: Enter.\n")
        print("You push open the door. It creaks slowly as it shuts behind you. Scanning the room, you notice a plain table and simple kitchen on one side of the hut. Against the back wall is a grey stone fireplace that is gently burning and a cauldron full of vegetables and broth. Next to the fireplace is a robed elderly woman, who is rocking back and forth in her chair.\n")
        if (firstVisit == True):
            firstConversation()
        elif ("Green Gem" in playerInventory):
            greenGemConversation()
        elif (firstVisit == False):
            print("You are familiar with the witch now, and she has nothing more to say (for now).")
            playerActions()
    elif (knockKnock == "No") or (knockKnock == "NO") or (knockKnock == "no"):
        print("The ominous energy that emanates from the old shack keeps you from approaching it. You decide to leave the witch's hut alone.\n")
        playerActions()

# This function outlines the first conversation that the player can have with the witch, Annabelle        
def firstConversation():
    global plotCount
    global firstVisit
    global greenGemQuest
    if (plotCount == 4):
        print("Annabelle: You are probably curious about this world. Sit in the chair by the fire. I'll tell you a story.\n")
        print("You take a seat across from Annabelle. The fire crackles slightly as the warm aroma of cooked vegetables fills your nose. Annabelle conjures a long black pipe and takes a puff.\n")
        print("Annabelle: Once upon a time, our world was vast and wonderful. From the moment of creation, all living beings were able to branch out and thrive across our world.\n")
        print("A cloud of smoke swirls overhead, and it flattens and molds itself into a massive expanse of land. You can make out mountains and the details of several cities across it.\n")
        print("Annabelle: Mountains that felt the breath of the gods. Oceans that reflected the depths of the stars. Caverns that wove crystalline webs around the heart of the world. The diversity and intricacies of our world and others was wondrous.\n")
        print("Annabelle closes her eyes for a moment, which lasts for several.\n")
        print("Annabelle: But there was one person. One who feared everything. They cast a curse that tore away the layers and complexity of the world, stripping away the meaning of life in place for security and simplicity.\n")
        print("The smoke cloud begins to shrink. The landscape shrinks and begins to lose detail and focus. The cloud shrivels into a narrow rectangle.\n")
        print("Annabelle: And that's what brought the world to what it is today.\n")
        print("She stands up, and grabbing a ladle, she scoops some soup into a bowl and hands it to you. She also hands you a large wooden spoon.\n")
        print("Annabelle: I lost a gem out in the plains. It's the size of your hand, shaped like a triangle, green like an emerald. If you find it, bring it to me.\n")
        print("You agree to help Annabelle find the missing gem. You take your time sipping the veggie soup, and it is surprisingly flavorful as the warmth fills your stomach. You thank Annabelle for her hospitality before leaving the hut.\n")
        firstVisit = False
        greenGemQuest = True
        plotCount = 0
        playerActions()
    conversationChoices = input("These are the question choices. Just type in the number next to each question to ask this question.\n1. Who are you?\n2. What is this hut doing in the middle of the woods?\n3. What are you making?\n4. What is this place?\nInput Number: ")
    if (conversationChoices == "1"):
        count = True
        print("???: Who I am is not important, but it would be rude to not provide a name. You may call me Annabelle, and all I am is a mere device to push the plot forward and aid you on your journey.\n")
        if (count == True):
            plotCount = plotCount + 1
            count = False
        firstConversation()
    elif (conversationChoices == "2"):
        count = True
        print("???: The previous owner built it here. For one reason or another. I do not proclaim to understand what motivates one to build a home far from civilization. It was abandoned long before I uptook residence in it.\n")
        if (count == True):
            plotCount = plotCount + 1
            count = False
        firstConversation()
    elif (conversationChoices == "3"):
        count = True
        print("???: It's not a magical concoction, if that was your first assumption. This is a concoction of different vegetables and herbs that I grew in my garden and found in the forest. You are welcome to a bowl once it is finished cooking.\n")
        if (count == True):
            plotCount = plotCount + 1
            count = False
        firstConversation()
    elif (conversationChoices == "4"):
        count = True
        print("???: An old hut in the forest. And my home. There is nothing more to this place than what you see, but you do not have to take my word for it.\n")
        if (count == True):
            plotCount = plotCount + 1
            count = False
        firstConversation()

# This function introduces the exposition of climbing into the plains underground passage
def exploreTrapdoor():
    print("You clear some of the briar and open the trapdoor. It opens with ease, and you find a worn ladder that leads into a dirt tunnel. You climb down the ladder and find yourself in a small cave that is overgrown with vegetation from the surface. None of the plants appear dangerous or abnormal, and there are small holes which allow trickles of light into the cave.\n")
    print("Walking down the tunnel, you have no issues seeing what is ahead or along the tunnel walls. After a couple of minutes, the tunnel leads slightly downwards before opening up into a larger chamber. The chamber is coated with vines and foliage. You have a peculiar feeling that the green gem Annabelle wants is in here.\n")
    searchCave()

# This function allows the user to decide if they wish to continue looking around the overgrown cave for
# the green gem            
def searchCave():
    global currentPosition
    global opponent
    global playerInventory
    findGemOption = input("As you gaze around the overgrown chamber, do you wish to keep searching for the gem?\nInput (Yes or No): ")
    if (findGemOption == "Yes") or (findGemOption == "YES") or (findGemOption == "yes"):
        currentPosition = "C"
        search = random.randint(1, 5)
        search = 6
        if (search <= 4):
            print("Despite ripping out some leaves and roots, you fail to find anything that resembles a gem.\n")
        elif (search > 4 and search <= 7):
            opponent = Opponent.create_ornery_onion
            print("When you overturn a large vine, an overgrown vegetable rolls out. You step back, and it gives you a creepy and angry smirk.")
            combat()
        elif (search > 7):
            if "Green Gem" in playerInventory:
                print("As you begin oveturning some vines and leaves, you stop. You realize that you won't find another gem. You decide to return to the mouth of the cave and figure out what you want to do.\n")
            else:
                print("Tearing a couple vines away, you see a faint glimmer beneath the overgrowth.\n")
                print("You continue ripping away more and more vines, and cradled beneath a large leaf is the " + itemList["Green Gem"][0] + ".\nYou pick it up and place it in your satchel. Annabelle will be pleased by your discovery.\n")
                foundGem = itemList["Green Gem"][0]
                playerInventory.append(foundGem)
                print("You leave the cave with no issues and return to the surface.\n")
                currentPosition == " "
                playerActions()
        searchCave()
    elif (findGemOption == "No") or (findGemOption == "NO") or (findGemOption == "no"):
        print("You decide that it would be best to return to the cave when you have had time to prepare.\n")
        currentPosition == " "
        playerActions()
    else: 
        print("The shadows beneath the overgrowth mess with you mind, and you cannot decide on an action to take.\n")
        searchCave()
        
# this function outlines the conversation the player has with Annabelle if the player has the Green Gem in their 
# inventory --> in the future, this will progress the story further and expand the map to be 5 x 5 (2D)
def greenGemConversation():
    global greenGemQuest
    print("Annabelle: Hm. You found it.\n")
    print("You pull out the gem from your satchel. Her dark eyes twinkle for a brief moment before hiding themselves beneath her hood.\n")
    print("Annabelle: You are wondering why I wanted you to find this gem, if am reading your mind correctly. Please, have a seat.\n")
    print("You sit in the chair across from Annabelle. The cauldron blows a new smell onto you, one that is meaty and sweet.\n")
    print("Annabelle: This gem was designated to be the first key in undoing the curse that shrank and condensed our world into something simple and predictable. Please hand it to me.\n")
    print("Though you do not fully understand her words, you hand her the gem. When you give it to her, it begins to faintly shine like a dull star. The gem's green colors twist and fade into different hues, and its glow colors the shadows inside of the hut.\n")
    playerInventory.remove("Green Gem")
    print("Annabelle: When the curse was cast, several keys to undoing it were created. One of these keys took the form of this gemstone. With it, I can undoa small piece of the curse.\n")
    greenGemQuest = False
    print("THIS IS WHERE THE GAME ENDS SO FAR!!  MORE TO COME IN THE FUTURE!!\n")

# Based on the item that the player wishes to access, if they choose a fruit/consumable item, then the
# player is healed by that item. If the player has no items or types in something that cannot be consumed,
# then         
def useItem():
    chooseItem = input("You open your satchel and rummage through your items. Think of which item you would like to use. \n Input: ")
    if (len(playerInventory) > 0):
        if (chooseItem == "Berries") or (chooseItem == "BERRIES") or (chooseItem == "berries"):
            chooseItem = "Berries"
        elif (chooseItem == "Apple") or (chooseItem == "APPLE") or (chooseItem == "apple"):
            chooseItem = "Apple"
        elif (chooseItem == "Grapes") or (chooseItem == "GRAPES") or (chooseItem == "grapes"):
            chooseItem = "Grapes"
        print("Going through your bag, you pull out " + chooseItem + " . You take a couple of bites, and it partially fills your stomach and heals you. \n")
        playerCharacter[2] = playerCharacter[2] + itemList[chooseItem][2]
        playerInventory.remove(chooseItem)
        playerActions()
    elif (len(playerInventory) == 0):
        print("Your satchel is empty. Maybe you need to collect a few items in the area. \n")
    else:
        print("Looking at " + chooseItem + ", you realize that you cannot consume this. Or better said, it would probably hurt you if it did. You close your satchel and take a moment to think about what you really want. \n")
        playerActions()
    
newAdventure()