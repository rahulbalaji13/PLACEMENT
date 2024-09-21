#include<iostream>
using namespace std;

int sentinelLS(int a[], int n, int target)
{
    //Assign array last element as last
    
    int l = a[n-1];
    
    //Place key value at the end of array
    
    a[n-1] = target;
    
    int i = 0;
    
    while(a[i] != target)
    {
        //If the target value was not found on first then move to proceeding iterations of array
        i++;
    }
    
    
    if(i < n - 1 || a[n - 1] == target)
    {
       return i;
    }   
      else 
    {  
       return -1;
    }
    
}

int main()
{
    int n;
    
    cout<<"Enter the number of employees: \n";
    cin>>n;
    
    cout<<"Enter the employee ages: \n";
    
    //Points to the array of employee ages
    int *age = new int[n];
    
    for(int i = 0; i < n; i++)
    {	 	  	 	   	      	 	      		     	      	 	
        cin>>age[i];
    }
    
    int target;
    cout<<"Enter the age needed to be searched: \n";
    cin>>target;
    
    int index = sentinelLS(age,n,target);
    
    if(index != -1)
    {
        cout<<"Age found at "<<index<<" index";
    }
    else 
    {
        cout<<"Age not found";
    }
    
    return 0;    
    
}
