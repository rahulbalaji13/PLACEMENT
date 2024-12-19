/*
Reverse vowels of a string 
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
*/

class Solution 
{
    public String reverseVowels(String s) 
    {
         char ch;
         String rev = "";
         for(int i = 0; i < s.length(); i++)
         {
             ch = s.charAt(i);

             if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o'|| ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O'|| ch =='U')    
            {
                 rev = ch + rev;           
            }
         }
         String result = "";
         for(int i = 0, count = 0; i < s.length(); i++)
         {
             ch = s.charAt(i);
             
             if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o'|| ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O'|| ch =='U')
             {
                 result = result + rev.charAt(count++);
             }  
             else
             {
                 result += ch;
             }
         }
         return result;
    }
}

/* TC = O(N) & SC = O(N) */
