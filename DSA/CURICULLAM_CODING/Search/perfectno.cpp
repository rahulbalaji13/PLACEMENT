#include<iostream>
#include<vector>

using namespace std;

int main()
{
   int n; //Input size
   
   cout<<"Enter the size: \n";
   cin>>n;
   
   vector<int> ages(n);  //Input the ages using vector storage
   
   cout<<"Enter the ages of the students: \n";
   
   for(int i = 0; i < n; ++i)
   {
       cin>>ages[i];
   }    
       cout<<"The perfect age of the students are:";
       
       for(int i = 0; i < n; ++i)
       {
         int digit = ages[i];  //The student ages were assigned to the digit variable for easily applying the operations
         
         if(digit <= 1)
         
              continue;
        
        int sum = 1;
         
       for(int j = 2; j <= digit / 2; ++j) //the digit which is checked that it was divisible by 2
       {
        
        
        if(digit % j == 0) //Checking the condition was perfect number
        {	 	  	 	   	      	 	      		     	      	 	
          sum += j;  //Adding the sum of divisors caculated during checking of the perfect number
        }
       }        
         if(sum == digit) //Checking the final condtion that whether the sum of divisors found is similar to the age given as input 
         {
            cout<<digit<<"\n"; //Return the student ages which are in perfect numbers
         }
       }
           return 0;
}
