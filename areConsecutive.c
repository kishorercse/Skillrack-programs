/*
The function/method areConsecutive accepts an argument str. The string str contains only digits.

The function/method areConsecutive must return 1 if the given string represents the concatenation of two consecutive integers. Else the function must return 0.

Your task is to implement the function areConsecutive so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
256257

Output:
1

Explanation:
Here the given string is 256257.
The two integers in the string are 256 and 257 which are consecutive.
So 1 is printed as the output.

Example Input/Output 2:
Input:
4241

Output:
1

Example Input/Output 3:
Input:
99100

Output:
1

Example Input/Output 4:
Input:
20412024

Output:
0
*/
int strToInteger(char *str, int a, int b)
{
    int n=0;
    for(int i=a;i<b;i++)
    {
        n=n*10+(str[i]-'0');
    }
    return n;
}
int areConsecutive(char *str)
{
    int len=strlen(str), a,b;
    if (str[len/2]!='0')
    {
        a=strToInteger(str,0,len/2), b=strToInteger(str,len/2,len);
        if (abs(a-b)==1)
            return 1;
    }
    if (len%2!=0)
    {
        if (str[len/2+1]!='0')
        {
            a=strToInteger(str,0,len/2+1); 
            b=strToInteger(str,len/2+1,len);
            if (abs(a-b)==1)
                return 1;
        }
    }
    return 0;
    

}
