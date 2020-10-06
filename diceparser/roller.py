#!usr/bin/python
# -*- coding:utf-8 -*-

# importing randrange for rolling within a certain range
from random import randrange

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


# initiationroll rolls for initiative, taking initiation as a param
def initiationroll(inimod):
    return randrange(1, 20) + inimod


# attackroll rolls for hit/miss, taking ability modifier, and proficiency
# as parameters.
def attackroll(abimod, prof):
    return randrange(1, 20) + abimod + prof


# damageroll rolls for damage inflicted,
# takes weapon damage and ability modifier as parameters
def damageroll(weapondmg, abimod):
    return randrange(1, weapondmg) + abimod


# Rolling a number
class Roller:
    def __init__(self):
        self.iniroll = initiationroll(3)
        self.atkroll = attackroll(3, 2)
        self.dmgroll = damageroll(5, 3)

    def getiniroll(self):
        return self.iniroll

    def getatkroll(self):
        return self.atkroll

    def getdmgroll(self):
        return self.dmgroll


if __name__ == "__main__":
    roller = Roller()
