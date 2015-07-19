__author__ = 'rohanmathure'

import unittest

'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
'''




def snail(snailArray,retArray=list()):
    if len(snailArray)==0:
        return retArray
    for i in range(len(snailArray[0])-1):#traverse horizontal
        retArray.append(snailArray[0][i])
        snailArray[0][i]=None
    for i in range(len(snailArray)-1): #traverse last column
        retArray.append(snailArray[i][len(snailArray[i])-1])
        snailArray[i][len(snailArray[i])-1]=None
    for i in range(len(snailArray[len(snailArray)-1]))[::-1]: #Traverse last row in reverse
        retArray.append(snailArray[len(snailArray)-1][i])
        snailArray[len(snailArray)-1][i]=None
    for i in range(1,len(snailArray)-1)[::-1]:#traverse first column in reverse
        retArray.append(snailArray[i][0])
        snailArray[i][0]=None
    for i in range(len(snailArray)):
        snailArray[i]=[x for x in snailArray[i] if x is not None]
    snailArray=[x for x in snailArray if len(x)!=0]
    return snail(snailArray,retArray)


class TestSnailSort(unittest.TestCase):
    def testSnailSort(self):
        array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array,[]), expected)


        array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(snail(array,[]), expected)

