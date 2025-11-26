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











    













































