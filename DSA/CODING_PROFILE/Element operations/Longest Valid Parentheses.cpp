/**Approach
Initialize variables:

n is set to the length of the input string s.
Create an empty stack of integers named st. This stack will be used to store the indices of opening parentheses '('.
Loop through each character in the input string s using a for loop.

Inside the loop, check if the current character is a closing parenthesis ')' (i.e., s[i] == ')').

a. If it's a closing parenthesis and the stack st is not empty, it means there is a matching opening parenthesis '(' for the current closing parenthesis.

b. Pop the top index j from the stack st, indicating that the opening parenthesis '(' at index j matches the closing parenthesis ')' at index i.

c. Replace both the opening and closing parentheses with underscores ('_') in the string s to mark them as valid and ignore them in subsequent calculations.

If the current character is an opening parenthesis '(' (i.e., s[i] == '('), push its index i onto the stack st to keep track of unmatched opening parentheses.

After processing the entire string s, all valid parentheses pairs should be marked with underscores ('_') in the string.

Initialize a variable ans to 0. This variable will store the length of the longest valid parentheses substring.

Iterate through the modified string s using a for loop.

When you encounter an underscore ('_'), it indicates a valid parentheses pair. Start counting consecutive underscores to determine the length of this valid parentheses substring.

a. Increment a counter variable ct by 1 for the current underscore.

b. Use a while loop to count consecutive underscores by incrementing ct until a non-underscore character is encountered.

c. After counting the consecutive underscores, update the loop variable i to the position after the last underscore.

d. Update the ans variable by taking the maximum of its current value and the value of ct. This keeps track of the longest valid parentheses substring encountered so far.

After processing the entire modified string s, the ans variable will contain the length of the longest valid parentheses substring.

Return the ans as the result.

Complexity
Time complexity:
O(2*n) -> O(n)

Space complexity:
O(n)**/


class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
    stack<int> st;
    for(int i=0;i<n;i++)
    {
        if(s[i] == ')')
        {
            if(st.empty()==0)
            {
                int j = st.top();
                st.pop();
                s[i] = '_';
                s[j] = '_';
            }
        }
        if(s[i] == '(')
        {
            st.push(i);
        }
    }
    int ans = 0;
    for(int i=0;i<n;i++)
    {
        if(s[i] == '_')
        {
            int ct=1;
            i++;
            while(s[i] == '_')
            {
                ct++;
                i++;
            }
            i--;
            ans = max(ans,ct);
        }
    }
    return ans;
    }
};
