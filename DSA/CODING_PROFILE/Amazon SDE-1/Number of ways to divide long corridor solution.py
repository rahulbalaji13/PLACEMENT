#IntuitionTo divide the corridor into non-overlapping sections with exactly two seats and any number of plants in between, we need to identify the positions where dividers can be installed. The problem constrains the installation of dividers such that each position between indices i-1 and i (1 <= i <= n - 1) can have at most one divider.
#Approach
#Initialize variables to keep track of chairs, result, and iterate through the corridor.
#When a seat ('S') is encountered, count it, skip any plants ('P') until the next seat is found, and count that seat as well.
#After identifying adjacent pairs of seats, count the divisions between them and consider each plant as an additional division.
#If there are extra divisions (more than one) and more characters in the corridor, update the result accordingly.
#Repeat the process until the end of the corridor is reached.
#Check if there are chairs and an even number of chairs, then return the final result; otherwise, return 0.
#Complexity
#The time complexity is O(n), where n is the length of the corridor, as we iterate through the corridor once.
#The space complexity is O(1), as we use a constant amount of space for variables.
#https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/solutions/4337254/beats-100-explained-with-video-coming-soon-interview-solution-visualized-too/?envType=daily-question&envId=2023-11-28







class Solution:
    def numberOfWays(self, corridor: str) -> int:
        numSeats=0
        numPlants=0
        dividers=1
        mod=1000000007

        for i in corridor:
            if i=='S':
                numSeats+=1
            
            if numSeats==2 and i=='P':
                numPlants+=1

            if numSeats==3:
                dividers*=(numPlants+1)
                dividers%=mod
                numSeats=1
                numPlants=0

        if numSeats<2:
            return 0

        return dividers






