/*
The function/method groupIntegersAndFormMatrix accepts an argument str. The string str contains integer values separated by a space, where each integer ends with a lower case
alphabet. The 26 lower case alphabets(a to z) are mapped to the rows numbered from 1 to 26. The lower case alphabet at the end of each integer indicates that the integer belongs
to the corresponding row of the integer matrix to be formed (a indicates the integers of the 1st row, b indicates the integers of the 2nd row, and so on).

The function/method groupIntegersAndFormMatrix must group the integer values based on the lower case alphabets. In each group, there will be an equal number of integers. Then
the function must form an integer matrix using the groups of integers. In each row of the matrix, the integers must be in the order of their occurrence. Finally, the function 
must return the integer matrix.

Your task is to implement the function groupIntegersAndFormMatrix so that it passes all the test cases.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int R, C;
    int **matrix;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
90c 30a 80c 50b 10a 70c 60b 20a 40b

Output:
3 3
30 10 20
50 60 40
90 80 70

Explanation:
Group a: 30, 10, 20
Group b: 50, 60, 40
Group c: 90, 80, 70
There are 3 groups of integers in the given string, which indicates the number of rows of the matrix.
There are 3 integers in each group, which indicates the number of columns of the matrix.
So the 3*3 integer matrix will be
30 10 20
50 60 40
90 80 70

Example Input/Output 2:
Input:
10b 32a 31b 54a 81b 82a 63a 15b

Output:
2 4
32 54 82 63
10 31 81 15
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int R, C;
    int **matrix;
} boundedArray;

boundedArray* groupIntegersAndFormMatrix(char *str)
{
    boundedArray *bArr=malloc(sizeof(boundedArray));
    bArr->R = bArr->C = 0;
    int t;
    for(int i=0;str[i];i++)
    {
        if (isalpha(str[i]))
        {
            if (str[i]=='a')
                bArr->C++;
            t=(str[i]-96);
            bArr->R=(t>bArr->R)?t:bArr->R;
        }
    }
    int colIndex[bArr->R], ptr=0, n;
    char ch;
    memset(colIndex,0,bArr->R*sizeof(int));
    bArr->matrix=malloc(sizeof(int*)*bArr->R);
    for(int i=0;i<bArr->R;i++)
    {
        bArr->matrix[i]=malloc(sizeof(int)*bArr->C);
    }
    while(str[ptr] && sscanf(str+ptr,"%d%c %n",&n,&ch,&t))
    {
        int row=ch-97;
        bArr->matrix[row][colIndex[row]++]=n;
        ptr+=t;
    }
    return bArr;

}

int main()
{
    char str[10001];
    scanf("%[^\n]", str);
    boundedArray *bArr = groupIntegersAndFormMatrix(str);
    if(bArr == NULL)
    {
        printf("Matrix is not formed\n");
    }
    if(bArr->R <= 0 || bArr->C <= 0)
    {
        printf("Invalid size for the matrix\n");
    }
    printf("%d %d\n", bArr->R, bArr->C);
    for(int row = 0; row < bArr->R; row++)
    {
        for(int col = 0; col < bArr->C; col++)
        {
            printf("%d ", bArr->matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}
