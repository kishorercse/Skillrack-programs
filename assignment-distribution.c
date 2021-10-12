/*
There are X assignments arranged on a table to be corrected. It has to be distributed equally to Y staff members. The program must print the number of assignments 
which are left after distributing the assignments equally to the Y staff members.

Example Input/Output 1:
Input:
159 10 

Output: 
9

Example Input/Output 2:
Input: 
346 5 

Output: 
1 

Example Input/Output 3: 
Input: 
340 20

Output: 
0
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d",x%y);

}
