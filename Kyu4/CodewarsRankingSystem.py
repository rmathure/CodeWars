__author__ = 'rohanmathure'

'''
Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

Business Rules:

A user starts at rank -8 and can progress all the way to 8.
There is no 0 (zero) rank. The next rank after -1 is 1.
Users will complete activities. These activities also have ranks.
Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression).
A user cannot progress beyond rank 8.
The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
The progress is scored like so:

Completing an activity that is ranked the same as that of the user's will be worth 3 points
Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is 10 d d where d equals the difference in ranking between the activity and the user.
Logic Examples:

If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
Code Usage Examples:

user = User()
user.rank # => -8
user.progress # => 0
user.inc\_progress(-7)
user.progress # => 10
user.inc\_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
'''


class User:
    def __init__(self):
        self.rank=-8
        self.progress=0

    def setRank(self,newRank):
        if newRank==0:
            newRank=1
        elif newRank>=8:
            newRank=8
        self.rank=newRank

    def setProgress(self,points):
        if self.rank==8:
            return
        self.progress+=points
        if self.progress/100 >0:
            self.setRank(self.rank+(self.progress/100))
            if self.rank==8:
                self.progress=0
            else:
                self.progress%=100
        
            

    def getDifference(self,activityRank):
        cnt=0
        tempRank=min(self.rank,activityRank)
        destRank=max(self.rank,activityRank)
        if self.rank<activityRank:
            factor=1
        elif self.rank>activityRank:
            factor=-1
        else:
            return 0
        while tempRank<destRank:
            tempRank+=1
            if tempRank==0:
                tempRank+=1
            cnt+=1
        return cnt*factor

    def inc_progress(self,activityRank):
        if activityRank<-8 or activityRank>8 or activityRank==0:
            raise Exception
        if self.getDifference(activityRank)<=-2:
            pass
        elif self.getDifference(activityRank)==0:
            self.setProgress(3)
        elif self.getDifference(activityRank)==-1:
            self.setProgress(1)
        else:
            diff=self.getDifference(activityRank)
            self.setProgress(10*diff*diff)
        print [self.rank,self.progress,activityRank]


