#include <iostream>
#include <string>
#include <vector>

using namespace std;

void createlps(const string& pattern, vector<int>& lps) 
{
    int m = pattern.length();
    int j = 0; // Tracks the length of the longest prefix suffix

    lps[0] = 0; // LPS[0] is always 0
    int i = 1;  // Start calculating from index 1

    while (i < m) 
    {
        if (pattern[i] == pattern[j]) 
        { // Matching characters
            j++;
            lps[i] = j;
            i++;
        } else 
          { // Mismatch
            if (j != 0) 
            {
                j = lps[j - 1]; // Use LPS to avoid redundant comparison
            } 
            else 
            {
                lps[i] = 0;
                i++;
            }
          }
    }
}

void KMPalgm(const string& text, const string& pattern) 
{
    int m = text.length();
    int n = pattern.length();

    vector<int> lps(n);

    createlps(pattern, lps); // Generate LPS array

    int i = 0; // Pointer for text
    int j = 0; // Pointer for pattern

    while (i < m) 
    {
        if (pattern[j] == text[i]) 
        {
            i++;
            j++;
        }

        if (j == n) 
        { // Pattern found
            cout << "Pattern found at index " << i - j << endl;
            j = lps[j - 1]; // Use LPS to continue search
        } else if (i < m && pattern[j] != text[i]) 
        {
            if (j != 0) 
            {
                j = lps[j - 1];
            } 
            else 
            {
                i++;
            }
        }
    }
}

int main() 
{
    string text, pattern;

    // Input text
    cout << "Enter the text in which you want to search: ";
    getline(cin, text); // Use getline to allow spaces in the text

    // Input pattern
    cout << "Enter the pattern you want to search for: ";
    getline(cin, pattern);

    // Call the KMP algorithm
    KMPalgm(text, pattern);

    return 0;
}
