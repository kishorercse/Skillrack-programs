/*
Two string values S1 and S2 are passed as input. The program must print the count of common characters in strings S1 and S2. Assume the alphabets in S1 and S2 will be in lower case.

Example 1:

Input:
china
india
Output:
3

Example 2:

Input:
energy
every
Output:
3
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[26]={0},t=0;
    char a[101],b[101];
    scanf("%s\n%s",a,b);
    for(int i=0;a[i]!='\0';i++){
        arr[a[i]-97]=1;
    }
    for(int i=0;b[i]!='\0';i++){
        if (arr[b[i]-97]==1){
            t+=1;
            arr[b[i]-97]=0;
        }
    }
    printf("%d",t);

}
