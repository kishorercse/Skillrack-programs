/*
Arun reads lot of story books and he keeps all the story books piled as a single stack. He wants to write a program to keep the order of the books in the pile. The program must 
implement the following functionalities. 
- Add a book to the top of the pile when 1 is followed by the name of the book. 
- Remove a book from the top of the pile when -1 is given as the input (provided the pile has atleast one book).
- Print the name of the book on the top of the pile when 2 is given as the input (provided the pile has atleast one book).
- The program must exit when 0 is given as the input.

Boundary Condition(s): 
The maximum number of story books in the pile will be 100. 
The name of the book will not exceed 100 characters. 

Example Input/Output 1: 
Input:
1 The Arrival 
1 The Borrowers
1 The Cat in the Hat
2 
-1
2 
1 Curious George 
2
-1
2
-1
2
-1
2
-1
1 Freight Train
2
0

Output: 
The Cat in the Hat 
The Borrowers 
Curious George 
The Borrowers
The Arrival
Freight Train 

Explanation: 
After the first three lines of input, the books from top to bottom in the pile are 
-The Cat in the Hat 
-The Borrowers 
-The Arrival 

Now 2 prints "The Cat in the Hat" which is at the top of the pile. Then -1 removes the book on the top. So now the books in the pile from top to bottom are 
-The Borrowers 
-The Arrival 

Now 2 prints "The Borrowers". Now the book "Curious George" is added to the top of the pile. So now the books in the pile from top to bottom are 
-Curious George 
-The Borrowers 
-The Arrival 

Now 2 prints "Curious George". -1 removes "Curious George". So now the books in the pile from top to bottom are 
-The Borrowers 
-The Arrival 

Now 2 prints "The Borrowers". -1 removes "The Borrowers". So now the books in the pile from top to bottom are
-The Arrival 
Now 2 prints "The Arrival". -1 removes "The Arrival". So now there are no books in the pile.
Now 2 does not print anything as the pile is empty. 
Now -1 does not remove anything as the pile is empty. 
Then 1 adds "Freight Train" to the top of the pile. 
Now 2 prints "Freight Train". 
Now 0 ends the program.
*/
#include<stdio.h>
#include<stdlib.h>

char stack[100][101];
int top=-1;

int main()
{
    int n;
    scanf("%d",&n);
    while (n!=0){
        if (n==1){
            scanf("%[^\n]",stack[++top]);
        }
        else if (top!=-1){
            if (n==2)
                printf("%s\n",stack[top]);
            if (n==-1)
                top-=1;
            
        }
        scanf("%d",&n);
    }
}
