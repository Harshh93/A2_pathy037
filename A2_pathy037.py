'''
File: A2_pathy037.py 
Description: This file has the main code of the assignment.
Author: Harsh Manishkumar Patel
StudentID: 110403785
EmailID: pathy037@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import math
from abc import ABC, abstractmethod

class Laboratory:
    """Represents a laboratory for potion mixing."""

    def __init__(self):
        """Initializing the Laboratory with potions, herbs, and catalysts."""
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat,  primaryingredient, secondaryingredient):
        if (primaryingredient in self.__herbs or primaryingredient in self.__catalysts)  and (secondaryingredient in self.__catalysts or secondaryingredient in self.__potions):
            # Mix potion based on the recipe
            if secondaryingredient in self.__potions:
                # Create a super potion
                super_potion = next(p for p in self.__potions if p.name == secondaryingredient)
                if type == "Super":
                    # Super potion formula: potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5
                    boost_value = primaryingredient.getPotency() + (secondaryingredient.getPotency() * secondaryingredient.getQuality()) * 1.5
                    new_potion = SuperPotion(name, stat, round(boost_value, 2), primaryingredient, secondaryingredient)
                elif type == "Extreme":
                    # Extreme potion formula: (potency of its reagent * boost value of its super potion) * 3.0
                    boost_value = (primaryingredient.getPotency() * super_potion.getBoost()) * 3.0
                    new_potion = ExtremePotion(name, stat, round(boost_value, 2), primaryingredient, super_potion)
                else:
                    print(f"Invalid potion type: {type}")
                    return
            else:
                # Create a super potion
                boost_value = (primaryingredient.getPotency() + (secondaryingredient.getPotency() * secondaryingredient.getQuality())) * 1.5
                new_potion = SuperPotion(name, stat, round(boost_value, 2), primaryingredient, secondaryingredient)

            self.__potions.append(new_potion)
        else:
            print(f"Missing ingredients for {name}.")

    def addReagent(self, reagent, amount=1):
        if isinstance(reagent, Herb):
            # Add herb to the laboratory
            self.__herbs.extend([reagent] * amount)
        elif isinstance(reagent, Catalyst):
            # Add catalyst to the laboratory
            self.__catalysts.extend([reagent] * amount)

class Alchemist:
    """Represents an alchemist who mixes potions and refines reagents."""

    def __init__(self):
        """Initialize the Alchemist with various attributes."""
        self.__attack = 0
        self.__strength = 0
        self.__defence = 0
        self.__magic = 0
        self.__range = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes = {
            "Super Attack": ("Irit", " Eye of Newt"),
            "Super Strength": ("Kwuarm", "Limpwurt Root"),
            "Super Defence": ("Cadantine", "White Berries"),
            "Super Magic": ("Lantadyme", "Potato Cactus"),
            "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
            "Super Necromancy": ("Arbuck", "Blood of Orcus"),
            "Extreme Attack": ("Avantoe", "Super Attack"),
            "Extreme Strength": ("Dwarf Weed", "Super Strength"),
            "Extreme Defence": ("Lantadyme", "Super Defence"),
            "Extreme Magic": ("Ground Mud Rune", "Super Magic"),
            "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
            "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy")
        }

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, potion_name):
        recipe = self.__recipes.get(potion_name)
        if recipe:
            primary_name, secondary_name = recipe[0], recipe[1]
            primaryIngredient = next((herb for herb in self.__laboratory._Laboratory__herbs if herb.getName() == primary_name), None)
            secondaryIngredient = next((catalyst for catalyst in self.__laboratory._Laboratory__catalysts if catalyst.getName() == secondary_name), None)

            if primaryIngredient and secondaryIngredient:
                stat_attribute = self.__recipes[potion_name]  # Assuming the stat attribute is stored directly in the recipe dictionary
                self.__laboratory.mixPotion(potion_name, recipe[2], stat_attribute, primaryIngredient, secondaryIngredient)
                print(f"Successfully mixed {potion_name}.")
            else:
                print(f"Missing ingredients for {potion_name}.")
        else:
            print(f"No recipe found for {potion_name}.")
            
    def drinkPotion(self, potion):
        if potion.getStat() == "attack":
            self.__attack += potion.getBoost()
        elif potion.getStat() == "strength":
            self.__strength += potion.getBoost()
        elif potion.getStat() == "defence":
            self.__defence += potion.getBoost()
        elif potion.getStat() == "magic": 
            self.__magic += potion.getBoost()
        elif potion.getStat() == "range":
            self.__range += potion.getBoost()
        elif potion.getStat() == "necromancy":
            self.__necromancy += potion.getBoost()
        return potion.getStat()

    def collectReagent(self, reagent, amount=1):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        for herb in self.__laboratory._Laboratory__herbs:
            herb.refine()

        for catalyst in self.__laboratory._Laboratory__catalysts:
            catalyst.refine()

class Potion(ABC):
    """Abstract base class representing a potion."""

    def __init__(self, name, stat, boost):
        """Initialize the Potion with name, stat, and boost."""
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        """Abstract method to calculate the boost value of the potion."""
        pass

    def getName(self):
        
        return self.__name

    def getStat(self):
        
        return self.__stat

    def getBoost(self):
        
        return self.__boost

    def setBoost(self, newBoost):
        self.__boost = newBoost

class SuperPotion(Potion):
    """
    Represents a super potion.

    Attributes:
    __herb (Herb): Herb used in the super potion.
    __catalyst (Catalyst): Catalyst used in the super potion.
    """
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.setBoost(round(self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5, 2))

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst

class ExtremePotion(Potion):
    """
    Represents an extreme potion.

    Attributes:
    __reagent (Reagent): Reagent used in the extreme potion.
    __potion (Potion): Potion used as a base for the extreme potion.
    """
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        self.setBoost(round((self.__reagent.getPotency() * self.__potion.getBoost()) * 3.0, 2))

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion

class Reagent(ABC):
    """
    Abstract base class representing a reagent.

    Attributes:
    __name : Name of the reagent.
    __potency : Potency value of the reagent.
    """
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, newPotency):
        self.__potency = newPotency

class Herb(Reagent):
    """
    Represents a herb reagent.

    Attributes:
    __grimy (bool): Indicator if the herb is grimy or not.
    """
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__potency = potency  

        self.__grimy = True

    def refine(self):
        self.setGrimy()
        self.__potency = self.__potency * 2.5
        print(f"The herb is not grimy and its potency is multiplied by 2.5")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self):
        self.__grimy = False

class Catalyst(Reagent):
    """
    Represents a catalyst reagent.

    Attributes:
    __quality (float): Quality value of the catalyst.
    """
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"As quality of catalyst is less than 8.9. So, quality is increased by 1.1")
        else:
            self.__quality = 10
            print(f"{self.__quality} it cannot be refined any further.")

    def getQuality(self):
        return self.__quality

