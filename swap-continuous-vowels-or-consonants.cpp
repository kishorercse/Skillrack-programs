/*
A string S is passed as the input to the program. The program must swap two continuously occurring alphabets if both 
of them are vowels or both of them are consonants. Then the program must print the modified string as the output. 

Boundary Condition(s): 
1 <= Length of S <= 100 

Input Format: 
The first line contains the string S. 

Output Format: 
The first line contains the modified string. 

Example Input/Output 1: 
Input: 
introduction 

Output:
itrnodutcoin 

Explanation: 
The alphabets 'n' and 't' in introduction are both consonants so they are swapped so the string becomes itnroduction. 
The alphabets 'n' and 'r' in itnroduction are both consonants so they are swapped so the string becomes itrnoduction. 
The alphabets 'i' and 'o' in introduction are both vowels so they are swapped so the string becomes itrnoductoin. 

Example Input/Output 2:
Input: 
maintenance 

Output: 
miatnenacne
*/
#include <bits/stdc++.h>
 
using namespace std;

bool isVowel(char ch){
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main(int argc, char** argv)
{
    string s;
    cin >> s;
    for(int i=1;s[i];i++){
        if (isVowel(s[i-1])==isVowel(s[i]))
            swap(s[i-1],s[i]);
    }
    cout << s;
}
