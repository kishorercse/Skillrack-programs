/*
The function/method findBinarySum accepts two arguments N and binValues. The binValues represents a 2-D array of characters denoting the N binary string values.

The function/method findBinarySum must return a string containing the binary sum of the given N binary string values.


Boundary Condition(s):
2 <= N <= 100
1 <= Length of each string <= 100

Example Input/Output 1:
Input:
2
10001
11001

Output:
101010

Explanation:
Here N=2 and the given 2 binary string values are 10001 and 11001.
The sum of two binary string values 10001 and 11001 is 101010.

Example Input/Output 2:
Input:
3
1000
111
100010

Output:
110001
*/
#include <stdio.h>
#include <stdlib.h>

char* findBinarySum(int N, char binValues[N][101])
{
    int index[N], count=0, max=0;
    for(int i=0;i<N;i++)
    {
        int size=strlen(binValues[i]);
        index[i]=size-1;
        max=size>max?size:max;
    }
    static char res[201];
    memset(res,'0',sizeof(char)*(max+1));
    int resInd=0;
    while (count<N)
    {
        int s=0;
        for(int i=0;i<N;i++) 
        {
            if (index[i]>=0)
            {
                s+=(binValues[i][index[i]--]-'0');
                if (index[i]==-1)
                    count++;
            }
        }
        int temp=resInd, val;
        while(s>0)
        {
            val=s%2;
            s/=2;
            if (val==1)
            {
                int t2=temp;
                while(res[t2]=='1')
                {
                    res[t2++]='0';
                }
                res[t2]='1';
            }
            temp++;
        }
        resInd++;
    }
    int a=0,b=strlen(res)-1;
    char tmp;
    while(a<b)
    {
        tmp=res[a];
        res[a]=res[b];
        res[b]=tmp;
        a++;
        b--;
    }
    for(int i=0;i<201;i++)
    if (res[i]!='0')
        return &res[i];
}

int main()
{
    int N;
    scanf("%d", &N);
    char str[N][101];
    for(int index = 0; index < N; index++)
    {
        scanf("%s", str[index]);
    }
    char *binarySum = findBinarySum(N, str);
    if(binarySum == NULL || binarySum == str[0])
    {
        printf("String is not formed\n");
    }
    if(binarySum[0] == '\0' || binarySum[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", binarySum);
    return 0;
}
