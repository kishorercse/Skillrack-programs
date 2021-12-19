/*
The function/method alphabetsToIntegers accepts an argument str. The string str contains only alphabets(a - j) and minus symbol(-). The alphabets from a to j indicate the
digits from 0 to 9 respectively. The minus symbol(-) indicates the sign of an integer.

The function/method alphabetsToIntegers must form integers from the given alphabets and return the resulting integers as an array.

Your task is to implement the function alphabetsToIntegers so that it passes all the test cases.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
bc dff eaaj -hi

Output:
12 355 4009 -78

Explanation:
bc -> 12
dff -> 355
eaaj -> 4009
-hi -> -78

Example Input/Output 2:
Input:
-aaae -gab ajai

Output:
-4 -601 908
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
boundedArray* alphabetsToIntegers(char *str)
{
    boundedArray *bArr=malloc(sizeof(boundedArray));
    bArr->arr=malloc(sizeof(int)*100);
    bArr->SIZE=0;
    bArr->arr[0]=0;
    int neg=0;
    for(int i=0;str[i];i++)
    {
        if (str[i]=='-')
        {
            neg=1;
            continue;
        }
        if (str[i]==' ')
        {
            if (neg==1)
                bArr->arr[bArr->SIZE]*=-1;
            bArr->SIZE++;
            bArr->arr[bArr->SIZE]=0;
            neg=0;
            continue;
        }
        bArr->arr[bArr->SIZE]=bArr->arr[bArr->SIZE]*10+(str[i]-'a');
    }
    if(neg==1)
        bArr->arr[bArr->SIZE]*=-1;
    bArr->SIZE++;
    return bArr;
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    boundedArray *bArr = alphabetsToIntegers(str);
    if(bArr == NULL)
    {
        printf("Array is not formed\n");
    }
    if(bArr->SIZE <= 0)
    {
        printf("Invalid size for the array\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
