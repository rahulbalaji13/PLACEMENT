#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
   stack<char> stk;
   string name;
   
   int choice;
   char ch;
   
   cout<<"Enter your name: ";
   getline(cin , name);
   
   do
   {
      cout<<"\n Stack Operations"<<endl;
      cout<<"\n 1.Push my name character into the stack"<<endl;
      cout<<"\n 2.Pop a my name character from the stack"<<endl;
      cout<<"\n 3.Display the current stack"<<endl;
      cout<<"\n 4.Exit the program"<<endl;
      
      cout<<"\n Enter your choice: ";
      cin>>choice;
      
      switch(choice)
      {
         case 1:
                 for(char c : name)
                 {
                     stk.push(c); //Push the string name = RAHUL
                 }
                 cout<<"\n Your name inserted into the stack";  
                 break;
                 
         case 2: 
                 if(!stk.empty())
                 {	 	  	 	   	      	 	      		     	      	 	
                    ch = stk.top();  //Assign stack top to the character variable
                    stk.pop();       //Pop the elements from the stack - pop the topmost element from the stack
                    
                    cout<<"\n The popped character is: "<<ch;  //Pop and display character in top of the stack 
                 }
                   else 
                 { 
                    cout<<"\n The stack is empty";
                 }
                 break;
                 
         case 3: 
                 if(!stk.empty())
                 {
                     stack<char> tstk = stk;  //Create temproary stack and assign to the previous stack
                     cout<<"\n Stack character(Top or Bottom)"; 
                     while(!tstk.empty())
                     {
                         cout<<tstk.top()<<" ";  //Display the top elemnt of the temproary stack that already assigned to previous stack
                         tstk.pop(); //Pop the top pointed temproary stack character 
                     }
                 }
                 else
                 {
                     cout<<"\n Stack is empty"<<endl;
                 }
                 break;
                 
          case 4: 
                   cout<<"\n Exiting the program"<<endl;
                   break;
                   
          default: cout<<"\n Invalid choice. Please try again";
                     
        }
      }	 	  	 	   	      	 	      		     	      	 	
      while(choice != 4);      

      return 0;
}
   
    
    
