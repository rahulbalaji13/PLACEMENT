class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]

        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = ['inf'] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)] # Distance, Node

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            if visited[x]:
                continue

            visited[x] = True

            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))


        return -1
        
