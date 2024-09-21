#include<iostream>
#include<stack>
#include<string>

using namespace std;

//Sample Input: (a+b)*c

//Check the precedence of infix expression before performing stack operations

int precedence(char opr)
{
  if(opr == '+' || opr == '-')
  
      return 1;  //First precedence is + and - and if founded return 1
      
   if(opr == '*' || opr == '/')
   
      return 2;  //Second precedence is * and / and if founded return 2
      
   if(opr == '^')
   
      return 3;  //Third precendece is ^ and if founded return 3
      
   return 0;  //If not then return as 0
}

//Check whether the character expression input is operand

bool check_operand(char ch)
{
  return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= 0 && ch <= 9);
}

//Method to convert infix to postfix expression

string infixTOpostfix(string exp)
{	 	  	 	   	      	 	      		     	      	 	
  stack<char> stk;
  string postfix = "";
  
  for(char &ch : exp)
  {
      //If character is the operand then add to the output
      
      if(check_operand(ch))
      {
          postfix += ch;
      }
      
      //If character is '(' push it to the stack
      
      else if(ch == '(')
      {
          stk.push(ch);
      }
      
      //if character is ')' then pop and output(print) the stack
      
      //until we get '('
      
      else if(ch == ')')
            {  
             while(!stk.empty() && stk.top() != '(')
             {
                 postfix += stk.top();
                 stk.pop();
             }
             if(!stk.empty())
             
                 stk.pop();  //pop the '(' from the stack
            }
             else 
             {	 	  	 	   	      	 	      		     	      	 	
               while(!stk.empty() && precedence(stk.top()) >= precedence(ch))
              {
                postfix += stk.top();
                stk.pop();
              }
        
      stk.push(ch);
  
      }
  //Pop all the operator from the stack
  }
  while(!stk.empty())
  {
      postfix += stk.top();
      stk.pop();
  }
  return postfix;
}



int main()
{
      string exp;
      
      //Input: (a+b)*c
      
      cout << "Enter an infix expression: ";
      cin >> exp;        
      
      //Output: ab+c*
      
      string postfix = infixTOpostfix(exp);
      cout << "Postfix expression: " << postfix << endl;

      return 0;
}	 	  	 	   	      	 	      		     	      	 	