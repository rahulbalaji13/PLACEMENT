//1.FIND MAXIMUM AND MINIMUM ELEMENT FROM AN ARRAY

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[] = {1,2,3,4,5};
    
    int minVal = a[0];
    int maxVal = a[0];
    
    for(int i = 0; i < 5; i++)
    {
        if(a[i] < minVal)
        {
            minVal = a[i];
        }
        else if(a[i] > maxVal)
        {
            maxVal = a[i];
        }
    }
    cout<<"Min is: "<<minVal<<endl;
    cout<<"Max is: "<<maxVal<<endl;
    return 0;
}

//2. REVERSE THE GIVEN STRING

#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "HELLO WORLD";
    reverse(s.begin(),s.end());
    cout<<s<<" ";
 
    return 0;
}

//3. Reverse the array element 

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[] = {1,2,3,4,5};
    reverse(a,a+5);
    for(int i = 0; i < 5; i++)
    {
        cout<<a[i];
    }
    return 0;
}

//4. Check the number is palindrome or not
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n = 78987;
    int temp = n;
    int rev = 0;
    
    while(temp != 0)
    {
       int last = temp % 10;
       rev = rev * 10 + last;
       temp=temp/10;
    }
    if(rev == n)
    {
        cout<<"palindrome";
    }
    else 
    {
        cout<<"Not palindrome";
    }
    return 0;
}

//5. Check whether the given string is palindrome or not
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "MADAM";
    string temp = s;
    reverse(s.begin(),s.end());
    
    if(temp == s)
    {
        cout<<"Palindrome"<<endl;
    }
    else
    {
        cout<<"Not Palindrome"<<endl;
    }
    return 0;
}

//6. Check odd or even for array of elements 
#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> arr = {1,2,3,4,5};
    
    for(int a:arr)
    {
        if(a % 2 == 0)
        {
            cout<<"Even"<<endl;
        }
        else 
        {
            cout<<"Odd"<<endl;
        }
    }
    return 0;
}
//7. Find the second largest and smallest element 

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int arr[] = {1,2,3,4,5};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    int largest = INT_MIN, second_largest = INT_MIN;
    int smallest = INT_MAX, second_smallest = INT_MAX;
    
    for(int i = 0; i < n; i++)
    {
        if(arr[i] > largest)
        {
            largest = arr[i];
        }
        if(arr[i] < smallest)
        {
            smallest = arr[i];
        }
    }
    
    for(int i = 0; i < n; i++)
    {
        if(arr[i] != largest && arr[i] > second_largest)
        {
            second_largest = arr[i];
        }
        if(arr[i] != smallest && arr[i] < second_smallest)
        {
            second_smallest = arr[i];
        }
    }
    
    if(second_largest == INT_MIN)
    {
        cout<<"No second largest exist"<<"\n";
    }
    else
    {
        cout<<"Second largest exist"<<second_largest<<"\n";
    }
    if(second_smallest == INT_MAX)
    {
        cout<<"No second smallest exist"<<"\n";
    }
    else
    {
        cout<<"Second smallest exist"<<second_smallest<<"\n";
    }
    return 0;
}

//8. Remove deuplicates from an array

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int arr[] = {1,2,3,3,5};
    int n = sizeof(arr)/sizeof(arr[0]);
    set<int> unique;
    
    for(int i = 0; i < n; i++)
    {
        unique.insert(arr[i]);
    }
    
    for(int point : unique)
    {
        cout<<point;   
    }

    return 0;
}

//9. Merge two sorted arrays
#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v1 = {1,2,3};
    vector<int> v2 = {4,5,6};
    vector<int> res(v1.size() + v2.size());
    
    merge(v1.begin(),v1.end(),v2.begin(),v2.end(),res.begin());
    
    for(int num : res)
    {
        cout<<num<<" ";
    }
    return 0;
}

//Move all zeros to end of an array 
#include<bits/stdc++.h>
using namespace std;

void moveZero(int arr[], int n)
{
   int result = 0;
   for(int i = 0; i < n; i++)
   {
       if(arr[i] != 0)
       {
         arr[result++] = arr[i];
       }
    }
    while(result < n)
    {
          arr[result++] = 0;
    }
}

int main()
{
    int arr[] = {1,2,0,3,4,0,0};
    int n = sizeof(arr)/sizeof(arr[0]);
    moveZero(arr,n);
    for(int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}

//Rotate an array by k position
#include<bits/stdc++.h>
using namespace std;
void rotatekpos(int arr[], int n, int k)
{
    k = k % n;
    int temp[n];
    
    for(int i = 0; i < k; i++)
    {
        temp[i] = arr[n - k + i];
    }
    
    for(int i = k; i < n; i++)
    {
        temp[i] = arr[i - k];
    }
    
    for(int i = 0; i < n; i++)
    {
        arr[i] = temp[i];
    }
}

int main()
{
   int arr[] = {1,2,3,4,7,8,9};
   int k = 2;
   int n = sizeof(arr)/sizeof(arr[0]);
   rotatekpos(arr, n, k);
   for(int i = 0; i < n; i++)
   {
       cout<<arr[i]<<" ";
   }
   return 0;
}

/**
Using C++ STL for above code:

//Rotate the element in array for k positions

#include<bits/stdc++.h>
using namespace std;
void rotatekpos(vector<int>&arr,int k)
{
    int n = arr.size();
    k = k % n;
    
    reverse(arr.begin(),arr.end());
    reverse(arr.begin(),arr.begin() + k);
    reverse(arr.begin() + k,arr.end());
}

int main()
{
   vector<int> arr = {1,2,3,4,7,8,9};
   int k = 2;
   int n = arr.size();
   rotatekpos(arr,k);
   for(int i = 0; i < n; i++)
   {
       cout<<arr[i]<<" ";
   }
   return 0;
}
**/










