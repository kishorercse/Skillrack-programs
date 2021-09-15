/*
he program must accept N integers as the input. The program must print all the even integers which are at the even positions as the output. 
If there is no even integer at even positions then the program must print -1 as the output. 

Boundary Condition(s): 
1 <= N <= 10^5
-99999 <= Each Integer Value <= 99999 

Input Format: 
The first line contains the value of N. 
The second line contains N integers separated by space(s). 

Output Format: 
The first line contains the even integers which have occurred at the even positions each separated by a space. 

Example Input/Output 1: 
Input: 
7
43 -49 -22 16 -86 78 77 
Output: 
16 78 
Explanation: 
The integers present at even positions are -49, 16 and 78. So the even integers are 16 and 78. 
Hence the output is 16 78

Example Input/Output 2:
Input: 
5 
24 -45 38 -13 37 
Output:
-1
*/
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n,t,flag=0;
    cin >> n;
    for(int i=1;i<=n;i++){
        cin >> t;
        if (i%2==0 && t%2==0){
            cout << t << " ";
            flag=1;
        }
    }
    if (flag==0)
        cout << -1;
}
