/*

The program must accept an integer array of size N as the input. The program must reverse each integer in the array. Finally, the program must print the minimum difference of 
any two integers in the modified array as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Array Element Value <= 10000

Input Format:
The first line contains the integer value of N.
The second line contains N integers separated by spaces.

Output Format:
The first line contains the minimum difference obtained from two integers in the modified array.

Example Input/Output 1:
Input:
4
19 100 293 73

Output:
36

Explanation:
The array elements are 19 100 293 73.
After reversing each integer in the array, the elements are 91 1 392 37.
The minimum difference 36 is obtained from the two integers 1 and 37.
Hence 36 is printed as the output. 

Example Input/Output 2:
Input:
7
290 1800 27 92 35 39 72

Output:
1
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        int t;
        scanf("%d",&t);
        arr[i]=0;
        while (t>0)
        {
            arr[i]=arr[i]*10+t%10;
            t/=10;
        }
    }
    int minDiff=9999999;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            int d=abs(arr[i]-arr[j]);
            if (d<minDiff)
                minDiff=d;
        }
    }
    printf("%d",minDiff);

}
