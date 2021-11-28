/*The program must accept N unique integers and an integer K as the input. The first integer among the given N integers is considered as the root of the Binary Search Tree 
(BST) to be formed. The program must print the subtree having the root node K in pre-order traversal. If the given node K is not present in the tree, then the program must
print the -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the integers values or -1.

Example Input/Output 1:
Input:
8
25 15 5 45 55 40 42 20
45

Output:
45 40 42 55

Explanation:
Here K = 45.
So the integers in the subtree having the root node 45 are printed in pre-order traversal.
45 40 42 55
The root of the subtree is 45.
The left child of 45 is 40.
The right child of 40 is 42.
The right child of 45 is 55.

Example Input/Output 2:
Input:
8
25 15 5 45 55 40 42 20
25

Output:
25 15 5 20 45 40 42 55

Example Input/Output 3:
Input:
4
10 20 15 30
25

Output:
-1
*/
#include<stdio.h>
#include<stdlib.h>
int global_flag,k;
struct Node
{
    int data;
    struct Node *left, *right;
}*root=NULL;

struct Node *createNode(int data)
{
    struct Node *node=(struct Node*)malloc(sizeof(struct Node));
    node->data=data;
    node->left=node->right=NULL;
    return node;
}

struct Node *insert(struct Node *root, int data)
{
    if (root==NULL)
        return createNode(data);
    if (data < root->data)
        root->left=insert(root->left,data);
    else if (data > root->data)
        root->right=insert(root->right,data);
}

void preOrderTraversal(struct Node *root, int flag)
{
    if (root==NULL)
        return;
    if (root->data==k)
    {
        flag=1;
        global_flag=1;
    }
    if (flag==1)
        printf("%d ",root->data);
    preOrderTraversal(root->left,flag);
    preOrderTraversal(root->right,flag);
}

int main()
{
    int n,data;
    scanf("%d %d",&n,&data);
    root=insert(root,data);
    for(int i=1;i<n;i++)
    {
        scanf("%d",&data);
        insert(root,data);
    }
    scanf("%d",&k);
    preOrderTraversal(root,0);
    if (global_flag==0)
        printf("-1");
}
