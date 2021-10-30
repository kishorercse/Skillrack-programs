/*
The program must accept N integers and X number of pairs as the input. Each pair contains two integers V and P. V represents an integer value to be added to the integer present 
in the position P. For each pair, the program must add the integer V to the integer in the position P and then print the sum of even integers in the modified array as the output.

Boundary Condition(s): 
1 <= N, X <= 10^5 
-10^4 <= Each integer value, V <= 10^4 
1 <= P <= N 

Input Format: 
The first line contains N and X separated by a space. 
The second line contains the N integers separated by a space. 
The next X lines contain the pair of integers ( V and P) separated by space(s). 

Output Format: 
The first line contains the sum of even integers separated by a space. 

Example Input/Output 1: 
Input: 
5 2 
17 12 10 2 21 
5 2 
7 3 

Output: 
12 2 

Explanation: 
For the 1st pair (5, 2), the value 5 is added to the integer 12. 
Now the array becomes 17 17 10 2 21. 
Here the sum of even integers is 12 (10 + 2). 
For the 2nd pair (7, 3), the value 7 is added to the integer 10. 
Now the array becomes 17 17 17 2 21. 
Here the sum of even integer(s) is 2 (2). 
Hence the output is 12 2 

Example Input/Output 2: 
Input: 
10 10
10 91 83 79 100 76 54 53 27 5 
8 4 
3 7 
1 5 
7 3 
5 1 
6 8 
9 2 
2 9 
4 6 
9 10

Output: 
240 186 86 176 166 166 266 266 270 284
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,x;
    scanf("%d %d",&n,&x);
    int arr[n],sum=0;
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
        if (arr[i]%2==0)
            sum+=arr[i];
    }
    for(int i=0;i<x;i++){
        int v,p;
        scanf("%d %d",&v,&p);
        p-=1;
        if (arr[p]%2==0)
            sum-=arr[p];
        arr[p]+=v;
        if (arr[p]%2==0)
            sum+=arr[p];
        printf("%d ",sum);
    }
}
