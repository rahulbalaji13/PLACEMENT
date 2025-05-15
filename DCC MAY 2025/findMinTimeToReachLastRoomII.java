/**

3342. Find Minimum Time to Reach Last Room II
Solved
Medium
Topics
Companies
Hint
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 4

 

Constraints:

2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
0 <= moveTime[i][j] <= 109
  **/

class Solution {
    public int minTimeToReach(int[][] t) {
        int n = t.length, m = t[0].length;
        int[][][] dp = new int[n][m][2];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        dp[0][0][0] = 0;
        pq.offer(new int[]{0, 0, 0, 0});

        int[][] dir = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int time = curr[0], x = curr[1], y = curr[2], parity = curr[3];

            if (dp[x][y][parity] < time) continue;

            for (int[] d : dir) {
                int nx = x + d[0], ny = y + d[1];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                int waitTime = Math.max(time, t[nx][ny]);
                int nextParity = 1 - parity;
                int nextTime = waitTime + 1 + parity;

                if (nx == n - 1 && ny == m - 1)
                    return nextTime;

                if (nextTime < dp[nx][ny][nextParity]) {
                    dp[nx][ny][nextParity] = nextTime;
                    pq.offer(new int[]{nextTime, nx, ny, nextParity});
                }
            }
        }

        return -1;
    }
}
