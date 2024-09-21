#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool IsAnagram(string str1, string str2) {
    // Convert both strings to uppercase
    transform(str1.begin(), str1.end(), str1.begin(), ::toupper);
    transform(str2.begin(), str2.end(), str2.begin(), ::toupper);

    // Remove spaces from both strings
    str1.erase(remove(str1.begin(), str1.end(), ' '), str1.end());
    str2.erase(remove(str2.begin(), str2.end(), ' '), str2.end());

    // Sort both strings
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());

    // Compare sorted strings
    return str1 == str2;
}

int main() {
    cout << "Anagram" << endl;

    string str1, str2;

    cout << "Enter the first string: ";
    getline(cin, str1);

    cout << "Enter the second string: ";
    getline(cin, str2);

    cout << " '" << str1 << "' and '" << str2 << "' are ";

    if (IsAnagram(str1, str2)) {
        cout << "anagrams";
    } else {
        cout << "not anagrams";
    }

    cout << endl;
    return 0;
}
