/*
The runs scored by a cricket team in the first and second innings of N test cricket matches are passed as input. 
The program must print the average of first and second innings (with precision upto two decimal places). 

Input Format: 
The first line denotes the value of N.
Next N lines will contain the first and second innings score separated by a space. 

Output Format: 
The first line contains the average of first innings score.
The second line contains the average of second innings score.

Boundary Conditions: 
2 <= N <= 20 
The value of the runs will be from 0 to 1000. 

Example Input/Output 1:
Input: 
3 
250 200 
450 300
200 250 

Output:
300.00 
250.00
*/
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n,a,b;
    float first=0,second=0;
    cin >> n;
    for(int i=1;i<=n;i++){
        cin >> a >> b;
        first+=a;
        second+=b;
    }
    cout << fixed << setprecision(2) << first/n << endl;
    cout << fixed << setprecision(2) << second/n;
}
