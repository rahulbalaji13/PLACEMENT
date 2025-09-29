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

//5. Check odd or even for array of elements 
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




