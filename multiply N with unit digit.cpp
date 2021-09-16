/*
The program must accept a positive integer N and print the value of N multiplied with it’s unit digit.

Boundary Condition(s):
1 <= N <= 9999

Input Format:
The first line contains N.

Output Format:
The first line contains the value of N multiplied with it’s unit digit.

Example Input/Output 1:
Input:
24

Output:
96

Explanation:
The unit digit of 24 is 4. Hence 24*4 = 96.
 
Example Input/Output 2:
Input:
401

Output:
401
*/
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n;
    cin >> n;
    cout << n*(n%10);
}
