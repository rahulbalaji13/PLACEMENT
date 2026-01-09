"""
Problem Statement

A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced by the sum of squares of its digit, that is, if we start with a happy number and keep replacing it with digits square sums, we reach 1. 

Examples 

Input: n = 19

Output: 19 is Happy Number

Explanation:

1^2 + 9^2 = 82

8^2 + 2^2 = 68

6^2 + 8^2 = 100

1^2 + 0^2 + 0^2 = 1

As we reach 1, 19 is a Happy Number.

Input: n = 20

Output: 20 is not a Happy number

Input format :
The input is an integer value of n.

Output format :
The output displays an integer, representing if the input integer is a happy number or not.

Refer to the sample output for the formatting specifications.

Code constraints :
The given test cases fall under the following constraints:

1 <= n <= 1005

Sample test cases :
Input 1 :
19
Output 1 :
19 is a Happy number
Input 2 :
20
Output 2 :
20 is not a Happy number
"""

n = int(input())

def happy_number(x):
    s = 0
    while x > 0:
        d = x % 10
        s += d * d
        x //= 10
    return s
    
seen = set()
num = n # Create copy in num

while num != 1 and num not in seen:
    seen.add(num)
    num = happy_number(num)

if num == 1:
    print(n , "is a Happy number")
else:
    print(n, "is not a Happy number")

"""
Problem Statement



Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.



A subarray is a contiguous part of an array.



Example 1



Input: 

6

4 5 0 -2 -3 1

5



Output: 

7



Explanation:

There are 7 subarrays with a sum divisible by k = 5:

[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]



Example 2



Input:

1

5

9

Output:

0

Explanation:

The sum of elements from 1st position to 5th position is 15.

Input format :
The first line contains a single integer n, representing the size of the array nums.

The second line contains n space-separated integers arr[i], representing the elements of the array nums.

The third line contains a single integer k, representing the divisor.

Output format :
The output displays a single integer representing the number of subarrays in nums whose sum is divisible by k.

Refer to the sample output for the formatting specifications.

Code constraints :
1 ≤ n ≤ 10

1 ≤ arr[i] ≤100

1 ≤ k ≤ 1000

Sample test cases :
Input 1 :
6
4 5 0 -2 -3 1
5
Output 1 :
7
Input 2 :
1
5
9
Output 2 :
0"""

n = int(input().strip())
arr = list(map(int, input().strip().split()))
k = int(input().strip())

# Frequency count of prefix-sum remainders
rem_cnt = [0] * k
rem_cnt[0] = 1  # empty prefix has remainder 0

prefix_sum = 0
ans = 0

for x in arr:
    prefix_sum += x  # runns sum of array so every step represents the sum of a prefix ending at current element
    r = prefix_sum % k # For handling remainders 
    r = (r + k) % k
    ans += rem_cnt[r]
    rem_cnt[r] += 1 # To handle remainders

print(ans)
