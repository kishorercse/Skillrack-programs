/*
You must implement the function shiftToLeft(char str[], int K) which accepts a string S and an integer K (where K is always less than the length of S) as the input. The function
must shift all the characters for K times towards the left in the string S. 

Example Input/Output 1: 
Input: 
skillrack 
3 

Output: 
llrack 

Explanation: 
After shifting all the characters for 3 times towards the left in the string "skillrack", the string becomes "llrack".
Hence the output is llrack 

Example Input/Output 2: 
Input: 
performance 
10 

Output: 
e
*/
void shiftToLeft(char str[], int K)
{
    int i=0;
    for(i=0;str[K]!='\0';i++)
    {
        str[i]=str[K++];
    }
    str[i]='\0';
}
