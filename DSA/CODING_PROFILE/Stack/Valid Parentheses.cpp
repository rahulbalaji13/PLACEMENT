/**1)For opening bracket we need to push the bracket in the stack 
   2)For closing the bracket:
        i)We chech whether the stack is empty or not
        ii)For closing bracket we need to find corresponding openning bracket from the stack 
           If found we pop it out
  3)If my stack is empty after performing oprations then my input string is valid beacuse for each opening bracket we have corresponding closing bracket**/




class Solution {
public:
    bool isValid(string s) {
        stack <char> str;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                str.push(s[i]);
            }
            else{
                if(!str.empty()){
                    if(s[i]==')' && str.top()=='(')
                       str.pop();
                    else if(s[i]=='}' && str.top()=='{')
                        str.pop();
                        else if(s[i]==']' && str.top()=='[')
                          str.pop();
                        else 
                           return false;
                }
                   else return false;
                }
            }
            if(str.empty())
               return true;
            else 
            return false;     
        }
        
    
};
