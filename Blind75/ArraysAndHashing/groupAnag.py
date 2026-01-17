class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
    
        for i in strs:
            key = "".join(sorted(i))
            ans[key].append(i)

        return ans.values() 
