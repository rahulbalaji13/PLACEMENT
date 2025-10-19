#include<bits/stdc++.h>
using namespace std;
int main()
{
  for(int i = 0; i < 5; i++)
  {
    for(int j = 0; j < 5; j++)
    {
      cout<<"*";    
    }
    cout<<endl;
  }
   return 0;
}  

/**
OUTPUT:

*****
*****
*****
*****
*****

**/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 1; j <= i; j++)
        {
            cout<<j;
        }
        cout<<endl;
    }
    return 0;
}

/**
1
12
123
1234
12345
**/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 1; j <= i; j++)
        {
            cout<<i;
        }
        cout<<endl;
    }
    return 0;
}

/**
1
22
333
4444
55555
**/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 5; j >= i; j--)
        {
            cout<<"* ";
        }
        cout<<endl;
    }
    return 0;
}

/**
[?2004l
* * * * * 
* * * * 
* * * 
* * 
* 
[?2004h

**/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 5; j >= i; j--)
        {
            cout<<5 - j + 1<<" ";
        }
        cout<<endl;
    }
    return 0;
}

/**
[?2004l
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
[?2004h
**/

