//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
             int mod = 1e5;
    public:
        vector <int> search(string pat, string txt)
        {
             vector<int>ans;
             
             int t = 0; //TO compute hash value of text
             int p = 0; //To compute hash value of pattern
             
             int n = txt.size();
             int m = pat.size();
             
             for(int i = 0; i < m; i++)
             {
                 //TO compute hash function with correspond ASCII value of the given alphabet
                 t = ((txt[i] - 'a') + t) % mod; 
                 p = ((pat[i] - 'a') + p) % mod;
             }
            
             if(t == p)
             {
                 if(txt.substr(0,m)==pat)
                 
                      ans.push_back(1);
             }
            
             for(int i = m, j = 0; i < txt.size(); i++, j++)
             {   
                 //Slide the text over pattern one by one
                 t = (t - txt[j]) % mod;
                 //Sum the substring found on roll hash/slide
                 t = (t + txt[i]) % mod;
                
                 if(t == p)
                {
                     if(txt.substr(j + 1 , m) == pat)
                       
                          ans.push_back(j + 2);
                }
            }
              return ans;
        }
};

//ASCII value of the respective alphabets 
//a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8; i = 9, j = 10,
//k = 11, l = 12, m = 13, n = 14, o = 15, p = 16, q = 17, r = 18, s = 19, t = 20, u = 21, 
//v = 22, w = 23, x = 24, y = 25, z = 26
//Since the alhapbet's ASCII startes from 1 and end with 26 so, 
//take that value as MOD 26 value

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S, pat;
        cin >> S >> pat;
        Solution ob;
        vector <int> res = ob.search(pat, S);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}



// } Driver Code Ends
