__author__ = 'rohanmathure'

'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java or C# and as an array of arrays in other languages.

Example:

I = [12, 15]
result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Note: It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
'''

import unittest

def getPrimeFactors(num):
    primeSet=set()
    cnt=2
    if num==1:
        return primeSet.add(1)
    while abs(num)>1:
        if num%cnt==0:
            primeSet.add(cnt)
            num/=cnt
        else:
            cnt+=1
    return primeSet

def sum_for_list(lst):
    finalSet=set()
    for i in lst:
        finalSet=finalSet.union(getPrimeFactors(i))
    finalSet=sorted(finalSet)
    retArray=[]
    for i in finalSet:
        num=0
        for j in lst:
            if j%i==0:
                num+=j
        retArray.append([i,num])
    return retArray


class TestSumByFactors(unittest.TestCase):
    def testSumForList(self):
        a = [12, 15]
        self.assertEqual(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])
