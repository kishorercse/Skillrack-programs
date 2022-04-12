/*
The function/method sortIntegersInplace accepts an argument str. The string str contains words and integers.

The function/method sortIntegersInplace must sort the integers in the string str among their positions. Then the function must return the revised string as a new 
string.

Your task is to implement the function sortIntegersInplace so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
skillrack 50 20 code 105 how are 40 you 30

Output:
skillrack 20 30 code 40 how are 50 you 105

Explanation:
The integers in the given string are 50, 20, 105, 40 and 30.
After sorting the integers in their positions, the string becomes
skillrack 20 30 code 40 how are 50 you 105

Example Input/Output 2:
Input:
135 cat 9841 dog rat 12 987 cow

Output:
12 cat 135 dog rat 987 9841 cow
*/
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int cmpfunc(const void *a, const void *b)
{
    return (*(int*)a-*(int*)b);
}
char* sortIntegersInplace(char *str)
{
    char a[50][20], temp[10];
    int arr[50], i=0;
    int ind=0,ptr=0,t;
    static char res[101];
    while(sscanf(str+ptr,"%s %n",a[ind],&t)==1)
    {
        if (isdigit(a[ind][0]))
        {
            sscanf(a[ind],"%d",&arr[i++]);
        }
        ind++;
        ptr+=t;
    }
    qsort(arr,i,sizeof(int),cmpfunc);
    i=0;
    for(int j=0;j<ind;j++)
    {
        if (isdigit(a[j][0]))
        {
            sprintf(temp,"%d ",arr[i++]);
            strcat(res,temp);
        }
        else
        {
            strcat(res,a[j]);
            strcat(res," ");
        }
    }
    return res;

}

int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    char *result = sortIntegersInplace(str);
    if(result == NULL || result == str)
    {
        printf("New string is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}
