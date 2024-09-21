#include<iostream>
#include<stack>

using namespace std;

int main()
{
  stack<int> stk; //Stack is the one of inbuilt method in C++ STL 
  
  int n; //Input 'n' for decimal number 
  
  cout<<"Enter the decimal number: ";
  cin>>n;
  
  if(n == 0)
  {
     cout<<"\n Binary number is 0"<<endl;
  }
  
  while(n > 0)
  {
      stk.push(n%2); //Calculating and pushing the remainder of entered decimal number
      n /= 2; //Dividing and seperating the decimal number into binary equialent 
  }
  
  cout<<"\n The binary equialent of the entered number is: ";
  while(!stk.empty()) //Check whether the stack is empty
  {
      cout<<stk.top();
      stk.pop();
  }
  
     return 0;
  
}	 	  	 	   	      	 	      		     	      	 	
