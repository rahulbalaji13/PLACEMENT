/**
3335. Total Characters in String After Transformations I
Solved
Medium
Topics
Companies
Hint
You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105

**/

class Solution {
    private static final int mod = 1000000007;
    private int mod_add(int a, int b) {
        a %= mod; b %= mod;
        return ((a + b) % mod + mod) % mod;
    }
    public int lengthAfterTransformations(String s, int t) {
        int[] nums = new int[26];
        for (char ch : s.toCharArray()) nums[ch - 'a']++;
        while (t-- > 0) {
            int[] cur = new int[26];
            for (int j = 0; j < 26; j++) {
                if (j == 25 && nums[j] > 0) {
                    cur[0] = mod_add(cur[0], nums[j]);
                    cur[1] = mod_add(cur[1], nums[j]);
                } else {
                    if (j < 25) cur[j + 1] = mod_add(cur[j + 1], nums[j]);
                }
            }
            nums = cur;
        }
        int ans = 0;
        for (int i : nums) ans = mod_add(ans, i);
        return ans;
    }
}
