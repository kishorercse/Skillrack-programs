/*
There are M students participating in a competition. There are Y certificates to be given. If a student wins he gets an award certificate plus participation certificate. 
Else if he loses he gets only a participation certificate. The program must accept the input values for M, Y and W(number of students who wins the competition) and print 
the number of certificates remaining after distribution as the output. 

Input Format:
The first line contains the values of M, Y and W separated by spaces.

Example Input/Output 1:
Input:
50 120 30 

Output: 
40 

Explanation: 
Participation certificates = 50, Award certificates = 30. 
Remaining certificates = 120-(50+30)=40. 
Hence 40 is printed as the output.
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,y,w;
    scanf("%d %d %d",&m,&y,&w);
    printf("%d",y-m-w);

}
