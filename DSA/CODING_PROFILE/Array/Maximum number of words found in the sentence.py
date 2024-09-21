class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        ans=0
        for i in range(len(s)):
          s[i]=s[i].count(' ')+1
          ans=max(ans,s[i])
        return ans
