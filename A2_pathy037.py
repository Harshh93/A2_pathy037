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
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mix_potion(self, name, type, stat,  primaryingredient, secondaryingredient):
        if (primaryingredient in self.__herbs or primaryingredient in self.__catalysts)  and (secondaryingredient in self.__catalysts or secondaryingredient in self.__potions):
            # Mix potion based on the recipe
            if secondaryingredient in self.__potions:
                # Create an super potion
                super_potion = next(p for p in self.__potions if p.name == secondaryingredient)
                if type == "Super":
                    # Super potion formula: potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5
                    boost_value = primaryingredient.potency + (secondaryingredient.potency * secondaryingredient.quality) * 1.5
                    new_potion = SuperPotion(name, stat, round(boost_value, 2), primaryingredient, primaryingredient)
                elif type == "Extreme":
                    # Extreme potion formula: (potency of its reagent * boost value of its super potion) * 3.0
                    boost_value = (primaryingredient.potency * super_potion.boost) * 3.0
                    new_potion = ExtremePotion(name, stat, round(boost_value, 2), primaryingredient, super_potion)
                else:
                    print(f"Invalid potion type: {type}")
                    return
            else:
                # Create a super potion
                boost_value = (primaryingredient.potency + (secondaryingredient.potency * secondaryingredient.quality)) * 1.5
                new_potion = SuperPotion(name, stat, round(boost_value, 2), primaryingredient, secondaryingredient)

            self.__potions.append(new_potion)
        else:
            print(f"Missing ingredients for {name}.")
    def add_reagent(self, reagent,amount=1):
        if isinstance(reagent, Herb):
            # Add herb to the laboratory
            self.__herbs.extend([reagent]*amount)
        elif isinstance(reagent, Catalyst):
            # Add catalyst to the laboratory
            self.__catalysts.extend([reagent]*amount)

    


class Alchemist:
    def __init__(self):
        self.__attack = 0
        self.__strength = 0
        self.__defence = 0
        self.__magic = 0
        self.__range = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory()
        self.__recipes = {"Super Attack":("Irit", " Eye of Newt"), "Super Strength": ("Kwuarm", "Limpwurt Root"), "Super Defence": ("Cadantine", "White Berries"), "Super Magic": ("Lantadyme", "Potato Cactus"), "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"), "Super Necromancy": ("Arbuck", "Blood of Orcus"),"Extreme Attack": ("Avantoe", "Super Attack"), "Extreme Strength": ("Dwarf Weed", "Super Strength"),"Extreme Defence": ("Lantadyme", "Super Defence"), "Extreme Magic": ("Ground Mud Rune", "Super Magic"), "Extreme Ranging": ("Grenwall Spike", "Super Ranging"), "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy")}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mix_potion(self, potion_name):
        recipe = self.__recipes.get(potion_name)
        if recipe:
            primaryIngridient = next((herb for herb in self.__laboratory.herbs if herb.name == recipe["primary"]), None)
            secondaryIngridient = next((catalyst for catalyst in self.__laboratory.catalysts if catalyst.name == recipe["ingredient2"]), None)

            if primaryIngridient and secondaryIngridient:
                self.__laboratory.mix_potion(primaryIngridient, secondaryIngridient, potion_name, self.__recipes[potion_name]["stat_attribute"], recipe["type"])
                print(f"Successfully mixed {potion_name}.")
            else:
                print(f"Missing ingredients for {potion_name}.")
        else:
            print(f"No recipe found for {potion_name}.")
    def drink_potion(self, potion):
        if potion.__stat == "attack":
            self.__attack += potion.__boost
        elif potion.__stat == "strength":
            self.__strength += potion.__boost
        elif potion.__stat == "defence":
            self.__defence += potion.__boost
        elif potion.__stat == "magic":
            self.__magic += potion.__boost
        elif potion.__stat == "range":
            self.__range += potion.__boost
        elif potion.__stat == "necromancy":
            self.__necromancy += potion.__boost
        return potion.__stat

    def collect_reagent(self, reagent,amount=1):
        self.__laboratory.add_reagent(reagent,amount)

    def refine_reagents(self):
        for herb in self.__laboratory.herbs:
            herb.refine()

        for catalyst in self.__laboratory.catalysts:
            catalyst.refine()




# class Potion
class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
        
    @abstractmethod
    def calculateBoost(self):
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
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.setBoost(round(self.__herb.getPotency() + (self.__catalyst.getPotency() * self.__catalyst.getQuality()) * 1.5 ,2))

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst

class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name , stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        self.setBoost(round((self.__reagent.getPotency() * self.__potion.getBoost())* 3.0, 2))

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion

class Reagent(ABC):
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
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        self.setGrimy()
        self.__potency = self.__potency * 2.5
        print(f"the herb is not grimy and its potency is multiplyed by 2.5")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self):
        self.__grimy = False

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"As quality of catalyst is less then 8.9. So, quality is increased by 1.1")
        else:
            self.__quality = 10
            print(f"{self.__quality} it cannot be refined any further.")

    def getQuality(self):
        return self.__quality