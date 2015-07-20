__author__ = 'rohanmathure'

import unittest

'''
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!
'''
keyMap={'1':['1','2','4'],'2':['1','2','3','5'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8'],'6':['3','6','5','9'],'7':['4','7','8'],'8':['5','7','8','9','0'],'9':['6','8','9'],'0':['8','0']}

def combine(list1,list2):
    if len(list1)==0:
        return list2
    elif len(list2)==0:
        return list1
    else:
        return [i+j for i in list1 for j in list2]

def getAdjacent(str):
    return keyMap[str]

def get_pins(observed):
    retArray=list()
    for i in observed:
        retArray=combine(retArray,getAdjacent(i))
    return retArray






class TestObservedPIN(unittest.TestCase):
    def testObservedPIN(self):
        expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

        for tup in expectations:
          self.assertEqual(sorted(get_pins(tup[0])), sorted(tup[1]))