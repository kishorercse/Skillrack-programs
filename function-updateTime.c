/*
The function/method updateTime accepts two arguments time and str. The first argument time represents a time in 24-hour format (HH:MM:SS). The string str contains an integer X
that ends with a letter denoting the unit of time (h or H - hours, m or M - minutes, s or S - seconds).

The function/method updateTime must update the time by adding X (hours or minutes or seconds).

Your task is to implement the function updateTime so that the program runs successfully.

The following structure is used to represent the Time and is already defined in the default code (Do not write this definition again in your code).
struct Time
{
    int hours;
    int minutes;
    int seconds;
};

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
10:45:20
50s

Output:
10:46:10

Explanation:
Here X = 50 seconds.
After adding 50 seconds, the time becomes 10:46:10.

Example Input/Output 2:
Input:
15:30:55
125M

Output:
17:35:55

Explanation:
Here X = 125 minutes.
After adding 125 minutes, the time becomes 17:35:55.

Example Input/Output 3:
Input:
23:50:47
2h

Output:
01:50:47
*/
#include <stdio.h>
#include <stdlib.h>

struct Time
{
    int hours;
    int minutes;
    int seconds;
};
void updateTime(struct Time *time, char *str)
{
    int len=strlen(str)-1;
    char ch=tolower(str[len]);
    int x;
    sscanf(str,"%d",&x);
    if (ch=='s')
        time->seconds+=x;
    else if(ch=='m')
        time->minutes+=x;
    else
        time->hours+=x;
    time->minutes+=time->seconds/60;
    time->seconds%=60;
    time->hours+=time->minutes/60;
    time->minutes%=60;
    time->hours%=24;
}
int main()
{
    char str[11];
    struct Time time;
    scanf("%d:%d:%d\n", &time.hours, &time.minutes, &time.seconds);
    scanf("%s", str);
    updateTime(&time, str);
    printf("%02d:%02d:%02d", time.hours, time.minutes, time.seconds);
    return 0;
}
