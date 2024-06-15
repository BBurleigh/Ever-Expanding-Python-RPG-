# The player character constructor - contains all of the base information that the character, general information
# about said character, as well as other information
class PlayerCharacter(object):
    def __init__(self, name, class_, starting_HP, starting_MP, level, strength, dexterity, intelligence, agility, luck, constitution, willpower, EXP, wallet, skill_list, consumables_inventory, combat_inventory, crafting_inventory, key_items_inventory, description, melee_attack, range_attack, magic_attack, flee):
        self.name = name
        self.class_ = class_
        self.starting_HP = starting_HP
        self.starting_MP = starting_MP
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.agility = agility
        self.luck = luck
        self.constitution = constitution
        self.willpower = willpower
        self.EXP = EXP
        self.wallet = wallet
        self.skill_list = skill_list
        self.consumables_inventory = consumables_inventory
        self.combat_inventory = combat_inventory
        self.crafting_inventory = crafting_inventory
        self.key_items_inventory = key_items_inventory
        self.description = description
        self.melee_attack = melee_attack
        self.range_attack = range_attack
        self.magic_attack = magic_attack
        self.flee = flee
        
    # # Information about Noel, The Herbalist
    # def create_noel(cls):
    #     return PlayerCharacter("Noel", "Herbalist", 12, 10, 1, 3, 2, 2, 4, 3, 2, 2, 0, 0, [], [], [], [], [], "A simple and mild-mannered boy, Noel travels with a staff and is knowledgeable about herbology.", "You wind up your staff and strike your opponent center mass!", "You pull out a slingshot, steady your aim, and strike your opponent with a hard pellet", "You hold your staff outwards with both hands. Conjuring your innate magic, mushrooms sprout around your opponent and pelt them with clouds of toxic spores!", "You pull out a pepper bomb from your satchel and throw it at your opponent's feet. While they are disoriented, you take your chance to flee.")
    
    # # Information about Bianca, The Huntress
    # def create_bianca(cls):
    #     return PlayerCharacter("Bianca", "Huntress", 14, 8, 1, 2, 4, 1, 3, 2, 3, 1, 0, 0, [], [], [], [], [], "A serious and distrustful woman, Bianca spends most of her time in the wild, hunting with her bow.", "You brandish the hunting knife from the side of your boot and slice your opponent!", "Notching an arrow, you take aim. The arrow hits what appears to be a vital area on your foe!", "Stabbing your hunting knife in the ground, you conjure the image of a boar that charges into your opponent!", "You notch an arrow and let it loose. It stops you opponent in their tracks. While they are trying to free themselves, you safely withdraw from the battle.")
    
    # # Information about Pale, The Shaman
    # def create_pale(cls):
    #     return PlayerCharacter("Rocco Taco", "The Golden Floof", 10, 10, 1, 3, 4, 2, 5, 4, 4, 2, 0, 0, [], [], [], [], [], "An excitable and overly friendly puppy, Rocco Taco demands the attention of others and loves pets.", "You fly through the air like a furry buzzsaw and collide into your opponent!", "Grabbing your fuzzy soccerball, you spin in circles until releasing the ball. It soars through the air and plummets into your opponent, who flies backwards!", "Your golden fur begins to shine, and the light envelops the area. Your opponent is slightly burned and blinded!", "You bolt and leave your opponent in the dust. You have successfully fled the battle.")
    
    # # Information about Bunny, The Cosmonaut
    # def create_bunny(cls):
    #     return PlayerCharacter("Bunny", "Cosmonaut", 12, 12, 1, 2, 3, 3, 3, 4, 2, 3, 0, 0, [], [], [], [], [], "A cheerful and sassy rabbit from a distant star, Bunny travels to discover the best carrot wine.", "You summon your giant rainbow carrot and pummels your opponent!", "You summon your rainbow bunny blaster and fire a laser carrot at your opponent!", "You press your paws together and summon a carrot meteorite, which descends and plummets on your opponent. All that is left is your opponent in a crater!", "You click a button on your watch, and it teleports your far away from your opponent.")
    
    # Information about Rocco Taco, The Golden Floof
    # def create_rocco_taco(cls):
    #     return PlayerCharacter("Rocco Taco", "The Golden Floof", 10, 10, 1, 3, 4, 2, 5, 4, 4, 2, 0, 0, [], [], [], [], [], "An excitable and overly friendly puppy, Rocco Taco demands the attention of others and loves pets.", "You fly through the air like a furry buzzsaw and collide into your opponent!", "Grabbing your fuzzy soccerball, you spin in circles until releasing the ball. It soars through the air and plummets into your opponent, who flies backwards!", "Your golden fur begins to shine, and the light envelops the area. Your opponent is slightly burned and blinded!", "You bolt and leave your opponent in the dust. You have successfully fled the battle.")
    
    # Information about Annabelle, The Witch
    # def create_annabelle(cls):
    #     return PlayerCharacter("Annabelle", "Witch", 8, 16, 1, 1, 2, 5, 3, 4, 2, 5, 0, 0, [], [], [], [], [], "An elderly woman who has many stories to tell, Annabelle is searching for one more adventure to excite her old bones.", "Pulling out a ladle from beneath your robes, you whack your opponent with it!", "A cauldron of boiling soup appears beside you, and with your ladle, you fling a molten wad of soup at your opponent!", "You take out your pipe, and with a puff, a whirlwind of smoke buffets against your opponent!", "Taking a puff on your pipe, you are enveloped in a cloud of smoke. You appear in another area, successfully fleeing that battle.")

# Below is the same information written as subclasses
# Information about Noel, The Herbalist
class Noel(PlayerCharacter):
    def __init__(self):
        super(Noel, self).__init__("Noel", "Herbalist", 12, 10, 1, 3, 2, 2, 4, 3, 2, 2, 0, 0, [], [], [], [], [], "A simple and mild-mannered boy, Noel travels with a staff and is knowledgeable about herbology.", "You wind up your staff and strike your opponent center mass!", "You pull out a slingshot, steady your aim, and strike your opponent with a hard pellet", "You hold your staff outwards with both hands. Conjuring your innate magic, mushrooms sprout around your opponent and pelt them with clouds of toxic spores!", "You pull out a pepper bomb from your satchel and throw it at your opponent's feet. While they are disoriented, you take your chance to flee.")
        
# # Information about Bianca, The Huntress
class Bianca(PlayerCharacter):
    def __init__(self):
        super(Bianca, self).__init__("Bianca", "Huntress", 14, 8, 1, 2, 4, 1, 3, 2, 3, 1, 0, 0, [], [], [], [], [], "A serious and distrustful woman, Bianca spends most of her time in the wild, hunting with her bow.", "You brandish the hunting knife from the side of your boot and slice your opponent!", "Notching an arrow, you take aim. The arrow hits what appears to be a vital area on your foe!", "Stabbing your hunting knife in the ground, you conjure the image of a boar that charges into your opponent!", "You notch an arrow and let it loose. It stops you opponent in their tracks. While they are trying to free themselves, you safely withdraw from the battle.")
        
# # Information about Pale, The Shaman
class Pale(PlayerCharacter):
    def __init__(self):
        super(Pale, self).__init__("Pale", "Shaman", 10, 14, 1, 1, 1, 4, 2, 3, 1, 3, 0, 0, [], [], [], [], [], "A quiet and lonesome man from a local tribe, Pale seeks solitude and often communes with spirits.", "You assume a defensive stance, and when your opponent charges, you redirect their momentum into the ground!", "You wait for your opponent to step back, and you grab a giant fist of dirt. You hurl it at your opponent!", "You close your eyes and briefly connect with the spirit realm. A sickle of undead energy whips across the air and slashes through your opponent, damaging their spirit!", "You create a replica of yourself with undead energy, and while your opponent is focused on attacking the duplicate, you withdraw from the fight.")

# # Information about Bunny, The Cosmonaut
class Bunny(PlayerCharacter):
    def __init__(self):
        super(Bunny, self).__init__("Bunny", "Cosmonaut", 12, 12, 1, 2, 3, 3, 3, 4, 2, 3, 0, 0, [], [], [], [], [], "A cheerful and sassy rabbit from a distant star, Bunny travels to discover the best carrot wine.", "You summon your giant rainbow carrot and pummels your opponent!", "You summon your rainbow bunny blaster and fire a laser carrot at your opponent!", "You press your paws together and summon a carrot meteorite, which descends and plummets on your opponent. All that is left is your opponent in a crater!", "You click a button on your watch, and it teleports your far away from your opponent.")
        
# # Information about Rocco Taco, The Golden Floof
class RoccoTaco(PlayerCharacter):
    def __init__(self):
        super(RoccoTaco, self).__init__("Rocco Taco", "The Golden Floof", 10, 10, 1, 3, 4, 2, 5, 4, 4, 2, 0, 0, [], [], [], [], [], "An excitable and overly friendly puppy, Rocco Taco demands the attention of others and loves pets.", "You fly through the air like a furry buzzsaw and collide into your opponent!", "Grabbing your fuzzy soccerball, you spin in circles until releasing the ball. It soars through the air and plummets into your opponent, who flies backwards!", "Your golden fur begins to shine, and the light envelops the area. Your opponent is slightly burned and blinded!", "You bolt and leave your opponent in the dust. You have successfully fled the battle.")
        
# # Information about Annabelle, The Witch
class Annabelle(PlayerCharacter):
    def __init__(self):
        super(Annabelle, self).__init__("Annabelle", "Witch", 8, 16, 1, 1, 2, 5, 3, 4, 2, 5, 0, 0, [], [], [], [], [], "An elderly woman who has many stories to tell, Annabelle is searching for one more adventure to excite her old bones.", "Pulling out a ladle from beneath your robes, you whack your opponent with it!", "A cauldron of boiling soup appears beside you, and with your ladle, you fling a molten wad of soup at your opponent!", "You take out your pipe, and with a puff, a whirlwind of smoke buffets against your opponent!", "Taking a puff on your pipe, you are enveloped in a cloud of smoke. You appear in another area, successfully fleeing that battle.")
        
# herbalist = Noel().name
# huntress = Bianca().class_
# shaman = Pale().combat_inventory
# cosmonaut = Bunny().agility
# goldenFloof = RoccoTaco().description
# witch = Annabelle().EXP

# print(herbalist)
# print(huntress)
# print(shaman)
# print(cosmonaut)
# print(goldenFloof)
# print(witch)