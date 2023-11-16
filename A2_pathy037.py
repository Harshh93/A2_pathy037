'''
File: A2_pathy037.py
Description: This file has the main code of the assignment.
Author: Harsh Manishkumar Patel
StudentID: 110403785
EmailID: pathy037@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

rom abc import ABC, abstractmethod

class Alchemist:
    def _init_(self, attack, strength, defense, magic, ranged, necromancy):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory(self)
        self.__recipes = {}