#!usr/bin/python
#-*- coding:utf-8 -*-

# importing randrange for rolling within a certain range
from random import randrange


# Rolling a number
class Roller:
    # initiationroll rolls for initiative, taking initiation as a param
    def initiationroll(self, inimod):
        return randrange(1, 20) + inimod

    # attackroll rolls for hit/miss, taking ability modifier, and proficiency
    # as parameters.
    def attackroll(self, abimod, prof):
        return randrange(1, 20) + abimod + prof

    # damageroll rolls for damage inflicted,
    # takes weapon damage and ability modifier as parameters
    def damageroll(self, weapondmg, abimod):
        return randrange(1, weapondmg) + abimod


if __name__ == "__main__":
    roller = Roller()
    print("Initiation roll : ", roller.initiationroll(3))
    print("Attack roll : ", roller.attackroll(3, 2))
    print("Damage roll : ", roller.damageroll(5, 3))
