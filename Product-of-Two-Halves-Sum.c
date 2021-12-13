/*
The program must accept a list of integers as the input. The program must print the product of the sum of the first half of the integers and the sum of the second half of the 
integers as the output. Note: If the number of integers is odd then consider the integer in the middle as part of the second half.

Boundary Condition(s):
1 <= Number of Integers <= 100
1 <= Array Element Value <= 1000

Input Format:
Thr first line contains the list of integers separated by spaces.

Output Format:
The first line contains the product of the sum of the first half integers and the sum of the second half integers.

Example Input/Output 1:
Input:
9 1 2 8 7 2

Output:
204

Explanation:
The first half integers are 9, 1 and 2 and their sum is 12.
The second half integers are 8, 7 and 2 and their sum is 17.
The product of 12 and 17 is 204.
Hence the output is 204

Example Input/Output 2:
Input:
5 2 10 2 1

Output:
91
 
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[100], n=0;
    while(scanf("%d",&arr[n++])==1);
    int first=0, second=0;
    int i=0, j=n-2;
    while(i<j)
    {
        first+=arr[i++];
        second+=arr[j--];
    }
    if (i==j)
        second+=arr[i];
    printf("%d",first*second);

}
