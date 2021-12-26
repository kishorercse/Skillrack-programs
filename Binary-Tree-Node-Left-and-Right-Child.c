/*
An array of N positive integers is passed as input. The program must form a binary search tree with these numbers. The first number (out of the N numbers passed as input) is
the root node of the binary tree. Then a number P which is present in these N numbers is passed as the input. The program must print the immediate left and right child values
of the node belonging to P, with the values separated by a space.

Note: If the node is a leaf node then print -1. Else if only left or only right child is present, then print only the child that is present.

Input Format:
The first line contains N numbers, each separated by a space.
The second line contains P

Output Format:
The first line contains the values of left and right child separated by a space (or only left or right child value)

Boundary Conditions:
1 <= N <= 9999

Example Input/Output 1:
Input:
1 2 5 3 6 4
5

Output:
3 6

Example Input/Output 2:
Input:
1 2 5 3 6 4
6

Output:
-1

Example Input/Output 3:
Input:
1 2 5 3 6 4
2

Output:
5


Max Execution Time Limit: 5000 millisecs

*/
#include<stdio.h>
#include<stdlib.h>
int p;
struct node
{
    int data;
    struct node *left, *right;
}*root=NULL;

struct node *createNode(int data)
{
    struct node *nd=malloc(sizeof(struct node));
    nd->data=data;
    nd->left=nd->right=NULL;
    return nd;
}

struct node *insert(struct node *curr, int data)
{
    if (root==NULL)
    {
        root=createNode(data);
        return;
    }
    if (curr==NULL)
    {
        return createNode(data);
    }
    if (data>curr->data)
    {
        curr->right=insert(curr->right,data);
    }
    else if (data<curr->data)
    {
        curr->left=insert(curr->left,data);
    }
}
void traversal(struct node* nd)
{
    if (nd==NULL)
        return;
    if (nd->data==p)
    {
        if (nd->left==NULL && nd->right==NULL)
            printf("-1");
        else
        {
            if(nd->left!=NULL)
                printf("%d ",nd->left->data);
            if(nd->right!=NULL)
                printf("%d",nd->right->data);
        }
        return;
    }
    traversal(nd->left);
    traversal(nd->right);
}
int main()
{
    int t, ind=0, l;
    char s[10001];
    scanf("%[^\n]",s);
    while(sscanf(s+ind,"%d%n",&t,&l)==1)
    {
        insert(root,t);
        ind+=l;
    }
    scanf("%d",&p);
    traversal(root);

}
