'''
File: A2_pathy037.py
Description: This file has the testing code of the assignment.
Author: Harsh Manishkumar Patel
StudentID: 110403785
EmailID: pathy037@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''
import unittest
from A2_pathy037 import Laboratory, Alchemist, Herb, Catalyst, SuperPotion, ExtremePotion

class TestPotionMixing(unittest.TestCase):
    def setUp(self):
        self.laboratory = Laboratory()
        self.alchemist = Alchemist(
    def test_mix_valid_potion(self):
        # Create herb and catalyst instances
        arbuck = Herb("Arbuck", 2.6)
        eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

        # Collect reagents in the laboratory
        self.alchemist.collectReagent(arbuck, 5)
        self.alchemist.collectReagent(eye_of_newt, 3)

        # Mix a valid potion
        self.alchemist.mixPotion("Super Attack")
        potions = self.alchemist.getLaboratory().getPotions()

        self.assertEqual(len(potions), 1)
        self.assertIsInstance(potions[0], SuperPotion)

    def test_mix_invalid_potion(self):
        # Create herb and catalyst instances
        arbuck = Herb("Arbuck", 2.6)
        eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

        # Collect reagents in the laboratory
        self.alchemist.collectReagent(arbuck, 5)
        self.alchemist.collectReagent(eye_of_newt, 3)

        # Mix an invalid potion (missing ingredients)
        self.alchemist.mixPotion("Invalid Potion")
        potions = self.alchemist.getLaboratory().getPotions()

        self.assertEqual(len(potions), 0)

    def test_drink_potion(self):
        # Create herb and catalyst instances
        arbuck = Herb("Arbuck", 2.6)
        eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

        # Collect reagents in the laboratory
        self.alchemist.collectReagent(arbuck, 5)
        self.alchemist.collectReagent(eye_of_newt, 3)

        # Mix a potion
        self.alchemist.mixPotion("Super Attack")

        # Drink the potion
        super_attack_potion = self.alchemist.getLaboratory().getPotions()[0]
        result = self.alchemist.drinkPotion(super_attack_potion)

        self.assertEqual(result, "Attack")
        self.assertEqual(self.alchemist.getAttack(), super_attack_potion.getBoost())

    def test_refine_reagents(self):
        # Create herb and catalyst instances
        arbuck = Herb("Arbuck", 2.6)
        eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

        # Collect reagents in the laboratory
        self.alchemist.collectReagent(arbuck, 5)
        self.alchemist.collectReagent(eye_of_newt, 3)

        # Refine reagents
        self.alchemist.refineReagents()

        # Check if reagents are refined
        self.assertFalse(arbuck.getGrimy())
        self.assertEqual(arbuck.getPotency(), 2.6 * 2.5)

        self.assertEqual(eye_of_newt.getQuality(), 2.1)

if __name__ == '__main__':
    unittest.main()
