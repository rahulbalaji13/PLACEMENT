/**
3341. Find Minimum Time to Reach Last Room I

There is a dungeon with n x m rooms arranged as a grid.
You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 3

Constraints:
2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109
**/

//DIJKSTRA ALGORITHM APPROACH 

class State //State class created for providing state space to store subsequent action like direction and time values 
{
     int i;
     int j;
     int time;
     
     public State(int i, int j, int time)
     {
         this.i = i;
         this.j = j;
         this.time = time;
     }
}

class Solution 
{
    public int minTimeToReach(int[][] moveTime) 
    {
         int m = moveTime.length;
         int n = moveTime[0].length;

         int[][] direction = {{1,0},{-1,0},{0,1},{0,-1}}; //Direction cell that moves down, up, right, left
        
         int distance[][] = new int[m][n];  // Declare new distance array
         boolean visited[][] = new boolean[m][n];

         PriorityQueue<State> pq = new PriorityQueue<State>((a,b) -> a.time - b.time); //Priority queue is declared for the state class created above and lambda expersion used to make condition for state like (a,b) = a.time - b.time

         for(int i = 0; i < m; i++)
           
         Arrays.fill(distance[i] , Integer.MAX_VALUE); //Intially fill the distance with the maximum value in integer as we initialize to infinity before traversal

         distance[0][0] = 0; //Initialize the distance to 0
         pq.offer(new State(0,0,0));  //Append with initial state 

         while(!pq.isEmpty()) //When this while loop ends entire traversal is over 
         {
             State temp = pq.poll();  //Remove the current maximum(lowest element) from the priority queue and then assign to state variable

             if(visited[temp.i][temp.j])
               
                 continue;

             visited[temp.i][temp.j] = true; //Mark the room visited 

             for(int d[] : direction)
             {
                 int x = temp.i + d[0]; //Initialize cell pointer with combination of state and direction at 0
                 int y = temp.j + d[1]; //Intilaize cell pointer with combination of state and direction at 1

                 if(x < 0 || y < 0 || x >= m || y >= n)  //Compare the all available cells

                     continue;

                 var time_value = Math.max(distance[temp.i][temp.j] , moveTime[x][y]) + 1; //Find max of current diatance and moving time then add 1. SO 4+1=5

                 if(distance[x][y] > time_value) 
                 {
                     distance[x][y] = time_value; //Assign time value for distance and this case 5 is the time value for given first test case

                     pq.offer(new State(x,y,time_value)); //Create new state
                 }
             }
         }
         return distance[m - 1][n - 1]; //This returns the last distance value calculated in between rooms and output is 6
    }
}

// TIME COMPLEXITY = O(M * N)
