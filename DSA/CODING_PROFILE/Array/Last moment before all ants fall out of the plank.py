#The abs() function in Python returns the absolute value of a number. The absolute value of a number is its distance from zero, regardless of whether the number is positive or negative.

class Solution(object):
    def getLastMoment(self, n, left, right):
        ans=0
        
        for i in left:
            ans=max(ans,abs(0-i))

        for i in right:
            ans=max(ans,abs(n-i))
        
        return ans
        
