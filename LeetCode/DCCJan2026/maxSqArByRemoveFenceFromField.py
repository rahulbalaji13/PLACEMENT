class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = (10 ** 9) + 7

        # Add borders and sort 
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        # Compute all possible horizontal
        h_gaps = set()

        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                gap = h[j] - h[i]
                h_gaps.add(gap)

        # Compute all possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                gap = v[j] - v[i]
                v_gaps.add(gap)

        # Find common gaps
        common = h_gaps & v_gaps # Set intersection
 
        if not common:
            return -1

        side = max(common)

        return (side * side) % MOD
        

        
