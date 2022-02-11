/*
The program must accept 4 times T1, T2, T3 and T4 in 24-hour format as the input. The program must print the output based on the following conditions.
- The program must print the time T1 in seconds.
- Then the program must print the sum of T1 and T2 in seconds.
- Then the program must print the sum of T1, T2 and T3 in seconds.
- Then the program must print the sum of T1, T2, T3 and T4 in seconds.
Please fill in the missing lines of code so that the program runs successfully.

Example Input/Output 1:
Input:
00:10:00
01:00:15
02:15:30
00:00:50

Output:
600
4215
12345
12395

Explanation:
T1 = 00:10:00 = 600 seconds.
T2 = 01:00:15 = 3615 seconds.
T3 = 02:15:30 = 8130 seconds.
T4 = 00:00:50 = 50 seconds.
T1 in seconds = 600.
T1 + T2 in seconds = 600+3615 = 4215.
T1 + T2 + T3 in seconds = 600+3615+8130 = 12345.
T1 + T2 + T3 + T4 in seconds = 600+3615+8130+50 = 12395.

Example Input/Output 2:
Input:
00:00:01
01:00:00
12:59:59
00:01:00

Output:
1
3601
50400
50460
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

typedef struct time
{
    int hours, minutes, seconds;
} Time;

void printTimeInSeconds(int n, ...)
{
    va_list valist;
    int totalSeconds=0;
    va_start(valist,n);
    for(int i=0;i<n;i++)
    {
        Time temp=va_arg(valist,Time);
        totalSeconds+=temp.hours*3600+temp.minutes*60+temp.seconds;
    }
    va_end(valist);
    printf("%d\n",totalSeconds);
}

int main()
{
    Time time1, time2, time3, time4;
    scanf("%d:%d:%d", &time1.hours, &time1.minutes, &time1.seconds);
    scanf("%d:%d:%d", &time2.hours, &time2.minutes, &time2.seconds);
    scanf("%d:%d:%d", &time3.hours, &time3.minutes, &time3.seconds);
    scanf("%d:%d:%d", &time4.hours, &time4.minutes, &time4.seconds);
    printTimeInSeconds(1, time1);
    printTimeInSeconds(2, time1, time2);
    printTimeInSeconds(3, time1, time2, time3);
    printTimeInSeconds(4, time1, time2, time3, time4);
    return 0;
}
