__author__ = 'rohanmathure'
import unittest

'''
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
'''


romanMap={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
tenSet=set([1,10,100,100])

def numToRoman(num):
    romanList=[]
    cnt=0
    revMap=list(romanMap.keys())
    revMap=sorted(revMap ,reverse=True)
    while True:
        found=False
        if num==0:
            return romanList
        if num/revMap[cnt] >0:
            romanList.append(romanMap[revMap[cnt]]*(num//revMap[cnt]))
            num%=revMap[cnt]
            found=True
        else:
            for i in range(cnt+1,len(revMap)):

                if num/(revMap[cnt]-revMap[i])==1 and (revMap[i] in tenSet):
                    romanList.append(romanMap[revMap[i]]+romanMap[revMap[cnt]])
                    num%=(revMap[cnt]-revMap[i])
                    found=True
                    break
        if not found:
            cnt+=1
    return romanList



def solution(n):
    return ''.join(numToRoman(n))

class TestRoman(unittest.TestCase):
    def testNumToRoman(self):
        self.assertEqual(solution(1),'I')
        self.assertEqual(solution(4),'IV')
        self.assertEqual(solution(6),'VI')
        self.assertEqual(solution(89),'LXXXIX')