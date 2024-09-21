/**Lambda function in C++ approach

https://www.geeksforgeeks.org/lambda-expression-in-c/**/

class Solution {
public:
    std::vector<std::string> generateParenthesis(int n) {
         std::vector<std::string> ans;
         auto generate=[]<typename Range,typename Func>(Range& r,std::string s,int open,int close,int n,Func func){
             if (close==n)
             {
                 r.push_back(s);
                 return;
             }
             if(open<n)
                func(r,s+'(',open+1,close,n,func);
             if(close<open)
                func(r,s+')',open,close+1,n,func);
         }; 
         generate(ans,"",0,0,n,generate);
         return ans;
         
         }

    
};
