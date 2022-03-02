/*
The program must accept an integer array of size N as the output. The program must print the next greater element for every element in the array. If there is no next greater 
element for an element, the program must print the same element as they are.

Boundary Condition(s):
1 <= N <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N integers which represent the next greater elements.

Example Input/Output 1:
Input:
7
2 1 5 15 10 6 20

Output:
5 5 15 20 20 20 20

Example Input/Output 2:
Input:
10
7 5 3 15 100 60 200 15 999 1

Output:
15 15 15 100 200 200 999 999 999 1
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

int isEmpty()
{
    return top==-1;
}

int peek()
{
    return stack[top];
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    for(int index=0;index<N;index++)
        scanf("%d",&arr[index]);
    for(int index=N-1;index>=0;index--)
    {
        if (isEmpty())
        {
            push(arr[index]);
        }
        else if (peek() > arr[index])
        {
            int temp=peek();
            push(arr[index]);
            arr[index]=temp;
        }
        else
        {
            while(!isEmpty() && peek()<=arr[index])
            {
                pop();
            }
            if (isEmpty())
            {
                push(arr[index]);
            }
            else
            {
                int temp=peek();
                push(arr[index]);
                arr[index]=temp;
            }
        }
    }
    for(int index=0;index<N;index++)
    {
        printf("%d ",arr[index]);
    }

}
