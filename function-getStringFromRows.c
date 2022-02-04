/*
The function/method getStringFromRows accepts five arguments - R, C, matrix, X and Y. The first two arguments R and C represent the size of a character matrix. The third
argument matrix represents a pointer to the R*C character matrix. The last two arguments X and Y represent the positions of two rows.

The function/method getStringFromRows must form a string value using the characters from the Xth to the Yth row of the given matrix. Consider the rows of the matrix in circular
fashion when forming the string value. Finally, the function must return the resulting string.

Your task is to implement the function getStringFromRows so that the program runs successfully.

IMPORTANT: Do not implement the main() function as it is already defined.

Example Input/Output 1:
Input:
8 5
k b n z c
m n n o h
a y v n q
e l r a q
i b j d o
u w v j e
u a h x g
b b j s d
2 5

Output:
mnnohayvnqelraqibjdo

Explanation:
The characters from the 2nd row to the 5th row of 8*5 character matrix are highlighted below.
k b n z c
m n n o h
a y v n q
e l r a q
i b j d o
u w v j e
u a h x g
b b j s d

Example Input/Output 2:
Input:
8 5
k b n z c
m n n o h
a y v n q
e l r a q
i b j d o
u w v j e
u a h x g
b b j s d
7 2

Output:
uahxgbbjsdkbnzcmnnoh
*/

#include <stdio.h>
#include <stdlib.h>

char* getStringFromRows(int R, int C, char *matrix, int X, int Y)
{    
    char *res=malloc(sizeof(char)*10001);
    int row=X-1, ind=0;
    while (1)
    {
        for (int j=0;j<C;j++)
        {
            res[ind++]=matrix[C*row+j];
        }
        row++;
        if (row==Y)
            break;
        row%=R;
        if (row==Y)
            break;
    }
    return res;
} // End of getStringFromRows function

int main()
{
    int R, C, X, Y;
    scanf("%d %d", &R, &C);
    char matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf(" %c", &matrix[row][col]);
        }
    }
    scanf("%d %d", &X, &Y);
    char *result = getStringFromRows(R, C, matrix, X, Y);
    if(result == NULL)
    {
        printf("New string is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
} // End of main() function
