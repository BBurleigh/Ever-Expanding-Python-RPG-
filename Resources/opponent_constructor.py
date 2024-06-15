# The opponent constructor - contains all of the base information for every opponent that will be faced by the 
# player --> this contains the opponent's name, class, HP, MP, level, other stats, how much EXP the player can gain
# upon victory, money dropped upon victory, a potential common drop item, a potential rare drop item, and messages 
# to display during combat based on which opponent is being fought
class Opponent(object):
    def __init__(self, name, class_, starting_HP, starting_MP, level, strength, dexterity, intelligence, agility, luck, constitution, willpower, EXP, money, commonItem, rareItem, melee_attack, range_attack, magic_attack, flee, victory, defeat):
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
        self.money = money
        self.commonItem = commonItem
        self.rareItem = rareItem
        self.melee_attack = melee_attack
        self.range_attack = range_attack
        self.magic_attack = magic_attack
        self.flee = flee
        self.victory = victory
        self.defeat = defeat
        
    # # Information about the Bad Bunny 
    # @classmethod   
    # def create_bad_bunny(cls):
    #     return Opponent("Bad Bunny", "animal", 6, 5, 1, 1, 2, 1, 3, 3, 1, 1, 2, 0, "Carrot", "Rabbit's Foot", "The Bad Bunny hustles up to you and kicks your leg!", "The Bad Bunny picks up a random carrot and hurls it at you like a throwing dart!", "The Bad Bunny's fur glows, and you get hit with a fluffy ball of light!", "The Bad Bunny's ears prick up, and twitching its nose, it hops away from the battlefield.", "The Bad Bunny topples to the ground, defeated. Victory is yours!", "The Bad Bunny hops onto your fallen body and begins nibbling on a victory carrot. GAME OVER!")
    
    # # Information about the Sneaky Sparrow
    # # @classmethod
    # def create_sneaky_sparrow(cls):
    #     return Opponent("Sneaky Sparrow", "animal", 4, 4, 1, 2, 1, 1, 3, 2, 1, 1, 2, 0, "Twig", "Tiny Feather", "The Sneaky Sparrow dives at your head and pecks it!", "The Sneaky Sparrow picks up a small rock and drops it on your head!", "The Sneaky Sparrow's wings glow and flap harder, and a gust of wind knocks you back!", "The Sneaky Sparrow begins to fidget, and it flies from the battlefield.", "The Sneaky Sparrow flops onto the ground, defeated. Victory is yours!", "The Sneaky Sparrow keeps pecking at your head, even though you have stopped moving. GAME OVER!")
    
    # # Information about the Hungry Hobo
    # # @classmethod
    # def create_hungry_hobo(cls):
    #     return Opponent("Hungry Hobo", "bum", 9, 4, 1, 1, 1, 3, 2, 2, 1, 2, 4, 1, "Scrap", "Coarse Leather", "The Hungry Hobo tackles you and bites your arm!", "The Hungry Hobo pulls out a rotten apple from its crusty coat and chucks it at you!", "The Hungry Hobo blows on a rancid onion, and when he throws it at you, it explodes and knocks you on your back!", "The Hungry Hobo emits an incoherent wail, and it hobbles away from the battlefield.", "The Hungry Hobo wobbles back and forth. It falls on its back, and you put your foot on its lifeless chest and pose. Victory is yours!", "The Hungry Hobo drags your unmoving body off into the fields. GAME OVER!")
    
    # # Information about the Busy Big Bee
    # # @classmethod
    # def create_busy_big_bee(cls):
    #     return Opponent("Busy Big Bee", "bug", 3, 4, 1, 2, 2, 1, 4, 2, 1, 1, 2, 0, "Stinger", "Honey", "The Busy Big Bee buzzes by you and stings your arm!", "The Busy Big Bee buzzes over you and shakes off a small cloud of pollen. You cough and wheeze as it envelops you!", "The Busy Big Bee starts to vibrate violently. It spits a glob of poison on your leg, which burns!", "The Busy Big Bee hustles its fuzzy fat body back to its hive, fleeing the battlefield.", "The Busy Big Bee spins and takes a nosedive into a bush. Victory is yours!", "The Busy Big Bee has lost interest in the fight since your swollen body stopped moving. It takes its honey back to the hive. GAME OVER!")
    
    # # Information about the Rascally Raccoon
    # # @classmethod
    # def create_rascally_raccoon(cls):
    #     return Opponent("Rascally Raccoon", "animal", 7, 5, 1, 1, 3, 2, 2, 3, 2, 1, 3, 1, "Tuff of Fur", "Scrap", "The Rascally Raccoon gets you to trip on a hidden wire. You faceplant into the dirt!", "The Rascally Raccoon pulls out a slingshot from its tail and fires a hard pellet at your chest!", "The Rascally Raccoon creates unusual hand signs in quick succession. Its body expands rapidly like a balloon and knocks you into a tree!", "The Rascally Raccoon throws a smoke bomb between the two of it. When the smoke clears, the Rascally Raccoon has disappeared.", "The Rascally Raccoon takes a final and dramatic bow before its body bursts in a puff of smoke. Victory is yours!", "The Rascally Raccoon slaps a paper talisman on your back, and your body shrinks and tranforms into paper fan. It fans itself as it returns to its burrow. GAME OVER!")
    
    # # Information about the Crosseyed Cat
    # # @classmethod
    # def create_crosseyed_cat(cls):
    #     return Opponent("Rascally Raccoon", "animal", 7, 5, 1, 1, 3, 2, 2, 3, 2, 1, 3, 1, "Tuff of Fur", "Scrap", "The Rascally Raccoon gets you to trip on a hidden wire. You faceplant into the dirt!", "The Rascally Raccoon pulls out a slingshot from its tail and fires a hard pellet at your chest!", "The Rascally Raccoon creates unusual hand signs in quick succession. Its body expands rapidly like a balloon and knocks you into a tree!", "The Rascally Raccoon throws a smoke bomb between the two of it. When the smoke clears, the Rascally Raccoon has disappeared.", "The Rascally Raccoon takes a final and dramatic bow before its body bursts in a puff of smoke. Victory is yours!", "The Rascally Raccoon slaps a paper talisman on your back, and your body shrinks and tranforms into paper fan. It fans itself as it returns to its burrow. GAME OVER!")
    
    # # Information about the Lumpy Ladybug
    # # @classmethod
    # def create_lumpy_ladybug(cls):
    #     return Opponent("Lumpy Ladybug", "bug", 3, 3, 1, 1, 1, 3, 2, 4, 2, 2, 2, 0, "Berries", "Shell", "The Lumpy Ladybug curls into a ball and rolls into your shins!", "The Lumpy Ladybug spits a wad of wet leaves at you, knocking you backwards!", "The Lumpy Ladybug's wings reverberate, and a gust of flowers disorients you!", "The Lumpy Ladybug senses the impending danger of continuing the fight, and it flees from the battlefield.", "The Lumpy Ladybug crumples and curls into a ball before dying. Victory is yours!", "The Lumpy Ladybug crawls onto your still chest and bounces up and down in joy. GAME OVER!")
    
    # # Information about the Persnickety Prairie Dog
    # # @classmethod
    # def create_persnickety_prairie_dog(cls):
    #     return Opponent("Persnickety Prairie Dog", "animal", 5, 6, 1, 3, 2, 1, 3, 2, 1, 2, 3, 0, "Tuff of Fur", "Claw", "The Persnickety Prairie Dog burrows underground and jumps out of another hole behind you, tackling you to the ground!", "The Persnickety Prairie Dog dives into a hole. It pops up seconds later and throws a dirt clod at your head!", "The Persnickety Praire Dog jumps in a hole. Moments later, a small quake shakes the ground and knocks you off your feet!", "The Persnickety Prairie Dog burrows into the ground and disappears from the battlefield.", "The Persnickety Prairie Dog flops out of its hole and collapses. Victory is yours!", "A giant hole opens beneath your body, and you fall into the darkness. Hundreds of red eyes watch you fall before everything goes black. GAME OVER!")
    
    # # Information about the Ornery Onion
    # # @classmethod
    # def create_ornery_onion(cls):
    #     return Opponent("Ornery Onion", "plant", 6, 5, 1, 2, 3, 2, 2, 3, 2, 2, 3, 0, "Onion", "Vine", "The Ornery Onion slaps you with one of its vines!", "The Ornery Onion peels off a small layer of its skin, and it flings that curved peel like a boomerang at you!", "The Ornery Onion shoots a vine into the ground, and that vines shoots up and stabs you in the shoulder!", "The Ornery Onion peels off one layer of its skin as a distraction before rolling into the darkness of the cave, fleeing the battle.", "The Ornery Onion rolls to a stop, and a semi-foul stench emanates from it. Victory it yours!", "The Ornery Onion drags your body into the darkness and plants it among the overgrowth. You eventually awaken, to find yourself as an overgrown and angry onion. GAME OVER!")
    

# Below is the same information but written as subclasses
# Information about the Bad Bunny
class BadBunny(Opponent):
    def __init__(self):
        super(BadBunny, self).__init__("Bad Bunny", "animal", 6, 5, 1, 1, 2, 1, 3, 3, 1, 1, 2, 0, "Carrot", "Rabbit's Foot", "The Bad Bunny hustles up to you and kicks your leg! ", "The Bad Bunny picks up a random carrot and hurls it at you like a throwing dart! ", "The Bad Bunny's fur glows, and you get hit with a fluffy ball of light! ", "The Bad Bunny's ears prick up, and twitching its nose, it hops away from the battlefield.", "The Bad Bunny topples to the ground, defeated. Victory is yours!", "The Bad Bunny hops onto your fallen body and begins nibbling on a victory carrot. GAME OVER!")

# # Information about the Sneaky Sparrow        
class SneakySparrow(Opponent):
    def __init__(self):
        super(SneakySparrow, self).__init__("Sneaky Sparrow", "animal", 4, 4, 1, 2, 1, 1, 3, 2, 1, 1, 2, 0, "Twig", "Tiny Feather", "The Sneaky Sparrow dives at your head and pecks it! ", "The Sneaky Sparrow picks up a small rock and drops it on your head! ", "The Sneaky Sparrow's wings glow and flap harder, and a gust of wind knocks you back! ", "The Sneaky Sparrow begins to fidget, and it flies from the battlefield.", "The Sneaky Sparrow flops onto the ground, defeated. Victory is yours!", "The Sneaky Sparrow keeps pecking at your head, even though you have stopped moving. GAME OVER!")

# # Information about the Hungry Hobo
class HungryHobo(Opponent):
    def __init__(self):
        super(HungryHobo, self).__init__("Hungry Hobo", "bum", 9, 4, 1, 1, 1, 3, 2, 2, 1, 2, 4, 1, "Scrap", "Coarse Leather", "The Hungry Hobo tackles you and bites your arm! ", "The Hungry Hobo pulls out a rotten apple from its crusty coat and chucks it at you! ", "The Hungry Hobo blows on a rancid onion, and when he throws it at you, it explodes and knocks you on your back! ", "The Hungry Hobo emits an incoherent wail, and it hobbles away from the battlefield.", "The Hungry Hobo wobbles back and forth. It falls on its back, and you put your foot on its lifeless chest and pose. Victory is yours!", "The Hungry Hobo drags your unmoving body off into the fields. GAME OVER!")

# # Information about the Busy Big Bee        
class BusyBigBee(Opponent):
    def __init__(self):
        super(BusyBigBee, self).__init__("Busy Big Bee", "bug", 3, 4, 1, 2, 2, 1, 4, 2, 1, 1, 2, 0, "Stinger", "Honey", "The Busy Big Bee buzzes by you and stings your arm!", "The Busy Big Bee buzzes over you and shakes off a small cloud of pollen. You cough and wheeze as it envelops you!", "The Busy Big Bee starts to vibrate violently. It spits a glob of poison on your leg, which burns!", "The Busy Big Bee hustles its fuzzy fat body back to its hive, fleeing the battlefield.", "The Busy Big Bee spins and takes a nosedive into a bush. Victory is yours!", "The Busy Big Bee has lost interest in the fight since your swollen body stopped moving. It takes its honey back to the hive. GAME OVER!")

# # Information about the Rascally Raccoon        
class RascallyRaccoon(Opponent):
    def __init__(self):
        super(RascallyRaccoon, self).__init__("Rascally Raccoon", "animal", 7, 5, 1, 1, 3, 2, 2, 3, 2, 1, 3, 1, "Tuff of Fur", "Scrap", "The Rascally Raccoon gets you to trip on a hidden wire. You faceplant into the dirt!", "The Rascally Raccoon pulls out a slingshot from its tail and fires a hard pellet at your chest!", "The Rascally Raccoon creates unusual hand signs in quick succession. Its body expands rapidly like a balloon and knocks you into a tree!", "The Rascally Raccoon throws a smoke bomb between the two of it. When the smoke clears, the Rascally Raccoon has disappeared.", "The Rascally Raccoon takes a final and dramatic bow before its body bursts in a puff of smoke. Victory is yours!", "The Rascally Raccoon slaps a paper talisman on your back, and your body shrinks and tranforms into paper fan. It fans itself as it returns to its burrow. GAME OVER!")

# # Information about the Crosseyed Cat        
class CrosseyedCat(Opponent):
    def __init__(self):
        super(CrosseyedCat, self).__init__("Crosseyed Cat", "animal", 6, 6, 1, 2, 3, 1, 3, 3, 1, 1, 3, 0, "Tuff of Fur", "Claw", "The Crosseyed Cat turns away, feigning disinterest, before scratching you!", "The Crosseyed Cat hacks up a gross hairball, and it throws it at you!", "The Crosseyed Cat shakes its body. The fur floats around it before they fly at you like many tiny needles!", "The Crosseyed Cat slinks away in the shadows of the forest, fleeing from the battlefield.", "The Crosseyed Cat attempts to limp away before collapsing on the ground. Victory is yours!", "The Crosseyed Cat leaps on your lifeless body. It scoops out one of your eyes and bats it between its paws. GAME OVER!")

# # Information about the Lumpy Ladybug
class LumpyLadybug(Opponent):
    def __init__(self):
        super(LumpyLadybug, self).__init__("Lumpy Ladybug", "bug", 3, 3, 1, 1, 1, 3, 2, 4, 2, 2, 2, 0, "Berries", "Shell", "The Lumpy Ladybug curls into a ball and rolls into your shins!", "The Lumpy Ladybug spits a wad of wet leaves at you, knocking you backwards!", "The Lumpy Ladybug's wings reverberate, and a gust of flowers disorients you!", "The Lumpy Ladybug senses the impending danger of continuing the fight, and it flees from the battlefield.", "The Lumpy Ladybug crumples and curls into a ball before dying. Victory is yours!", "The Lumpy Ladybug crawls onto your still chest and bounces up and down in joy. GAME OVER!")

# # Information about the Persnickety Prairie Dog        
class PersnicketyPrairieDog(Opponent):
    def __init__(self):
        super(PersnicketyPrairieDog, self).__init__("Persnickety Prairie Dog", "animal", 5, 6, 1, 3, 2, 1, 3, 2, 1, 2, 3, 0, "Tuff of Fur", "Claw", "The Persnickety Prairie Dog burrows underground and jumps out of another hole behind you, tackling you to the ground! ", "The Persnickety Prairie Dog dives into a hole. It pops up seconds later and throws a dirt clod at your head! ", "The Persnickety Praire Dog jumps in a hole. Moments later, a small quake shakes the ground and knocks you off your feet! ", "The Persnickety Prairie Dog burrows into the ground and disappears from the battlefield.", "The Persnickety Prairie Dog flops out of its hole and collapses. Victory is yours!", "A giant hole opens beneath your body, and you fall into the darkness. Hundreds of red eyes watch you fall before everything goes black. GAME OVER!")

# # Information about the Ornery Onion        
class OrneryOnion(Opponent):
    def __init__(self):
        super(OrneryOnion, self).__init__("Ornery Onion", "plant", 6, 5, 1, 2, 3, 2, 2, 3, 2, 2, 3, 0, "Onion", "Vine", "The Ornery Onion slaps you with one of its vines!", "The Ornery Onion peels off a small layer of its skin, and it flings that curved peel like a boomerang at you!", "The Ornery Onion shoots a vine into the ground, and that vines shoots up and stabs you in the shoulder!", "The Ornery Onion peels off one layer of its skin as a distraction before rolling into the darkness of the cave, fleeing the battle.", "The Ornery Onion rolls to a stop, and a semi-foul stench emanates from it. Victory it yours!", "The Ornery Onion drags your body into the darkness and plants it among the overgrowth. You eventually awaken, to find yourself as an overgrown and angry onion. GAME OVER!")

# badBunny = BadBunny().name
# sneakySparrow = SneakySparrow().level
# hungryHobo = HungryHobo().class_
# busyBigBee = BusyBigBee().commonItem
# rascallyRaccoon = RascallyRaccoon().rareItem
# crosseyedCat = CrosseyedCat().melee_attack
# lumpyLadybug = LumpyLadybug().flee
# persnicketyPrairieDog = PersnicketyPrairieDog().victory
# orneryOnion = OrneryOnion().defeat

# print(badBunny)
# print(sneakySparrow)
# print(hungryHobo)
# print(busyBigBee)
# print(rascallyRaccoon)
# print(crosseyedCat)
# print(lumpyLadybug)
# print(persnicketyPrairieDog)
# print(orneryOnion)