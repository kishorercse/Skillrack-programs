/*
The function/method validateDate accepts an argument dateStr representing a string value which contains a date in the format "DD-MM-YYYY".

The function/method validateDate must return 1 if the given date is valid. Else the function must return 0.

Your task is to implement the function validateDate so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
26-08-2021

Output:
1

Example Input/Output 2:
Input:
09-15-2010

Output:
0

Explanation:
Invalid month 15.

Example Input/Output 3:
Input:
39-12-2100

Output:
0

Explanation:
Invalid date 39 in December.

Example Input/Output 4:
Input:
29-02-2021

Output:
0

Explanation:
Invalid date 29 in February (2021 is not a leap year).
*/
#include <stdio.h>
#include <stdlib.h>

int validateDate(char *dateStr)
{
    int dd=(dateStr[0]-'0')*10+(dateStr[1]-'0'), mm=(dateStr[3]-'0')*10+(dateStr[4]-'0'), yyyy=(dateStr[6]-'0')*1000+(dateStr[7]-'0')*100+(dateStr[8]-'0')*10+(dateStr[9]-'0');
    int months[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    if ((yyyy%4==0 && yyyy%100!=0) || (yyyy%400==0))
        months[2]=29;
    if (dd>0 && dd<=months[mm] && mm>0 && mm<=12)
        return 1;
    return 0;
}

int main()
{
    char dateStr[11];
    scanf("%s", dateStr);
    printf("%d", validateDate(dateStr));
    return 0;
}
