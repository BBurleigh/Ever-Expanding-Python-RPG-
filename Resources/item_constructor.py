# The item constructor contains all of the base information for every item found within the game, whether foraged,
# dropped from an opponent, or (later) bought in a store as well as what type of item it is
class Items(object):
    def __init__(self, name, general_description, heal_HP_value, heal_MP_value, damage_HP_value, damage_MP_value, sell_value, purchase_value, use_description, key_item, consumable_item, combat_item, crafting_item):
        self.name = name
        self.general_description = general_description
        self.heal_HP_value = heal_HP_value
        self.heal_MP_value = heal_MP_value
        self.damage_HP_value = damage_HP_value
        self.damage_MP_value = damage_MP_value
        self.sell_value = sell_value
        self.purchase_value = purchase_value
        self.use_description = use_description
        self.key_item = key_item
        self.consumable_item = consumable_item
        self.combat_item = combat_item
        self.crafting_item = crafting_item
        
    # This section contains the items that can be consumed by the player ----------------------------------------
    # Information about the item "Berries"
    # def Berries(cls):
    #     return Items("Berries", "A handful of common and tiny fruits", 3, 0, 0, 0, 1, 4, "You pull out a handful of berries from your satchel and quickly eat them. Their juices have very limited healing properties, and you feel a little better.", False, True, False, False)
    
    # # Information about the item "Carrot"
    # def Carrot(cls):
    #     return Items("Carrot", "A pointy and crunchy orange vegetable", 2, 0, 0, 0, 1, 3, "You pull out a carrot from your satchel and quickly munch on it. You feel a little better.", False, True, False, False)
    
    # # Information about the item "Grapes"
    # def Grapes(cls):
    #     return Items("Grapes", "A bunch of purple berries that can be used to make wine", 0, 4, 0, 0, 3, 10, "You pull out some grapes from your satchel and slurp down each one. The juices run down your throat, and you feel slightly restored.", False, True, False, False)
    
    # # Information about the item "Onion"
    # def Onion(cls):
    #     return Items("Onion", "An edible bulb with multiple layers and a bitter taste", 2, 2, 0, 0, 2, 8, "You pull out an onion from your satchel and begin to peel and eat it. Its taste and smell sting, but you feel weirdly better after a moment.", False, True, False, False)
    
    # # Information about the item "Apple"
    # def Apple(cls):
    #     return Items("Apple", "A round and red fruit with a crisp taste", 5, 0, 0, 0, 2, 8, "You pull out an applie from your satchel and take a several bites out of it. The crisp taste fills your mouth, and you feel better.", False, True, False, False)
    
    # # Information about the item "Honey"
    # def Honey(cls):
    #     return Items("Honey", "Sweet golden nectar created by the bees", 3, 6, 0, 0, 5, 20, "You unfasten a small jar and guzzle down the honey. Its sticky sweetness rejuvenates you.", False, True, False, False)
    
    # # Information about the item "Veggie Soup"
    # def VeggieSoup(cls):
    #     return Items("Veggie Soup", "A warm bowl of thick soup with pieces of vegetables in it", 10, 5, 0, 0, 8, 30, "You pull out the veggie soup from your satchel and remove the top from the bowl. The warmth wafts through your nose as you slurp down the soup. You feel reinvigorated.", False, True, False, False)
    
    # # This section contains the items that the player can use during combat ----------------------------------------
    # # Information about the item "Thorns"
    # def Thorns(cls):
    #     return Items("Thorns", "A couple of long wooden thorns pulled from a briar patch", 0, 0, 2, 0, 0, 3, "You brandish several thorns and throw them like knives at your opponent!", False, False, True, False)
    
    # # Information about the item "Rocks"
    # def Rocks(cls):
    #     return Items("Rocks", "A small pile of pebbles that are harder than they look", 0, 0, 4, 0, 0, 4, "From your satchel, you pull out a handful of rocks and throw them at your opponent!", False, False, True, False)
    
    # # Information about the item "Bomb"
    # def Bomb(cls):
    #     return Items("Bomb", "A small black bomb that creates a minor explosion when lit", 0, 0, 10, 0, 10, 40, "From your satchel, you pull out a small bomb. Lighting it, you toss the bomb at your opponent, and it explodes!", False, False, True, False)
    
    # # This section contains the items that the player can use for crafting (will be added later) ----------------
    # # Information about the item "Tuft of Fur"
    # def TuftOfFur(cls):
    #     return Items("Tuft of Fur", "A small and loosely bound collection of animal hair/fur", 0, 0, 0, 0, 1, 5, "You pull out a tuft of fur from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Small Feather"
    # def SmallFeather(cls):
    #     return Items("Tiny Feather", "A small and ordinary bird feather", 0, 0, 0, 0, 0, 3, "You pull out a tiny feather from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Scraps"
    # def Scraps(cls):
    #     return Items("Scraps", "A small collection of garbage/trash", 0, 0, 0, 0, 2, 8, "You pull out some scraps from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Twig"
    # def Twig(cls):
    #     return Items("Twig", "A small and fragile stick", 0, 0, 0, 0, 0, 2, "You pull out a twig from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Vine"
    # def Vine(cls):
    #     return Items("Vine", "A long and somewhat sturdy piece of a plant", 0, 0, 0, 0, 1, 6, "You pull out a vine from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Stinger"
    # def Stinger(cls):
    #     return Items("Stinger", "A large insect barb with a litle venom left in it", 0, 0, 0, 0, 0, 3, "You pull out a stinger from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Claw"
    # def Claw(cls):
    #     return Items("Claw", "A small and partially crooked animal talon that is a little sharp", 0, 0, 0, 0, 2, 8, "You pull out a claw from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Shell"
    # def Shell(cls):
    #     return Items("Shell", "A large and partially plated exoskeleton", 0, 0, 0, 0, 2, 10, "You pull out a shell from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Coarse Leather"
    # def CoarseLeather(cls):
    #     return Items("Coarse Leather", "A pelt of unrefined/raw hide", 0, 0, 0, 0, 4, 16, "You pull out some coarse leather from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # Information about the item "Rabbit's Foot"
    # def RabbitsFoot(cls):
    #     return Items("Rabbit's Foot", "A small severed paw of a rabbit, which is said bring the holder luck (but not the bunny)", 0, 0, 0, 0, 8, 32, "You pull out a rabbit's foot from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
    
    # # This section contains items that the player will use to advance the storyline or side quests --------------
    # # Information about the item "Green Gem"
    # def GreenGem(cls):
    #     return Items("Green Gem", "A small and partially cut emerald that fits in the palm of one's hand", 0, 0, 0, 0, 0, 0, "You pull out the green gem, but you put it back in your satchel. It is too important to throw at the opponent.", True, False, False, False)

# This section contains the items that can be consumed by the player --------------------------------------------
# Information about the item "Berries"
class Berries(Items):
    def __init__(self):
        super(Berries, self).__init__("Berries", "A handful of common and tiny fruits", 3, 0, 0, 0, 1, 4, "You pull out a handful of berries from your satchel and quickly eat them. Their juices have very limited healing properties, and you feel a little better.", False, True, False, False)

# Information about the item "Carrot"
class Carrot(Items):
    def __init__(self):
        super(Carrot, self).__init__("Carrot", "A pointy and crunchy orange vegetable", 2, 0, 0, 0, 1, 3, "You pull out a carrot from your satchel and quickly munch on it. You feel a little better.", False, True, False, False)

# Information about the item "Grapes"
class Grapes(Items):
    def __init__(self):
        super(Grapes, self).__init__("Grapes", "A bunch of purple berries that can be used to make wine", 0, 4, 0, 0, 3, 10, "You pull out some grapes from your satchel and slurp down each one. The juices run down your throat, and you feel slightly restored.", False, True, False, False)

# Information about the item "Onion"        
class Onion(Items):
    def __init__(self):
        super(Onion, self).__init__("Onion", "An edible bulb with multiple layers and a bitter taste", 2, 2, 0, 0, 2, 8, "You pull out an onion from your satchel and begin to peel and eat it. Its taste and smell sting, but you feel weirdly better after a moment.", False, True, False, False)
        
# Information about the item "Apple"
class Apple(Items):
    def __init__(self):
        super(Apple, self).__init__("Apple", "A round and red fruit with a crisp taste", 5, 0, 0, 0, 2, 8, "You pull out an applie from your satchel and take a several bites out of it. The crisp taste fills your mouth, and you feel better.", False, True, False, False)

# Information about the item "Honey"        
class Honey(Items):
    def __init__(self):
        super(Honey, self).__init__("Honey", "Sweet golden nectar created by the bees", 3, 6, 0, 0, 5, 20, "You unfasten a small jar and guzzle down the honey. Its sticky sweetness rejuvenates you.", False, True, False, False)
        
# Information about the item "Veggie Soup"
class VeggieSoup(Items):
    def __init__(self):
        super(VeggieSoup, self).__init__("Veggie Soup", "A warm bowl of thick soup with pieces of vegetables in it", 10, 5, 0, 0, 8, 30, "You pull out the veggie soup from your satchel and remove the top from the bowl. The warmth wafts through your nose as you slurp down the soup. You feel reinvigorated.", False, True, False, False)

# This section contains the items that the player can use during combat ------------------------------------------
# Information about the item "Thorns"
class Thorns(Items):
    def __init__(self):
        super(Thorns, self).__init__("Thorns", "A couple of long wooden thorns pulled from a briar patch", 0, 0, 2, 0, 0, 3, "You brandish several thorns and throw them like knives at your opponent!", False, False, True, False)

# Information about the item "Rocks"        
class Rocks(Items):
    def __init__(self):
        super(Rocks, self).__init__("Rocks", "A small pile of pebbles that are harder than they look", 0, 0, 4, 0, 0, 4, "From your satchel, you pull out a handful of rocks and throw them at your opponent!", False, False, True, False)
        
# Information about the item "Bomb"
class Bomb(Items):
    def __init__(self):
        super(Bomb, self).__init__("Bomb", "A small black bomb that creates a minor explosion when lit", 0, 0, 10, 0, 10, 40, "From your satchel, you pull out a small bomb. Lighting it, you toss the bomb at your opponent, and it explodes!", False, False, True, False)

# This section contains the items that the player can use for crafting (system will be implemented later) --------
# Information about the item "Tuft of Fur"
class TuftOfFur(Items):
    def __init__(self):
        super(TuftOfFur, self).__init__("Tuft of Fur", "A small and loosely bound collection of animal hair/fur", 0, 0, 0, 0, 1, 5, "You pull out a tuft of fur from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Tiny Feather"
class TinyFeather(Items):
    def __init__(self):
        super(TinyFeather, self).__init__("Tiny Feather", "A small and ordinary bird feather", 0, 0, 0, 0, 0, 3, "You pull out a tiny feather from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Scraps"
class Scraps(Items):
    def __init__(self):
        super(Scraps, self).__init__("Scraps", "A small collection of garbage/trash", 0, 0, 0, 0, 2, 8, "You pull out some scraps from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Twig"
class Twig(Items):
    def __init__(self):
        super(Twig, self).__init__("Twig", "A small and fragile stick", 0, 0, 0, 0, 0, 2, "You pull out a twig from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Vine"
class Vine(Items):
    def __init__(self):
        super(Vine, self).__init__("Vine", "A long and somewhat sturdy piece of a plant", 0, 0, 0, 0, 1, 6, "You pull out a vine from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)

# Information about the item "Stinger"
class Stinger(Items):
    def __init__(self):
        super(Stinger, self).__init__("Stinger", "A large insect barb with a litle venom left in it", 0, 0, 0, 0, 0, 3, "You pull out a stinger from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Claw"
class Claw(Items):
    def __init__(self):
        super(Claw, self).__init__("Claw", "A small and partially crooked animal talon that is a little sharp", 0, 0, 0, 0, 2, 8, "You pull out a claw from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)

# Information about the item "Shell"
class Shell(Items):
    def __init__(self):
        super(Shell, self).__init__("Shell", "A large and partially plated exoskeleton", 0, 0, 0, 0, 2, 10, "You pull out a shell from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Coarse Leather"
class CoarseLeather(Items):
    def __init__(self):
        super(CoarseLeather, self).__init__("Coarse Leather", "A pelt of unrefined/raw hide", 0, 0, 0, 0, 4, 16, "You pull out some coarse leather from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# Information about the item "Rabbit's Foot"
class RabbitsFoot(Items):
    def __init__(self):
        super(RabbitsFoot, self).__init__("Rabbit's Foot", "A small severed paw of a rabbit, which is said bring the holder luck (but not the bunny)", 0, 0, 0, 0, 8, 32, "You pull out a rabbit's foot from your satchel and toss it at your opponent, which does nothing.", False, False, False, True)
        
# This section contains items that the player will use to advance the main storyline or side quests ---------------
# # Information about the item "Green Gem"
class GreenGem(Items):
    def __init__(self):
        super(GreenGem, self).__init__("Green Gem", "A small and partially cut emerald that fits in the palm of one's hand", 0, 0, 0, 0, 0, 0, "You pull out the green gem, but you put it back in your satchel. It is too important to throw at the opponent.", True, False, False, False)
        
# berries = Berries().name
# carrot = Carrot().consumable_item
# grapes = Grapes().crafting_item
# onion = Onion().heal_HP_value
# apple = Apple().heal_MP_value
# honey = Honey().purchase_value
# veggieSoup = VeggieSoup().sell_value
# thorns = Thorns().damage_MP_value
# rocks = Rocks().damage_HP_value
# bomb = Bomb().general_description
# tuftOfFur = TuftOfFur().use_description
# tinyFeather = TinyFeather().crafting_item
# scraps = Scraps().consumable_item
# twig = Twig().name
# stinger = Stinger().sell_value
# claw = Claw().sell_value
# shell = Shell().damage_MP_value
# coarseLeather = CoarseLeather().key_item
# rabbitsFoot = RabbitsFoot().use_description
# greenGem = GreenGem().key_item

# print(berries)
# print(carrot)
# print(grapes)
# print(onion)
# print(apple)
# print(honey)
# print(veggieSoup)
# print(thorns)
# print(rocks)
# print(bomb)
# print(tuftOfFur)
# print(tinyFeather)
# print(scraps)
# print(twig)
# print(stinger)
# print(claw)
# print(shell)
# print(coarseLeather)
# print(rabbitsFoot)
# print(greenGem)