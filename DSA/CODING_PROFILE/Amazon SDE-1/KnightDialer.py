class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD=10**9+7

        moves={0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}

        dp=dict()

        for i in range(10):
            dp[(1,i)]=1

        for m in range(2,n+1):
            for currDigit in range(10):
                dp[(m,currDigit)]=sum([dp[(m-1,nextDigit)] for nextDigit in moves[currDigit]])%MOD

        return sum([dp[(n,i)] for i in range(10)])%MOD
