/*
The program must accept an integer N as the input.
If the value of N is 1 the program must print on as the output. 
If the value of N is 0 then the program must print off as the out.
Note: The input is always either 1 or 0. 

Boundary Condition(s): 0 <= N <= 1 

Input Format: 
The first line contains the integer N. 

Output Format: 
The first line contains either on or off. 

Example Input/Output 1: 
Input: 
1 

Output: 
on 

Example Input/Output 2: 
Input: 
0 

Output: 
off
*/
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    bool n;
    cin >> n;
    cout << (n?"on":"off");
}
