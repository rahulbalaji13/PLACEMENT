# 1. Reverse a string
s = input()
print(s[:-1])

#2. Find largest in Array 
a = list(map(int, input().split()))
print(a)

#3. Check if string is palindrome
s = input()
print("Yes, it is palindrome" if s == s[::-1] else "NO")

# 4. print all even numbers from Array
arr = list(map(int, input().split()))
for num in arr:
    if num % 2 == 0:
        print(num, end = ' ')

# 5. Frequency of Character in String
s = input()
frequency = {} 
for c in s:
    frequency[c] = frequency.get(c, 0) + 1

for key, value in frequency.items():
    print(f"{key}:{value}")

#6. First Non-Repeating Character
s = input()
from collections import Counter
count = Counter(s)
for c in s:
    if count[c] == 1:
        print(c)
        break

# 7. Sort array and Print
arr = list(map(int, input().split()))
arr.sort()
print(' '.join(map(str, arr)))

# 8. Remove duplicates from the Array -> HINT: Use set(arr)
arr = list(map(int, input().split()))
print(' '.join(map(str, set(arr))))

#9. Print diamond Pattern (n =  size)
n = int(input())
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for j in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

#10. Sum of digits in Number
number = input()
print(sum(int(d) for d in number))

#11. Regular expression - extract the user id, domain name, and suffix from the following email addresses
import re
import sys

s = sys.stdin.read().strip()

pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, s)

for u, d, suf in matches:
    print(u, d, suf)

#12. NumPy Module - extract all odd number array using numpy array
import numpy as np

n = list(map(int, input().strip().split()))

arr = np.array(n)

odd_arr = arr[arr % 2 != 0]

print(odd_arr)

#13. to get the common unique items between two arrays sorted in ascending order using NumPy function.
import numpy as np

nums1 = list(map(int, input().strip().split()))
nums2 = list(map(int, input().strip().split()))

arr1 = np.array(nums1)
arr2 = np.array(nums2)

unique = np.intersect1d(arr1, arr2)

print(unique)

#15.  find the sum of digits of a number - Ex: I/P: 12345 so, O/P: 15
def sumOfDigits(num):
    sum = 0
    while num!=0:
        digit = int(num%10)
        sum += digit
        num = num/10
    return sum;

num = int(input())
print(sumOfDigits(num))

#16. Write a program to get the last part of a string before a specified character. Note: Specified characters are "/" and "-"
s = input().strip()
if "/" in s:
    print(s.rsplit("/", 1)[0])
else:
    print(s)
if "-" in s:
    print(s.rsplit("-", 1)[0])
else:
    print(s)

# 17. Find maximum sum from list
n=int(input())
arr=[int(i) for i in input().split()][:n]
add=0
for i in range(0,n,2):
    if arr[i]<arr[i+1]:
        add+=arr[i]
    else:
        add+=arr[i+1]
print(add)

#18. Given a list of numbers in python List. Write a Python program to create a list of tuples having the first element as the number and the second element as the cube of the number.

inp = input().split()
for i in range(0,len(inp)):
    inp[i] = int(inp[i])

res = [(val, pow(val, 3)) for val in inp]
print(res)




















    













































