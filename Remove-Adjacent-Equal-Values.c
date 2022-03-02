/*
The program must accept an integer array of size N as the input. The program must remove the adjacent values in the array if they are equal. The program must repeat the process
till there are no more equal adjacent values in the array. Finally, the program must print the integers in the array as the output. If there is no integer in the array, the 
program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the integers in the modified array or -1.

Example Input/Output 1:
Input:
9
20 15 10 30 30 10 15 50 90

Output:
20 50 90

Example Input/Output 2:
Input:
6
10 20 30 30 20 10

Output:
-1


*/
#include<stdio.h>
#include<stdlib.h>

int stack[100000];
int top=-1;

void push(int num)
{
    stack[++top]=num;
}

int pop()
{
    return stack[top--];
}

int peek()
{
    return stack[top];
}

int isEmpty()
{
    return top==-1;
}

int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    for(int index=0;index<N;index++)
    {
        scanf("%d",&arr[index]);
    }
    for(int index=N-1;index>=0;index--)
    {
        if (isEmpty() || peek()!=arr[index])
        {
            push(arr[index]);
        }
        else
        {
            pop();
        }
    }
    if (isEmpty())
    {
        printf("-1");
    }
    while(!isEmpty())
    {
        printf("%d ",pop());
    }
    

}
