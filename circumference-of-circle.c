/*
The program must accept an integer D which denotes the diameter of a circle as the input. The program must print the circumference of the circle with precision 
up to 3 decimal places as the output.

Example Input/Output 1: 
Input: 
20 

Output:
62.857 

Example Input/Output 2: 
Input: 
18 

Output: 
56.571
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int d;
    scanf("%d",&d);
    printf("%.3f",22*d/7.0);

}
