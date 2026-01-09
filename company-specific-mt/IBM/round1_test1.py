"""
Problem Statement
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
Example 2:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
Input format :
The first line of input consists of a string s, representing the input string.
The second line consists of an integer n, indicating the number of words in the dictionary.
The next line consists of n space-separated strings representing the words of the dictionary.
Output format :
If the input string can be segmented into words from the dictionary, output "true".
If the input string cannot be segmented into words from the dictionary, output "false".
Refer to the sample output for the formatting specifications.
Code constraints :
1 ≤ s.length ≤ 100
1 ≤ wordDict.length ≤ 10
1 ≤ wordDict[i].length ≤ 100
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Sample test cases :
Input 1 :
applepenapple
2
apple pen
Output 1 :
true
Input 2 :
catsandog
5
cats dog sand and cat
"""
s = str(input().strip())
n = int(input())
word = input().strip().split() 
word_set = set(word)

m = len(s)

dp = [False] * (m + 1) 
dp[0] = True

for i in range(1, m + 1):
    for j in range(i):
        if dp[j] and s[j:i] in word_set:
            dp[i] = True
            break

if dp[m]:
    print("true") 
else:
    print("false")

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

Example 1:

Input: s = "Hello World"

Output: 

5

World

Explanation: The last word is "World" with length 5.          

Example 2:

Input: s = "luffy is still joyboy"

Output: 

6

joyboy

Explanation: The last word is "joyboy" with length 6.

Input format :
The input consists of a string s.

Output format :
The first line of output prints the length of the last word in the string.

The second line prints the last word in the string.

Refer to the sample output for the formatting specifications.

Code constraints :
1 ≤ s.length ≤ 100

s consists of only English letters and spaces ' '.

There will be at least one word in s.

Sample test cases :
Input 1 :
Hello World
Output 1 :
5
World
Input 2 :
luffy is still joyboy
Output 2 :
6
joyboy
"""

s = input().strip().split()

last = s[-1]
print(len(last))
print(last)
