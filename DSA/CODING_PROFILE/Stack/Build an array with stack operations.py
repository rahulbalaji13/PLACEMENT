class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        curr=1
        for num in target:
            while curr<num:
                #while the current number is less than the target number
                #push the current number and generate the "push"operation
                res.extend(["Push","Pop"]) 
                curr+=1
                 #The current number matches the target number, so push it
            res.append("Push")
            curr+=1
        return res


