/*
The function/method generateRegNum accepts four arguments year, section, N and D. The first argument year represents the batch of a class. The second argument section 
represents the section of the class. The third argument N represents the number of students in the class. The four argument D represents an integer value.

The function/method generateRegNum must generate the registration number for each student in the class based on the following condition.
- Each registration number has three parts P1, P2, and P3, where P1 = year, P2 = section, P3 = numbers from 1 to N in D digits.
Then the function must return a string containing the N registration numbers separated by a space.

Note: The value of D is always greater than or equal to the number of digits in N.

Your task is to implement the function generateRegNum so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Boundary Condition(s):
1000 <= year <= 9999
1 <= N <= 10^4
1 <= D <= 5

Example Input/Output 1:
Input:
2021 C 5 3

Output:
2021C001 2021C002 2021C003 2021C004 2021C005

Explanation:
Year = 2021, Section = C, Number of students = 5 and D = 3.
So the registration numbers of the 5 students in the class are generated as given below.
2021C001
2021C002
2021C003
2021C004
2021C005

Example Input/Output 2:
Input:
1995 A 6 2

Output:
1995A01 1995A02 1995A03 1995A04 1995A05 1995A06
*/
#include <stdio.h>
#include <stdlib.h>

char* generateRegNum(int year, char section, int N, int D)
{
    static char s[1000001];
    int p=0;
    for(int i=1;i<=N;i++)
    {
        int t=sprintf(s+p,"%d%c%0*d ",year,section,D,i);
        p+=t;
    }
    return s;
}

int main()
{
    int year, N, D;
    char section;
    scanf("%d %c %d %d", &year, &section, &N, &D);
    char *str = generateRegNum(year, section, N, D);
    if(str == NULL)
    {
        printf("String is not formed\n");
    }
    if(str[0] == '\0' || str[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
    return 0;
}
