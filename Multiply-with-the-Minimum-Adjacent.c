/*
The program must accept an integer array of size N as the input. The program must replace each element in the array by the product of the current element and the minimum of 
it's adjacent elements. Finally, the program must print the modified array as the output. (The first and last elements have only one element adjacent to them. So consider only the single adjacent element for them).

Boundary Condition(s):
2 <= N <= 100

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains N integers of the modified array separated by a space.

Example Input/Output 1:
Input:
6
7 6 4 5 9 3

Output:
42 24 20 20 27 27

Explanation:
For 1st element, 7 is replaced by the product of 7 and 6. So 42 is printed.
For 2nd element, 6 is replaced by the product of 6 and 4. So 24 is printed.
For 3rd element, 4 is replaced by the product of 4 and 5. So 20 is printed.
For 4th element, 5 is replaced by the product of 5 and 4. So 20 is printed.
For 5th element, 9 is replaced by the product of 9 and 3. So 27 is printed.
For 6th element, 3 is replaced by the product of 3 and 9. So 27 is printed.

Example Input/Output 2:
Input:
9
37 18 14 32 23 78 86 56 81

Output:
666 252 252 448 736 1794 4816 4536 4536


*/
#include<stdio.h>
#include<stdlib.h>

#define MIN(x,y) ((x<y)?x:y)
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("%d ",arr[0]*arr[1]);
    for(int i=1;i<n-1;i++)
    {
        printf("%d ",arr[i]*MIN(arr[i-1],arr[i+1]));
    }
    printf("%d",arr[n-2]*arr[n-1]);

}
