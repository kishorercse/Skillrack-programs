/*
The program must accept two string values S1 and S2 as the input. The program must swap vowels in the first string with vowels in the second string in the order of their occurrences. Then the program must print the modified string values as the output.

Boundary Condition(s):
1 <= Length of S1 and S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains modified S1.
The second line contains modified S2.

Example Input/Output 1:
Input:
environment
auditorium

Output:
anvurinmont
eidoterium

Explanation:
The vowels in the first string (environment) in the given order are e, i, o and e.
The vowels in the second string (auditorium) in the given order are a, u, i, o, i and u.
These vowels are swapped in both the string values in the given order.
So the two string values become anvurinmont and eidoterium.
The string S2 has two vowels more than the string S1 which are not swapped.

Example Input/Output 2:
Input:
pen
basket

Output:
pan
besket
*/
#include <bits/stdc++.h>
 
using namespace std;

bool isVowel(char ch){
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}

int main(int argc, char** argv)
{
    string a,b;
    cin >> a >> b;
    int x=a.size(), y=b.size(), i=0, j=0;
    while(i<x && j<y){
        while(i<x && !isVowel(a[i]))
            i++;
        while(j<y && !isVowel(b[j]))
            j++;
        if (i<x && j<y)
            swap(a[i++],b[j++]);
    }
    cout << a << endl;
    cout << b;
}
