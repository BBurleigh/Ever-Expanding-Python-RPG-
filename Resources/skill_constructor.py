# Will need to make a constructor and subclasses for each skill that the player can learn upon leaving up
# The skill constructor - contains all of the information related to skills, such as their base description, what
# effects each has during combat (or outside of combat for some), the cost of using said skill, and some other 
# information
class Skill(object):
    def __init__(self, name, level_obtained, class_requirement, general_description, HP_cost, MP_cost, physical_damage, magical_damage, heal_amount, combat_description, type_melee, type_range, type_magic, type_support, combat_only):
        self.name = name
        self.level_obtained = level_obtained
        self.class_requirement = class_requirement
        self.general_description = general_description
        self.HP_cost = HP_cost
        self.MP_cost = MP_cost
        self.physical_damage = physical_damage
        self.magical_damage = magical_damage
        self.heal_amount = heal_amount
        self.combat_description = combat_description
        self.type_melee = type_melee
        self.type_range = type_range
        self.type_magic = type_magic
        self.type_support = type_support
        self.combat_only = combat_only
    
    # # Information about the skill Salve   
    # def Salve(cls):
    #     return Skill("Salve", 2, "Herbalist", "A minor healing topical cream, when applied on wounds, helps soothe pain and heal minor wounds.", 0, 2, 0, 0, 4, "You pull out a vial from your satchel and quickly lather your wounds with it, stopping the pain and healing you a bit!", False, False, False, True, False)
    
    # # Information about the skill Aim
    # def Aim(cls):
    #     return Skill("Aim", 2, "Huntress", "Focus in the midst of battle and target a vital/weak area on your opponent.", 0, 2, 5, 0, 0, "You steady your breath and notch an arrow. Tightening your core, you release your breath. The arrow flies and hits a vital area on your opponent!", False, True, False, False, True)
    
    # # Information about the skill Branch
    # def Branch(cls):
    #     return Skill("Branch", 2, "Shaman", "You call forth prickly branches to immobilize or potentially impale an opponent.", 0, 3, 0, 3, 0, "You whisper into the air, and barbed branches jut out of the ground and pierce your opponent!", False, False, True, False, True)
    
    # # Information about the skill Glitter
    # def Glitter(cls):
    #     return Skill("Glitter", 2, "Cosmonaut", "Magical glitter scatters through the air around you, purifying the area.", 0, 3, 0, 4, 2, "You spin in a circle, and colorful glitter fills the air and scatters throughout the nearby area. Your opponent is knocked around by the glitter as it bursts, and you feel a little better!", False, False, True, False, True)
    
    # # Information about the skill Tail Whip
    # def TailWhip(cls):
    #     return Skill("Tail Whip", 2, "The Golden Floof", "With your mighty tail, you whack your opponent.", 0, 1, 4, 0, 0, "You whorl at your opponent. With a leap, your tail collides with your opponent's face!", True, False, False, False, True)
    
    # # Information about the skill Smoke Ring
    # def SmokeRing(cls):
    #     return Skill("Smoke Ring", 2, "Witch", "With your pipe, you create a massive smoke ring that burns and blinds your opponent.", 0, 3, 0, 4, 0, "Taking a puff on your pipe, you exhale a massive ring of black smog.  The smoke wraps itself around your opponent, burning and blinding them!", False, False, True, False, True)

# Below is the sanme information written as subclasses        
# Information about the skill Salve
class Salve(Skill):
    def __init__(self):
        super(Salve, self).__init__("Salve", 2, "Herbalist", "A minor healing topical cream, when applied on wounds, helps soothe pain and heal minor wounds.", 0, 2, 0, 0, 4, "You pull out a vial from your satchel and quickly lather your wounds with it, stopping the pain and healing you a bit!", False, False, False, True, False)
        
# # Information about the skill Aim
class Aim(Skill):
    def __init__(self):
        super(Aim, self).__init__("Aim", 2, "Huntress", "Focus in the midst of battle and target a vital/weak area on your opponent.", 0, 2, 5, 0, 0, "You steady your breath and notch an arrow. Tightening your core, you release your breath. The arrow flies and hits a vital area on your opponent!", False, True, False, False, True)
        
# # Information about the skill Branch
class Branch(Skill):
    def __init__(self):
        super(Branch, self).__init__("Branch", 2, "Shaman", "You call forth prickly branches to immobilize or potentially impale an opponent.", 0, 3, 0, 3, 0, "You whisper into the air, and barbed branches jut out of the ground and pierce your opponent!", False, False, True, False, True)
        
# # Information about the skill Glitter
class Glitter(Skill):
    def __init__(self):
        super(Glitter, self).__init__("Glitter", 2, "Cosmonaut", "Magical glitter scatters through the air around you, purifying the area.", 0, 3, 0, 4, 2, "You spin in a circle, and colorful glitter fills the air and scatters throughout the nearby area. Your opponent is knocked around by the glitter as it bursts, and you feel a little better!", False, False, True, False, True)
        
# # Information about the skill Tail Whip
class TailWhip(Skill):
    def __init__(self):
        super(TailWhip, self).__init__("Tail Whip", 2, "The Golden Floof", "With your mighty tail, you whack your opponent.", 0, 1, 4, 0, 0, "You whorl at your opponent. With a leap, your tail collides with your opponent's face!", True, False, False, False, True)
        
# # Information about the skill Smoke Ring
class SmokeRing(Skill):
    def __init__(self):
        super(SmokeRing, self).__init__("Smoke Ring", 2, "Witch", "With your pipe, you create a massive smoke ring that burns and blinds your opponent.", 0, 3, 0, 4, 0, "Taking a puff on your pipe, you exhale a massive ring of black smog.  The smoke wraps itself around your opponent, burning and blinding them!", False, False, True, False, True)

# salve = Salve().class_requirement
# aim = Aim().level_obtained
# branch = Branch().name
# glitter = Glitter().magical_damage
# tailWhip = TailWhip().MP_cost
# smokeRing = SmokeRing().type_magic

# print(salve)
# print(aim)
# print(branch)
# print(glitter)
# print(tailWhip)
# print(smokeRing)