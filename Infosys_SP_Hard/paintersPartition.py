"""
The problem is the classic Painter’s Partition Problem: use binary search on the answer (time) plus a greedy check to find the minimum possible maximum time any painter spends, 
with each painter painting only contiguous boards.

Problem Statement
We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit time to paint 1 unit of the board. The problem is to find the minimum time to get 

this job was done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.

Write a program for the same.
Example:

Input :

4

10, 20, 30, 40

2 

Output: 60.

Here we can divide the first 3 boards for one painter and the last board for the second painter.

Input format :
The first line of the input consists of the integer value of n.

The next n integer inputs are the length of the boards.

The last input is the integer k value representing the number of painters.

Output format :
The output prints an integer, representing the minimum time required to paint all boards.
Refer to the sample output for formatting specifications.

Code constraints :
1 ≤ n ≤ 100

1 ≤ length of each board ≤ 1000

1 ≤ k ≤ n1

Sample test cases :
Input 1 :
4
10 10 10 10
2
Output 1 :
20
Input 2 :
4
10 20 30 40
2
"""
def canPaint(boards, k, limit):
    painters = 1
    current = 0
    
    for length in boards:
        if length > limit:
            return False
        
        if current + length <= limit:
            current += length
            
        else:
            
            painters += 1
            current = length
    
        if painters > k:
           return False
           
    return True
    

def minTimePaint(boards, k):
    low = max(boards)
    high = sum(boards)
    answers = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if canPaint(boards, k, mid):
            answers = mid
            high = mid - 1
            
        else:
            
            low = mid + 1
    
    return answers
    
    
def main():
    n = int(input().strip())
    boards = list(map(int, input().split()))
    k = int(input().strip())
    
    result = minTimePaint(boards, k)
    print(result)
    
if __name__ == "__main__":
    main()
