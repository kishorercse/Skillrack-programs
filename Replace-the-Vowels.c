/*
The program must accept two string values S1 and S2 as the input. For each vowel CH in the string S1, the program must replace CH by the vowel in the string S2 in the order
of their occurrence. If there is no vowel in the string S2 then replace all the vowels by 'a'. If the vowels in the string S2 is not sufficient then consider last occurred 
vowel as the replacement vowel. Finally, the program must print the modified string S1 as the output.
Note: S1 and S2 contain only lower case alphabets.

Boundary Condition(s):
1 <= Length of S1, S2 <= 100

Input Format:
The first line contains the string S1.
The second line contains the string S2.

Output Format:
The first line contains the modified string S1.

Example Input/Output 1:
Input:
banana
apple

Output:
banene

Explanation:
The 1st vowel in S1 is replaced by the 1st vowel in S2. Now the string S1 is banana.
The 2nd vowel in S1 is replaced by the 2nd vowel in S2. Now the string S1 is banena.
The 3rd vowel in S1 is replaced by the 2nd vowel in S2. Now the string S1 is banene.
Hence the output is banene

Example Input/Output 2:
Input:
abcdedfghijkl
wxyz

Output:
abcdadfghajkl
*/
#include<stdio.h>
#include<stdlib.h>

int isvowel(char ch)
{
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    char a[101], b[101], ch='a';
    scanf("%s %s",a,b);
    for(int i=0, j=0;a[i];i++)
    {
        if (isvowel(a[i]))
        {
            while(b[j]!='\0' && !isvowel(b[j]))
                j++;
            if (b[j]!='\0')
                ch=b[j++];
           a[i]=ch;
        }
    }
    printf("%s",a);
}
