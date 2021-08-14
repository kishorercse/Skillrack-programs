/*
In a betting game involving the roll of a dice.  Sandeep gains Rs.X if an odd number turns up and he loses.  Rs.y is an even number turns up.  The numbers shown on the face of the face of the dice in a certain number of games is passed as input.  The values of X and Y are also passed as input.  The program must print net gain or loss as the output.

Example 1:

Input:
1 4 3
10
30
Output:
-10

Example 2:

Input:
4 6 1 2 1
50
25
Output:
25

Explanation:
He gains 100 rupees for 1,1, And loses 75 rupees for 4,6,2. Hence there is a net gain of 100-75=25
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[10],x,y,t=0,l=0;
    char ch;
    while(scanf("%d%c",&arr[l++],&ch)==2){
        if (ch=='\n' || ch=='\r')
            break;
    }
    scanf("%d\n%d",&x,&y);
    for(int i=0;i<l;i++){
        if (arr[i]%2==0)
            t-=y;
        else
            t+=x;
    }
    printf("%d",t);

}
