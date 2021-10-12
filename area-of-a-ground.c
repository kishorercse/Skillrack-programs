/*
In a running race, players have to know about the area of the ground. The ground is in trapezium shape. The length of the parallel sides denoted by A and B of the ground and 
the height H of the ground are given. The program must calculate and print the area of the ground with precision upto 2 decimal places as the output. 
Formula: Area of trapezium = ((A + B) * H) / 2 

Example Input/Output 1: 
Input: 
10 15 20 

Output: 
250.00 

Example Input/Output 2:
Input:
5 4 5

Output: 
22.5
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b,h;
    scanf("%d %d %d",&a,&b,&h);
    printf("%.2f",((a+b)*h)/2.0);
}
