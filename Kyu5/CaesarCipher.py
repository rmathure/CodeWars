__author__ = 'rohanmathure'

import unittest
import math
import math
def moving_shift(s, shift):
    retStr=str()
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] == s[i].upper():
                num=65+(ord(s[i])+shift-65)%26
                retStr=retStr+chr(num)
            else:
                num=97+(ord(s[i])+shift-97)%26
                retStr=retStr+chr(num)
        else:
            retStr=retStr+s[i]
        shift+=1
    splitNum=int(math.ceil(len(retStr)/5))
    if not len(retStr)%5==0:
        splitNum+=1
    return [retStr[i:i + splitNum] for i in range(0, len(retStr), splitNum)]

def demoving_shift(s, shift):
    s=''.join(s)
    retStr=str()
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] == s[i].upper():
                num=65+(ord(s[i])-shift-65)%26
                retStr=retStr+chr(num)
            else:
                num=97+(ord(s[i])-shift-97)%26
                retStr=retStr+chr(num)
        else:
            retStr=retStr+s[i]
        shift+=1
    return retStr

class TestCaesar(unittest.TestCase):
    def testCaesar(self):
        self.assertEqual(
        moving_shift("I should have known that you would have a perfect answer for me!!!", 1),
        ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"])
        self.assertEqual(
            demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"],1),
                         "I should have known that you would have a perfect answer for me!!!")