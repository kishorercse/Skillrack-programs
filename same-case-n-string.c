/*
The program must accept N string values of equal size as the input. The program must print the count of position of the string where all the characters are lowercase
or all the characters are uppercase at that position.

Boundary Condition(s): 
1 <= N <= 1000 
1 <= Length of string <= 1000 

Input Format: 
The first line contains T which represents the number of test cases. 
Each test case consist of the following. 
The first line contains N. 
The next N lines contain N string values. 

Output Format:
The first N lines contains the count of positions for each test case as per the above condition. 

Example Input/Output 1: 
Input: 
2
3
tram 
BeLt
mark
5
Maker 
CHart
Cloth
BricK
DRink 

Output:
2 
3

Explanation: 
For the first testcase, all the characters in the 2nd and 4th column are lowercase. Hence 2 is printed. 
For the second testcase, all the characters in the 1st position are in uppercase. All the characters in the 3rd and 4th positions are in lowercase. Hence 3 is printed. 

Example Input/Output 2: 
Input: 
3
4
sBsiypcy
gcfabuEl
qoqBrwlv
qBnAcvnE 
6
aKixymgh
uLCrudkD
bChAqftx
aKnqtjwj 
BDEwDvok
vGnaAytf 
3
EutvW 
EdBmC 
EDgEQ 

Output:
4
3
2
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int t;
    scanf("%d",&t);
    while(t-- > 0){
        int n;
        scanf("%d",&n);
        char arr[n][1001];
        for(int i=0;i<n;i++)
            scanf("%s",arr[i]);
        int len=strlen(arr[0]), count=0;
        for(int i=0;i<len;i++){
            int islow=islower(arr[0][i]);
            int flag=1;
            for(int j=1;j<n;j++){
                if(islower(arr[j][i])!=islow){
                    flag=0;
                    break;
                }
            }
            if (flag==1)
                count++;
        }
        printf("%d\n",count);
    }

}
