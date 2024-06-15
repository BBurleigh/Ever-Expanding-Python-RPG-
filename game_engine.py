import random
from Resources.player_constructor import Noel, Bianca, Pale, Bunny, RoccoTaco, Annabelle
from Resources.opponent_constructor import BadBunny, HungryHobo, SneakySparrow, PersnicketyPrairieDog, BusyBigBee, CrosseyedCat, LumpyLadybug, RascallyRaccoon, OrneryOnion
from Resources.skill_constructor import Salve, Aim, Branch, Glitter, TailWhip, SmokeRing
from Resources.item_constructor import Berries, Apple, Grapes, Carrot, Onion, Honey, VeggieSoup, Thorns, Rocks, Bomb, TuftOfFur, TinyFeather, Scraps, Twig, Vine, Stinger, Claw, Shell, CoarseLeather, RabbitsFoot, GreenGem

# An array that makes up the world map:
# P represents the player's position
# " " represents an open area, such as a field
# F represents a forest biome
# H represents a hut
# When the map is expanded to be 2D, there will be more symbols to represent biomes/areas
# The player technically begins their journey in an open field
world_map = ["P", " ", " ", "F", "F", "H"]
current_position = " "

# The variables are set to false, but if the player inputs "secret" or "puppy" on the homescreen, it will
# be reassigned to true --> access to a secret fourth and/or fifth character
secret_character_bunny = False
secret_character_puppy = False
secret_character_witch = False
bestiary = False

# The first will store the player's information while playing the game
# The second will store the opponent's information if a battle occurs (will be emptied after the battle) 
player_character = []
opponent = []
opponent_list = [BadBunny, HungryHobo, SneakySparrow, PersnicketyPrairieDog, BusyBigBee, CrosseyedCat, LumpyLadybug, RascallyRaccoon, OrneryOnion]

# This will determine which conversation set the player sees when they interact with the witch
# The second acts as a switch, determining if the search for the green gem quest is active
# The third will be used to help create triggers for different events while advancing the main storyline
first_visit = True
green_gem_quest = False
plot_count = 0

# This will print out the homescreen in the terminal
# The player is prompted in the terminal to type what they would like to do next
def homescreen():
    print("+----------------------------------+")
    print("|       RPG MAP EXPLORER V.1       |")
    print("------------------------------------")
    print("|            NEW GAME              |")
    print("------------------------------------")
    print("|        GAME INSTRUCTIONS         |")
    if (bestiary == True):
        print("------------------------------------")
        print("|            BESTIARY              |")
    print("------------------------------------")
    print("|            CREDITS               |")
    print("------------------------------------")
    print("|         CLOSE TERMINAL           |")
    print("+----------------------------------+")
    select_option()

# This will print out the character select screen in the terminal
# The player is promted in the terminal to type which character that they would like to play as    
def character_select_screen():
    print("+----------------------------------+")
    print("|      CHOOSE YOUR CHARACTER       |")
    print("------------------------------------")
    print("|      NOEL, THE HERBALIST         |")
    print("------------------------------------")
    print("|       BIANCA, THE HUNTER         |")
    print("------------------------------------")
    print("|        PALE, THE SHAMAN          |")
    if(secret_character_bunny == True):
        print("------------------------------------")
        print("|       BUNNY, THE COSMONAUT       |")
    if(secret_character_puppy == True):
        print("------------------------------------")
        print("|   ROCCO TACO, THE GOLDEN FLOOF   |")
    if(secret_character_witch == True):
        print("------------------------------------")
        print("|       ANNABELLE, THE WITCH       |")
    print("+----------------------------------+")
    select_character()
# This will print out the game instructions screen in the terminal
# The player is prompted to type "Home" in the terminal to return to the homescreen 
def game_instructions():
    print("+----------------------------------+")
    print("|         GAME INSTRUCTIONS        |")
    print("------------------------------------")
    print("|   FIRST, CHOOSE YOUR CHARACTER.  |")
    print("------------------------------------")
    print("|      1) NOEL, THE HERBALIST      |")
    print("| A simple and mild-mannered boy,  |")
    print("|  he travels with a staff and is  |")
    print("|    knowledgeable in herbology.   |")
    print("|                                  |")
    print("|      2) BIANCA, THE HUNTER       |")
    print("| A serious and distrustful woman, |")
    print("|  she spends most of her time in  |")
    print("|  the wild, hunting with her bow. |")
    print("|                                  |")
    print("|       3) PALE, THE SHAMAN        |")
    print("| A quiet and lonesome man from a  |")
    print("| local tribe, he seeks solitude   |")
    print("| and communes often with spirits. |")
    print("|                                  |")
    if(secret_character_bunny == True):
        print("|     4) BUNNY, THE COSMONAUT      |")
        print("| A cheerful and sassy rabbit from |")
        print("|   a distant star, he travels to  |")
        print("|  discover the best carrot wine.  |")
        print("|                                  |")
    if(secret_character_puppy == True):
        print("| 5) ROCCO TACO, THE GOLDEN FLOOF  |")
        print("| An excitable and overly friendly |")
        print("| puppy, he demands the attention  |")
        print("|     of others and loves pets.    |")
        print("|                                  |")
    if(secret_character_witch == True):
        print("|     6) ANNABELLE, THE WITCH      |")
        print("|  An elderly woman who has many   |")
        print("|  stories to tell, Annabelle is   |")
        print("| searching for one more adventure |")
        print("|     to excite her old bones.     |")
        print("|                                  |")
    print("------------------------------------")
    print("|    THEN, A WORLD MAP WILL BE     |")
    print("|      GENERATED FROM A LIST.      |")
    print("|     P represents the player      |")
    print("|  \" \" represent an open area,     |")
    print("|     such as a field or plain     |")
    print("|   F represents a forest biome    |")
    print("|  H represent's the witch's hut   |")
    print("------------------------------------")
    print("|  OUTSIDE OF BATTLE, THE PLAYER   |")
    print("|     PERFORM SEVERAL ACTIONS:     |")
    print("|        a) Move west/left         |")
    print("|        b) Move east/right        |")
    print("|  c) Investigate an area, which   |")
    print("|  may result in a fight, finding  |")
    print("| an item, or speaking to someone. |")
    print("| d) Use an item to heal from the  |")
    print("|       player's inventory.        |")
    print("|----------------------------------|")
    print("| DURING A BATTLE, THE PLAYER CAN  |")
    print("|   CHOOSE FROM SEVERAL ACTIONS:   |")
    print("| a) Attack: use base Str, Dex, or |")
    print("|   Int to iniate a base attack.   |")
    print("| b) Defend: double Con or Will to |")
    print("|   to protect against an attack.  |")
    print("| c) Use Item: the player uses an  |")
    print("|   item in their inventory, if    |")
    print("|   there is an item available.    |")
    print("|   d) Skill: use a skill known to |")
    print("|  the specific character, if the  |")
    print("|      player has enough MP.       |")
    print("|  e) Flee: use base Agi and Luck  |")
    print("| to see if the player is able to  |")
    print("|  successfully flee the battle.   |")
    print("|----------------------------------|")
    print("| BATTLE CONDITIONS: VICTORY/LOSS  |")
    print("| If the opponent's HP reaches 0,  |")
    print("| then the player wins. The player |")
    print("|  obtains EXP and maybe an item.  |")
    print("|  If the player's HP reaches 0,   |")
    print("|  then the player loses. A game   |")
    print("| over screen shows. The player is |")
    print("|  presented the option to return  |")
    print("|  the homescreen or start a new   |")
    print("|  adventure with any character.   |")
    print("|----------------------------------|")
    print("|  TO RETURN TO THE HOME SCREEN,   |")
    print("|           TYPE: HOME             |")
    print("+----------------------------------+")
    return_home()

# This will print out the bestiary once the player has accessed this (or know the password)
# It will display the name of each opponent, their class, and their base stats
# This will need to be reformatted later so that it prints things nicely and symmetrically    
def open_bestiary():
    print("+----------------------------------+")
    print("|             BESTIARY             |")
    print("------------------------------------")
    for x in opponent_list:
        print("| " + str(x) + " | ")
        print("|                                  |")
    print("------------------------------------")
    print("|  TO RETURN TO THE HOME SCREEN,   |")
    print("|           TYPE: HOME             |")
    print("+----------------------------------+")
    return_home()

# This will print out the credits screen in the terminal
# The player is prompted to type "Home" in the terminal to return to the homescreen       
def credits():
    print("+----------------------------------+")
    print("|  CREDITS FOR THIS TERMINAL GAME  |")
    print("------------------------------------")
    print("|   CREATED BY BRAYDEN BURLEIGH    |")
    print("|    LANGUAGE: PYTHON v.3.11.4     |")
    print("|     USING VISUAL STUDIO CODE     |")
    print("| THE FIRST VERSION OF THE GAME WAS|")
    print("|  CREATED IN THE SPRING OF 2024.  |")
    print("------------------------------------")
    print("| I APPRECIATE THE LOVING SUPPORT  |")
    print("|   THAT I HAVE RECEIVED FROM MY   |")
    print("|   PARTNER AND OUR PUPPY, ROCCO.  |")
    print("|----------------------------------|")
    print("|  TO RETURN TO THE HOME SCREEN,   |")
    print("|           TYPE: HOME             |")
    print("+----------------------------------+")
    return_home()

# On the homescreen, depending on what the player types when prompted, one of these options will occur:
# 1) the player begins a new game --> taken to the character select screen
# 2) the player is sent to a set of instructions for how to play the game
# 3) the player is sent to the credits screen
# 4) the player is sent to the bestiary page, where information about opponents is displayed
# 5) the player types in one or both secret phrases --> unlocks one or two playable characters
# 6) the player can stop the app/close the terminal
# 7) the player is told that they typed something incorrect/not an option    
def select_option():
    player_input = input("Type which option you would like to select. Spelling matters. \n Input: ")
    if (player_input == "New Game") or (player_input == "NEW GAME") or (player_input == "new game"):
        print("Time to start a new adventure! \n")
        character_select_screen()
    elif (player_input == "Game Instructions") or (player_input == "GAME INSTRUCTIONS") or (player_input == "game instructions"):
        print("It is necessary to know what goes into this adventure! Here is some guidance! \n")
        game_instructions()
    elif (player_input == "Credits") or (player_input == "CREDITS") or (player_input == "credits"):
        print("Let's role the credits! \n")
        credits()
    elif (player_input == "Bestiary") or (player_input == "BESTIARY") or (player_input == "bestiary"):
        global bestiary
        if(bestiary == True):
                print("Let us open the bestiary and view information about former opponents! \n")
                open_bestiary()
        print("You have unlocked the bestiary for this world! \n" )
        bestiary = True
        homescreen()
    elif (player_input == "Secret") or (player_input == "SECRET") or (player_input == "secret"):
        global secret_character_bunny
        if(secret_character_bunny == True):
            print("Only one special space bunny per adventure! \n")
            select_option()
        print("You've discovered a secret bunny from the moon! Bunny is available! \n")
        secret_character_bunny = True
        select_option()
    elif(player_input == "Puppy") or (player_input == "PUPPY") or (player_input == "puppy"):
        global secret_character_puppy
        if(secret_character_puppy == True):
            print("You cannot have more than one golden puppy! \n")
            select_option()
        print("You've encountered an adorable golden puppy! Rocco Taco is available! \n")    
        secret_character_puppy = True
        select_option()
    elif(player_input == "Cursed") or (player_input == "CURSED") or (player_input == "cursed"):
        global secret_character_witch
        if(secret_character_witch == True):
            print("Across other dimensions, the other Annabelles refuse your call! \n")
            select_option()
        print("From a portal, an old woman with an iron ladle steps into your presence! You've encountered an adorable golden puppy! Annabelle is available! \n")    
        secret_character_witch = True
        select_option()
    elif (player_input == "Close Terminal") or (player_input == "CLOSE TERMINAL") or (player_input == "close terminal"):
        print("Closing app.  Til next time! \n")
        exit()
    else:
        print("Be careful with your spelling! \n")
        select_option()

# On the credits screen, depending on what the player types when prompted, one of these options will occur:
# 1) the player returns to the homescreen
# 2) the player is told that they typed something incorrect/not an option 
def return_home():
    player_input = input("If you'd like to return to the homescreen, then type 'Home'. \n Input: ")
    if (player_input == "Home") or (player_input == "HOME") or (player_input == "home"):
        print("Returning to the homescreen! \n")
        homescreen()
    else:
        print("Be careful with your spelling, even if it is just 'Home'! \n")
        return_home()

# On the select character screen, the player can choose one of the displayed characters to play as during
# their adventure --> a double-check is given, in case the player wishes to change characters       
def select_character():
    player_input = input("Type the name of the character you'd like to play as. Spelling matters, and only type the name \n (ex. correct 'Pale' but incorrect 'Pale, The Shaman'). \n Input: ")
    global player_character
    if (player_input == "Noel") or (player_input == "NOEL") or (player_input == "noel"):
        player_character = Noel()
    elif (player_input == "Bianca") or (player_input == "BIANCA") or (player_input == "bianca"):
        player_character = Bianca()
    elif (player_input == "Pale") or (player_input == "PALE") or (player_input == "pale"):
        player_character = Pale()
    elif (secret_character_bunny == True) and ((player_input == "The Bunny") or (player_input == "THE BUNNY") or (player_input == "the bunny")):
        player_character = Bunny()
    elif (secret_character_puppy == True) and ((player_input == "Rocco Taco") or (player_input == "ROCCO TACO") or (player_input == "rocco taco")):
        player_character = RoccoTaco
    elif (secret_character_witch == True) and((player_input == "Annabelle") or (player_input == "ANNABELLE") or (player_input == "annabelle")):
        player_character = Annabelle()
    else:
        print("Double check how you've typed in one of the character's names! \n")
        select_character()
    character_double_check()

# This prints out the selected character's stats and checks if the player wants to use this character:
# If "Yes", then a new adventure will commence
# If "No", then the player is taken back to the select character screen
# If the player inputs a typo, then the player is lightly mocked and asked to type "Yes" or "No" again
def character_double_check():
    global player_character
    print("\n Character Name: " + player_character.name + "\n Class: " + player_character.class_ + "\n HP: " + str(player_character.starting_HP) + "\n MP: " + str(player_character.starting_MP) + "\n Level: " + str(player_character.level) + "\n Strength: " + str(player_character.strength) + "\n Dexterity: " + str(player_character.dexterity) + "\n Intelligence: " + str(player_character.intelligence) + "\n Agility: " + str(player_character.agility) + "\n Luck: " + str(player_character.luck) + "\n Constitution: " + str(player_character.constitution) + "\n Willpower: " + str(player_character.willpower) +"\n")
    player_check = input("Is " + player_character.name + " the character you wish to play as? \n Yes/No? ")
    if (player_check == "Yes") or (player_check == "YES") or (player_check == "yes"):
        print("Perfect. " + player_character.name + ", it is time to begin your adventure! \n")
        new_adventure()
    elif (player_check == "No") or (player_check == "NO") or (player_check == "no"):
        print("It is best to be decisive before your adventure. Choose who you wish to journey as! \n")
        player_character = []
        select_character()
    else:
        print("It's a simple 'Yes' or 'No'. Let's try that again. \n")
        character_double_check()


# The world map is displayed in the terminal, and the player is given a list of options/actions as well as their 
# character's stats as well as inventory
def new_adventure():
    player_actions()
    
def player_actions():
    print("\n---------------------------------------------------------------------------")
    print("\nWorld Map: " + str(world_map))
    print("\nPlayer Stats: " + player_character.name + "   Class: " + player_character.class_ + "  Level: " + str(player_character.level) + "  EXP: " + str(player_character.EXP) + "  HP: " + str(player_character.starting_HP) + "  MP: " + str(player_character.starting_MP))
    print("              | Str " + str(player_character.strength) + " | Dex " + str(player_character.dexterity) + " | Int " + str(player_character.intelligence) + " | Agi " + str(player_character.agility) + " | Luck " + str(player_character.luck) + " | Con " + str(player_character.constitution) + " | Will " + str(player_character.willpower) + "|")
    print("\nPlayer Inventory: " + str(player_character.consumables_inventory))
    print("\nCombat Items: " + str(player_character.combat_inventory))
    print("\nSkills List: " + str(player_character.skill_list))
    print("\nKey/Quest Items: " + str(player_character.key_items_inventory) + "\n")
    print("+--------------------------------------------+")
    print("| Go West | Go East | Investigate | Use Item |")
    print("+--------------------------------------------+")
    player_choice = input("Based on your choices, what do you plan on doing? \n Input: ")
    if (player_choice == "Go West") or (player_choice == "GO WEST") or (player_choice == "go west"):
        travel_west()
    elif (player_choice == "Go East") or (player_choice == "GO EAST") or (player_choice == "go east"):
        travel_east()
    elif (player_choice == "Investigate") or (player_choice == "INVESTIGATE") or (player_choice == "investigate"):
        investigate()
    elif (player_choice == "Use Item") or (player_choice == "USE ITEM") or (player_choice == "use item"):
        use_item()
    else:
        print("That's not an option, whether you are thinking of something silly or incoherently (you spelled something incorrectly). \n")
        player_actions()

# This function determines whether the player can move west or not, and it stores the previous value of the
# index (the current area/terrain) inside the global variable current_position, which is updated when the player moves --> also prevents the player from # moving out-of-bounds
def travel_west():
    global current_position
    position = world_map.index("P")
    if (position == 0):
        print("\n There is nothing beyond this point. You cannot travel further west. \n")
        player_actions()
    if (position > 0 ):
        next_area = world_map[position - 1]
        world_map[position - 1] = "P"
        world_map[position] = current_position
        current_position = next_area
        print("\nYou travel a little west before stopping to take a rest.")
        player_actions()

# This function determines whether the player can move east or not, and it stores the previous value of the
# index (the current area/terrain) inside the global variable current_position, which is updated when the player moves --> also prevents the player from # moving out-of-bounds
def travel_east():
    global current_position
    position = world_map.index("P")
    if (position == 0):
        current_position = " "
    if (position < len(world_map) - 1):
        next_area = world_map[position + 1]
        world_map[position + 1] = "P"
        world_map[position] = current_position
        current_position = next_area
        print("\nYou travel a little east before stopping to take a rest.")
        player_actions()
    elif (position == len(world_map) - 1):
        print("\n There is nothing beyond this point. You cannot travel further east. \n")
        player_actions()

# Depending upon the current space that the player is in (current_position), they will either trigger a random
# event (either find an item, wander/nothing, or encounter a foe) or interact with the witch in her hut
def investigate():
    global current_position
    if (current_position == " ") or (current_position == "F"):
        random_event()
    elif (current_position == "H"):
        print("You have stumbled upon the witch's hut!\n")
        witch_hut_event()
 
# This function determmines, based one the value of current_position, what "event" will occur based on the
# value of event --> this could either involve finding an item, an encounter with a foe, or nothing        
def random_event():
    global current_position
    global opponent
    global green_gem_quest
    event = random.randint(1, 100)
    if (current_position == " "):
        if (event <= 25):
            random_item = random.randint(1, 2)
            if (random_item == 1):
                found_item = Berries().name
                player_character.consumables_inventory.append(found_item)
            else:
                found_item = Rocks().name
                player_character.combat_inventory.append(found_item)
            print("While searching through the open fields, you have discovered some " + str(found_item) + "! You place it in your inventory. \n")
            player_actions()
        elif (event > 25 and event <= 85):
            random_opponent = random.randint(1, 10)
            if (random_opponent <= 3):
                opponent = BadBunny()
                print(opponent)
            elif (random_opponent > 3 and random_opponent <= 6):
                opponent = HungryHobo()
                print(opponent)
            elif (random_opponent > 6 and random_opponent <= 9):
                opponent = SneakySparrow()
                print(opponent)
            elif (random_opponent == 10):
                opponent = PersnicketyPrairieDog()
                print(opponent)
            print("\nYou have encountered a " + opponent.name + "!\n")
            combat()
        elif (event > 85):
            print("\nAs you search around the open plains, you admire the scenery and take comfort in the gentle breeze that wafts across you. As the tallgrass shimmers like golden waves, you sit and relax.\n")
            if (green_gem_quest == True):
                trap_door_choice = input("As you search through the open fields for the " + GreenGem().name + ", you discover a rotted trapdoor that is nearly invisible under a thicket. It does not appear locked or guarded, and you are unsure where it leads. What will you do?\nInput (yes or no): ")
                if (trap_door_choice == "Yes") or (trap_door_choice == "YES") or (trap_door_choice == "yes"):
                    explore_trapdoor()
                elif (trap_door_choice == "No") or (trap_door_choice == "NO") or (trap_door_choice == "no"):
                    print("You decide that it would be best to come back more prepared. You do not know what could lie under the worn trapdoor.\n")
                else:
                    print("You take a step back, unable to properly get your thoughts together. It may be best to return to this area when you can better think things through.\n")
            player_actions()
    if (current_position == "F"):
        if (event <= 50):
            random_item = random.randint(1, 3)
            if (random_item == 1):
                found_item = Apple().name
                player_character.consumables_inventory.append(found_item)
            elif (random_item == 2):
                found_item = Grapes().name
                player_character.consumables_inventory.append(found_item)
            elif (random_item == 3):
                found_item = Thorns().name
                player_character.combat_inventory.append(found_item)
            print("While searching through the underbrush of the forest, you have discovered some " + str(found_item) + "! You place it in your inventory. \n")
            player_actions()
        elif (event > 50 and event <= 80):
            random_opponent = random.randint(1, 10)
            if (random_opponent <= 3):
                opponent = BusyBigBee()
                print(opponent)
            elif (random_opponent > 3 and random_opponent <= 6):
                opponent = CrosseyedCat()
                print(opponent)
            elif (random_opponent > 6 and random_opponent <= 9):
                opponent = LumpyLadybug()
                print(opponent)
            elif (random_opponent == 10):
                opponent = RascallyRaccoon
                print(opponent)
            print("You have encountered a " + opponent.name + "!\n")
            combat()
        elif (event > 80):
            print("\nAs you search around the forest, you admire the dense foliage and trickles of light that shimmer through the treetops. Everything is calm as you listen to the birds chirp in the trees, the bugs flit from flower to flower, and other small critters scurry in the underbrush.\n")
            player_actions()

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
    while ((player_character.starting_HP > 0) or (opponent.starting_HP > 0)) and (turn == True):
        print("What action do you plan on taking against " + opponent.name + "?\n")
        print("\n Opponent Information: " + opponent.name + "   Class: " + opponent.class_ + "  Level: " + str(opponent.level) + "  HP: " + str(opponent.starting_HP) + "  MP: " + str(opponent.starting_MP) + "\n")
        print("+-----------------------------------------------------------+")
        print("| Melee | Range | Magic | Skill | Use Item | Inspect | Flee |")
        print("+-----------------------------------------------------------+")
        print("\nPlayer Stats: " + player_character.name + "   Class: " + player_character.class_ + "  Level: " + str(player_character.level) + "  HP: " + str(player_character.starting_HP) + "  MP: " + str(player_character.starting_MP))
        print("              | Str " + str(player_character.strength) + " | Dex " + str(player_character.dexterity) + " | Int " + str(player_character.intelligence) + " | Agi " + str(player_character.agility) + " | Luck " + str(player_character.luck) + " | Con " + str(player_character.constitution) + " | Will " + str(player_character.willpower) + "|")
        print("\nPlayer Inventory: " + str(player_character.consumables_inventory))
        print("\nCombat Items: " + str(player_character.combat_inventory))
        print("\nSkills List: " + str(player_character.skill_list) + "\n")
        action = input("Decide which action you would like to take?\n Input: ")
        if (action == "Melee") or (action == "MELEE") or (action == "melee"):
            damage = player_character.strength - opponent.constitution
            print(player_character.melee_attack + " Your opponent receives " + str(damage) + " damage!")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Range") or (action == "RANGE") or (action == "range"):
            damage = player_character.dexterity - opponent.constitution
            print(player_character.range_attack + " Your opponent receives " + str(damage) + " damage!")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Magic") or (action == "MAGIC") or (action == "magic"):
            damage = player_character.intelligence - opponent.willpower
            print(player_character.magic_attack + " Your opponent receives " + str(damage) + " damage!")
            opponent.starting_HP = opponent.starting_HP - damage
        elif (action == "Use Item") or (action == "USE ITEM") or (action == "use item"):
            item_in_combat()
        elif (action == "Inspect") or (action == "INSPECT") or (action == "inspect"):
            inspection_chance = random.randint(1, 10)
            if (player_character.luck > inspection_chance):
                print("In the midst of combat, you are able to glean valuable information about the" + opponent.name + ".\n")
                print("Opponent Stats: " + opponent.name + "   Class: " + opponent.class_ + "  Level: " + str(opponent.level) + "  HP: " + str(opponent.starting_HP) + "  MP: " + str(opponent.starting_MP))
                print("Experience Points: " + str(opponent.EXP) + " | Money Dropped: " + str(opponent.money) + " Common Drop: " + opponent.commonItem + " | Rare Drop: " + opponent.rareItem + "|")
                print("              | Str " + str(opponent.strength) + " | Dex " + str(opponent.dexterity) + " | Int " + str(opponent.intelligence) + " | Agi " + str(opponent.agility) + " | Luck " + str(opponent.luck) + " | Con " + str(opponent.constitution) + " | Will " + str(opponent.willpower) + "|")
            else:
                print("In the midst of combat, you are unable to focus enough to infer any vital information about the " + opponent.name + ".\n")
        elif (action == "Flee") or (action == "FLEE") or (action == "flee"):
            if (player_character.agility > opponent.agility):
                print(player_character.flee + "\n")
                player_actions()
            else:
                print("You stumbled in your effort to escape, and your foe blocks your path.\n")
        print("\n---------------------------------------------------------------------------")
        turn = False
        while ((player_character.starting_HP > 0) or (opponent.starting_HP > 0)) and (turn == False):
            enemy_action = random.randint(1, 17)
            if (enemy_action <= 6):
                damage = opponent.strength - player_character.constitution
                if (damage < 0):
                    damage = 0
                print(opponent.melee_attack + " You receive " + str(damage) + " damage!\n")
                player_character.starting_HP = player_character.starting_HP - damage
                turn = True
            elif (enemy_action > 6 and enemy_action <= 11):
                damage = opponent.dexterity - player_character.constitution
                if (damage < 0):
                    damage = 0
                print(opponent.range_attack + " You receive " + str(damage) + " damage!\n")
                player_character.starting_HP = player_character.starting_HP - damage
                turn = True
            elif (enemy_action > 11 and enemy_action <= 16):
                damage = opponent.intelligence - player_character.willpower
                if (damage < 0):
                    damage = 0
                print(opponent.magic_attack + " You receive " + str(damage) + " damage!\n")
                player_character.starting_HP = player_character.starting_HP - damage
                turn = True
            elif (enemy_action == 17):
                print(opponent.flee)
                player_actions()
        if (player_character.starting_HP <= 0) or (opponent.starting_HP <= 0):
            victory_conditions()
        combat()

# This function determines how a player uses an item during combat
# If the player uses a healing item, then it restores HP
# If the player uses a damaging item, then it damages an opponent
def item_in_combat():
    chosen_item = input("You open your satchel and rummage through your items. Think of which item you would like to use. \n Input: ")
    if (len(player_character.consumables_inventory) > 0) or (len(player_character.combat_inventory) > 0):
        if (chosen_item == "Berries") or (chosen_item == "BERRIES") or (chosen_item == "berries"):
            chosen_item = Berries()
        elif (chosen_item == "Apple") or (chosen_item == "APPLE") or (chosen_item == "apple"):
            chosen_item = Apple()
        elif (chosen_item == "Grapes") or (chosen_item == "GRAPES") or (chosen_item == "grapes"):
            chosen_item = Grapes()
        elif (chosen_item == "Carrot") or (chosen_item == "CARROT") or (chosen_item == "carrot"):
            chosen_item = Carrot()
        elif (chosen_item == "Onion") or (chosen_item == "ONION") or (chosen_item == "onion"):
            chosen_item = Onion()
        elif (chosen_item == "Honey") or (chosen_item == "HONEY") or (chosen_item == "honey"):
            chosen_item = Honey()
        elif (chosen_item == "Veggie Soup") or (chosen_item == "VEGGIE SOUP") or (chosen_item == "veggie soup"):
            chosen_item = VeggieSoup()
        elif (chosen_item == "Thorns") or (chosen_item == "THORNS") or (chosen_item == "thorns"):
            chosen_item = Thorns()
        elif (chosen_item == "Rocks") or (chosen_item == "ROCKS") or (chosen_item == "rocks"):
            chosen_item = Rocks()
        elif (chosen_item == "Bomb") or (chosen_item == "BOMB") or (chosen_item == "bomb"):
            chosen_item = Bomb()
        if (chosen_item.consumable_item == True):
            print(chosen_item.use_description + "\n")
            player_character.starting_HP = player_character.starting_HP + chosen_item.heal_HP_value
            player_character.starting_MP = player_character.starting_MP + chosen_item.heal_MP_value
            player_character.consumables_inventory.remove(chosen_item.name)
        elif (chosen_item.combat_item == True):
            hp_damage = chosen_item.damage_HP_value
            mp_damage = chosen_item.damage_MP_value
            print(chosen_item.use_description + ".\n")
            opponent.starting_HP = opponent.starting_HP - hp_damage
            opponent.starting_MP = opponent.starting_MP - mp_damage 
            player_character.combat_inventory.remove(chosen_item.name)
    elif (len(player_character.consumables_inventory) == 0) and (len(player_character.combat_inventory) == 0):
        print("Your satchel is empty. So, you did not find anything useful for combat. \n")
    else:
        print("As you rummage through your satchel in search of " + chosen_item + ", you discover quickly that the rush of combat has clouded your judgment. You cannot recall exactly what you were looking for.\n")
        
# This function checks whether or not the player or the opponent has been defeated
# If the both have more than 0 HP, then the battle continues
# If the player reaches 0 HP, then it is "game over"
# If the opponent reaches 0 HP, then the player wins the battle (and eventually earns from EXP)
def victory_conditions():
    global opponent
    global current_position
    if(player_character.starting_HP <= 0):
        print(opponent.defeat)
        opponent = []
        print("\n-------------------- GAME OVER --------------------\n")
        homescreen()
    elif(opponent.starting_HP <= 0):
        print(opponent.victory)
        opponent = []
        if (current_position == "C"):
            search_cave()
        player_actions()
        
# When the player "investigates" the witch's hut, when on this space and depending on which visit -
# determined by first_visit being false or True            
def witch_hut_event():
    global first_visit
    knock_knock_witch = input("\nDo you dare to knock on the witch's door (yes or no)?\n Input: ")
    if (knock_knock_witch == "Yes") or (knock_knock_witch == "YES") or (knock_knock_witch == "yes"):
        print("You knock on the old wood door.\n")
        print("???: Enter.\n")
        print("You push open the door. It creaks slowly as it shuts behind you. Scanning the room, you notice a plain table and simple kitchen on one side of the hut. Against the back wall is a grey stone fireplace that is gently burning and a cauldron full of vegetables and broth. Next to the fireplace is a robed elderly woman, who is rocking back and forth in her chair.\n")
        if (first_visit == True):
            first_conversation()
        elif ("Green Gem" in player_character.key_items_inventory):
            green_gem_conversation()
        elif (first_visit == False):
            print("You are familiar with the witch now, and she has nothing more to say (for now).")
            player_actions()
    elif (knock_knock_witch == "No") or (knock_knock_witch == "NO") or (knock_knock_witch == "no"):
        print("The ominous energy that emanates from the old shack keeps you from approaching it. You decide to leave the witch's hut alone.\n")
        player_actions()

# This function outlines the first conversation that the player can have with the witch, Annabelle        
def first_conversation():
    global plot_count
    global first_visit
    global green_gem_quest
    if (plot_count == 4):
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
        first_visit = False
        green_gem_quest = True
        plot_count = 0
        player_actions()
    conversation_choices = input("These are the question choices. Just type in the number next to each question to ask this question.\n1. Who are you?\n2. What is this hut doing in the middle of the woods?\n3. What are you making?\n4. What is this place?\nInput Number: ")
    if (conversation_choices == "1"):
        count = True
        print("???: Who I am is not important, but it would be rude to not provide a name. You may call me Annabelle, and all I am is a mere device to push the plot forward and aid you on your journey.\n")
        if (count == True):
            plot_count = plot_count + 1
            count = False
        first_conversation()
    elif (conversation_choices == "2"):
        count = True
        print("???: The previous owner built it here. For one reason or another. I do not proclaim to understand what motivates one to build a home far from civilization. It was abandoned long before I uptook residence in it.\n")
        if (count == True):
            plot_count = plot_count + 1
            count = False
        first_conversation()
    elif (conversation_choices == "3"):
        count = True
        print("???: It's not a magical concoction, if that was your first assumption. This is a concoction of different vegetables and herbs that I grew in my garden and found in the forest. You are welcome to a bowl once it is finished cooking.\n")
        if (count == True):
            plot_count = plot_count + 1
            count = False
        first_conversation()
    elif (conversation_choices == "4"):
        count = True
        print("???: An old hut in the forest. And my home. There is nothing more to this place than what you see, but you do not have to take my word for it.\n")
        if (count == True):
            plot_count = plot_count + 1
            count = False
        first_conversation()

# This function introduces the exposition of climbing into the plains underground passage
def explore_trapdoor():
    print("You clear some of the briar and open the trapdoor. It opens with ease, and you find a worn ladder that leads into a dirt tunnel. You climb down the ladder and find yourself in a small cave that is overgrown with vegetation from the surface. None of the plants appear dangerous or abnormal, and there are small holes which allow trickles of light into the cave.\n")
    print("Walking down the tunnel, you have no issues seeing what is ahead or along the tunnel walls. After a couple of minutes, the tunnel leads slightly downwards before opening up into a larger chamber. The chamber is coated with vines and foliage. You have a peculiar feeling that the green gem Annabelle wants is in here.\n")
    search_cave()

# This function allows the user to decide if they wish to continue looking around the overgrown cave for
# the green gem            
def search_cave():
    global current_position
    global opponent
    find_gem_option = input("As you gaze around the overgrown chamber, do you wish to keep searching for the gem?\nInput (Yes or No): ")
    if (find_gem_option == "Yes") or (find_gem_option == "YES") or (find_gem_option == "yes"):
        current_position = "C"
        search = random.randint(1, 5)
        search = search + player_character[9]
        if (search <= 4):
            print("Despite ripping out some leaves and roots, you fail to find anything that resembles a gem.\n")
        elif (search > 4 and search <= 7):
            opponent = OrneryOnion()
            print("When you overturn a large vine, an overgrown vegetable rolls out. You step back, and it gives you a creepy and angry smirk.")
            combat()
        elif (search > 7):
            if "Green Gem" in player_character.key_items_inventory:
                print("As you begin oveturning some vines and leaves, you stop. You realize that you won't find another gem. You decide to return to the mouth of the cave and figure out what you want to do.\n")
            else:
                print("Tearing a couple vines away, you see a faint glimmer beneath the overgrowth.\n")
                print("You continue ripping away more and more vines, and cradled beneath a large leaf is the " + GreenGem().name + ".\nYou pick it up and place it in your satchel. Annabelle will be pleased by your discovery.\n")
                found_gem = GreenGem().name
                player_character.key_items_inventory.append(found_gem)
                print("You leave the cave with no issues and return to the surface.\n")
                current_position == " "
                player_actions()
        search_cave()
    elif (find_gem_option == "No") or (find_gem_option == "NO") or (find_gem_option == "no"):
        print("You decide that it would be best to return to the cave when you have had time to prepare.\n")
        current_position == " "
        player_actions()
    else: 
        print("The shadows beneath the overgrowth mess with you mind, and you cannot decide on an action to take.\n")
        search_cave()
        
# this function outlines the conversation the player has with Annabelle if the player has the Green Gem in their 
# inventory --> in the future, this will progress the story further and expand the map to be 5 x 5 (2D)
def green_gem_conversation():
    global green_gem_quest
    print("Annabelle: Hm. You found it.\n")
    print("You pull out the gem from your satchel. Her dark eyes twinkle for a brief moment before hiding themselves beneath her hood.\n")
    print("Annabelle: You are wondering why I wanted you to find this gem, if am reading your mind correctly. Please, have a seat.\n")
    print("You sit in the chair across from Annabelle. The cauldron blows a new smell onto you, one that is meaty and sweet.\n")
    print("Annabelle: This gem was designated to be the first key in undoing the curse that shrank and condensed our world into something simple and predictable. Please hand it to me.\n")
    print("Though you do not fully understand her words, you hand her the gem. When you give it to her, it begins to faintly shine like a dull star. The gem's green colors twist and fade into different hues, and its glow colors the shadows inside of the hut.\n")
    player_character.key_items_inventory.remove("Green Gem")
    print("Annabelle: When the curse was cast, several keys to undoing it were created. One of these keys took the form of this gemstone. With it, I can undoa small piece of the curse.\n")
    green_gem_quest = False
    print("THIS IS WHERE THE GAME ENDS SO FAR!!  MORE TO COME IN THE FUTURE!!\n")

# Based on the item that the player wishes to access, if they choose a fruit/consumable item, then the
# player is healed by that item. If the player has no items or types in something that cannot be consumed,
# then         
def use_item():
    chosen_item = input("You open your satchel and rummage through your items. Think of which item you would like to use. \n Input: ")
    if (len(player_character.consumables_inventory) > 0):
        if (chosen_item == "Berries") or (chosen_item == "BERRIES") or (chosen_item == "berries"):
            chosen_item = Berries()
        elif (chosen_item == "Apple") or (chosen_item == "APPLE") or (chosen_item == "apple"):
            chosen_item = Apple()
        elif (chosen_item == "Grapes") or (chosen_item == "GRAPES") or (chosen_item == "grapes"):
            chosen_item = Grapes()
        elif (chosen_item == "Carrot") or (chosen_item == "CARROT") or (chosen_item == "carrot"):
            chosen_item = Carrot()
        elif (chosen_item == "Onion") or (chosen_item == "ONION") or (chosen_item == "onion"):
            chosen_item = Onion()
        elif (chosen_item == "Honey") or (chosen_item == "HONEY") or (chosen_item == "honey"):
            chosen_item = Honey()
        elif (chosen_item == "Veggie Soup") or (chosen_item == "VEGGIE SOUP") or (chosen_item == "veggie soup"):
            chosen_item = VeggieSoup()
        print("Going through your bag, you pull out " + chosen_item + " . You take a couple of bites, and it partially fills your stomach and heals you. \n")
        player_character.starting_HP = player_character.starting_HP + chosen_item.heal_HP_value
        player_character.starting_MP = player_character.starting_MP + chosen_item.heal_MP_value
        player_character.consumables_inventory.remove(chosen_item)
        player_actions()
    elif (len(player_character.consumables_inventory) == 0):
        print("Your satchel is empty. Maybe you need to collect a few items in the area. \n")
    else:
        print("Looking at " + chosen_item + ", you realize that you cannot consume this. Or better said, it would probably hurt you if it did. You close your satchel and take a moment to think about what you really want. \n")
        player_actions()
    
homescreen()