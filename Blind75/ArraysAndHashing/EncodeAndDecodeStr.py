"""
ENCODING AND DECODING THE STRINGS

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = " "
        for s in strs:
          res += len(strs) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
              j = i
              while s[j] != '#':
                    j += 1
              length = int(s[i : j)
              j = j + 1
              j = i + length
              res.append(s[i : j])
              i = j

        return res


"""
Intuition
Instead of storing all string lengths first and then appending the strings, we can directly attach each string to its length.
For every string, we write length#string.
The # character acts as a clear boundary between the length and the actual content, and using the length ensures we know exactly how many characters to read—no matter what characters appear in the string itself.
During decoding, we simply read characters until we reach # to find the length, then extract exactly that many characters as the string.
This approach is both simpler and more efficient because it avoids building separate sections for lengths and content.

Algorithm

Encoding

Initialize an empty result string.
For each string in the list:
Compute its length.
Append "length#string" to the result.
Return the final encoded string.

Decoding

Initialize an empty list for the decoded strings and a pointer i = 0.
While i is within the bounds of the encoded string:
Move a pointer j forward until it finds '#' — this segment represents the length.
Convert the substring s[i:j] into an integer length.
Move i to the character right after '#'.
Extract the next length characters — this is the original string.
Append the extracted string to the result list.
Move i forward by length to continue decoding the next segment.
Return the list of decoded strings.

"""

















      









