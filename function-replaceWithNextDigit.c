/*
The function/method replaceWithNextDigit accepts an argument N representing an integer value.

The function/method replaceWithNextDigit must print the output based on the following conditions.
- For each digit D in the integer N, the program must form a new integer by replacing the digit with its next digit (for the digit 9, consider 0 as the next digit).
- Then the program must print the resulting integers in sorted order.

Your task is to implement the function replaceWithNextDigit so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
12543

Output:
12544 12553 12643 13543 22543

Explanation:
For the 1st digit: 12543 -> 22543
For the 2nd digit: 12543 -> 13543
For the 3rd digit: 12543 -> 12643
For the 4th digit: 12543 -> 12553
For the 5th digit: 12543 -> 12544
So the resulting 5 integers are printed in sorted order.
12544 12553 12643 13543 22543

Example Input/Output 2:
Input:
860679

Output:
860670 860689 860779 861679 870679 960679

Example Input/Output 3:
Input:
999

Output:
99 909 990
*/
#include <stdio.h>
#include <stdlib.h>

void replaceWithNextDigit(int N)
{
    char str[10];
    sprintf(str,"%d",N);
    int len=strlen(str), arr[len], index=0;
    for(int i=len-1;i>=0;i--)
    {
        if (str[i]=='9')
        {
            str[i]='0';
        }
        else
        {
            str[i]++;
        }
        sscanf(str,"%d",&arr[index++]);
        if (str[i]=='0')
        {
            str[i]='9';
        }
        else
        {
            str[i]--;
        }
    }
    for(int i=0;i<len-1;i++)
    {
        for(int j=0;j<len-i-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(int i=0;i<len;i++)
    {
        printf("%d ",arr[i]);
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    replaceWithNextDigit(N);
    return 0;
}
