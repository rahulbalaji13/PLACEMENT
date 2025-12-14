"""
OPTIMAL BINARY SEARCH TREE
Problem Statement
Write a program to implement an optimal binary search tree using dynamic programming.
Given a sorted array key [0... n-1] and an array freq [0... n-1] of frequency counts, where freq [i] is the number of searches for key [i], Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.
Note: Cost of a BST node: level of that node * frequency. The level of the root is 1.

Input format :
The first line of the input is the value of n.

The second line of input is the keys separated by a single space.

The last line of input is the frequency separated by a single space.

Output format :
The output prints the cost of the optimal binary search tree.

Code constraints :
1 ≤ n ≤ 100

1 ≤ keys[i] ≤ 104(Keys are unique and given in sorted order)

1 ≤ freq[i] ≤ 103(Frequency values are positive)

Sample test cases :
Input 1 :
3
10 12 20
34 8 50
Output 1 :
Cost of Optimal BST is 142
Input 2 :
5
15 18 20 25 28
30 12 5 10 8
Output 2 :
Cost of Optimal BST is 130
"""

def optimalBS(keys, freq):
    n = len(keys)
    
    cost = [[0] * n for _ in range(n)]
    
    sumFreq = [[0] * n for _ in range(n)]
    
    # Precompute freq sums
    for i in range(n):
        sumFreq[i][i] = freq[i]
        for j in range(i + 1, n):
            sumFreq[i][j] = sumFreq[i][j - 1] + freq[j]
    
    for i in range(n):
        cost[i][i] = freq[i]
        
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                
                leftCost = cost[i][r - 1] if r > i else 0
                rightCost = cost[r + 1][j] if r < j else 0
                
                currentCost = leftCost + rightCost + sumFreq[i][j]
                
                if currentCost < cost[i][j]:
                    cost[i][j] = currentCost
            
    return cost[0][n - 1]
    
def main():
    n = int(input().strip())
    keys = list(map(int, input().split()))
    freq = list(map(int, input().split()))
    
    result = optimalBS(keys, freq)
    print(f"Cost of Optimal BST is {result}")
    
if __name__ == "__main__":
    main()
