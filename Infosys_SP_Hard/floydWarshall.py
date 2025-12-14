"""
Problem Statement
Write a program to find the shortest path between every pair of cities using the Floyd Warshall algorithm.

Input format :
The first line of input consists of an integer (N), representing the number of cities.

The next N*N Matrix represents the distance Between each city.

Note: The distance between one city to itself will be 0, and the distance will be 999 if there is no direct edge between the two cities.

Output format :
The output prints the shortest travel distance between each pair of cities.

If there is no possible path between two cities, output INF instead of the distance.
Refer to the sample output for formatting specifications.

Code constraints :
1 ≤ N ≤ 100

0 ≤ distance ≤ 999

The diagonal elements (distance from a city to itself) will always be 0.

Sample test cases :
Input 1 :
4
0 5 999 10
999 0 3 999
999 999 0 1
999 999 999 0
Output 1 :
0 5 8 9 
INF 0 3 4 
INF INF 0 1 
INF INF INF 0 
Input 2 :
3
0 5 999
1 0 2
1 3 0
Output 2 :
0 5 7 
1 0 2 
1 3 0 
"""

INF = 999

def floydWarshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
            
def main():
    n = int(input().strip())
    dist = []
    for _ in range(n):
        row = list(map(int, input().split()))
        dist.append(row)
        
    floydWarshall(dist, n)
    
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end = " ")
            else:
                print(dist[i][j], end = " ")
                
        print()
        
if __name__ == "__main__":
    main()
