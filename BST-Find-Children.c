"""
The program must accept N integers. The first value is considered as the root of the Binary Search Tree (BST) to be formed. The program must print the children(left and right) of the given node K in the BST. If the given node does not have a child, then the program must print the string value "LEAF" as the output.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains the children(left and right) of the given node K in the BST.

Example Input/Output 1:
Input:
6
50 30 90 40 70 100
90

Output:
70 100

Explanation:
Here 50 is the root of the BST.
30 -> Left child of 50.
90 -> Right child of 50.
40 -> Right child of 30.
70 -> Left child of 90.
100 -> Right child of 90.
K = 90, so the children of 90 are 70 and 100.
Hence the output is
70 100

Example Input/Output 2:
Input:
9
25 40 55 60 35 20 10 30 15
30

Output:
LEAF

Example Input/Output 3:
Input:
4
10 20 15 30
10

Output:
20
"""
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int value;
    struct node *left, *right;
};

struct node *newNode(int value)
{
    struct node *nd=(struct node*)malloc(sizeof(struct node));
    nd->value=value;
    nd->left=nd->right=NULL;
    return nd;
}

struct node *insert(struct node *nd, int value)
{
    if (nd==NULL)
        return newNode(value);
    if (value < nd->value)
        nd->left=insert(nd->left,value);
    else if(value > nd->value)
        nd->right=insert(nd->right,value);
}

struct node *search(struct node *root, int key)
{
    if (root==NULL || root->value==key)
        return root;
    if (key < root->value)
        return search(root->left,key);
    else
        return search(root->right,key);
}

int main()
{
    int n,k,t;
    scanf("%d",&n);
    scanf("%d",&t);
    struct node *root=NULL;
    root=insert(root,t);
    for(int i=1;i<n;i++)
    {
        scanf("%d",&t);
        insert(root,t);
    }
    scanf("%d",&k);
    struct node *nd=search(root,k);
    if (nd->left==NULL && nd->right==NULL)
        printf("LEAF");
    else
    {
        if (nd->left!=NULL)
            printf("%d ",nd->left->value);
        if (nd->right!=NULL)
            printf("%d",nd->right->value);
    }
    
}
