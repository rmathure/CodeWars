__author__ = 'rohanmathure'
'''
our task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
'''

import unittest

def format_duration(seconds):
    if seconds==0:
        return "now"
    nums=[0,0,0,0,0]
    units=['year','day','hour','minute','second']
    nums[0]=seconds//(60*60*24*365)
    seconds%=(60*60*24*365)
    nums[1]=seconds//(60*60*24)
    seconds%=(60*60*24)
    nums[2]=seconds//(60*60)
    seconds%=(60*60)
    nums[3]=seconds//60
    seconds%=60
    nums[4]=seconds
    zipArray = [x for x in zip(nums, units) if x[0] != 0]
    zipArray=map(list,zipArray)
    for x in zipArray:
        if x[0] > 1:
            x[1] += 's'
    zipArray=[str(x[0])+" "+x[1] for x in zipArray]
    retStr=", ".join(zipArray[:-1])
    if len(retStr)>0:
        retStr+=" and "+zipArray[-1]
    else:
        retStr=zipArray[-1]
    return retStr

class TestDuration(unittest.TestCase):
    def testDuration(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
