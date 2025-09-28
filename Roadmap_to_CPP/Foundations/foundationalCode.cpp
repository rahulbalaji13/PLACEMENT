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
