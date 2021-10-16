/*
Given a set of numbers where all other numbers are multiple of smallest number, the program must find the count of the common factor C excluding 1.

Example 1:

Input:
2
100
75

Output:
2

Explanation: The common factors excluding 1 are 5,25. Hence output is 2.

Example 2:
Input:
3
10
20
30

Output:
3

Explanation:
The common factors are excluding 1 are 2,5,10. Hence output is 3.
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int min=999999,n,count=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
        if (arr[i]<min)
            min=arr[i];
    }
    for(int f=2;f<=min;f++){
        int t=n;
        for(int i=0;i<n;i++){
            if (arr[i]%f==0)
                t-=1;
        }
        if (t==0)
            count+=1;
    }
    printf("%d",count);

}
