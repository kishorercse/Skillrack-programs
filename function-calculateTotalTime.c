/*
The function/method calculateTotalTime accepts an argument str. The string str contains multiple integers separated by a space, where each integer ends with a character
denoting the unit of time.
d indicates days.
h indicates hours.
m indicates minutes.
s indicates seconds.

The function/method calculateTotalTime must return the total time in days, hours, minutes and seconds.

Your task is to implement the function calculateTotalTime so that the program runs successfully.

The following structure is used to represent the Time and is already defined in the default code (Do not write this definition again in your code).
struct Time
{
    int days;
    int hours;
    int minutes;
    int seconds;
};
IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
2h 1d 50m 102s 5d 30s 70m

Output:
6 4 2 12

Explanation:
2h -> 2 hours
1d -> 1 day
50m -> 50 minutes
102s -> 102 seconds
5d -> 5 days
30s -> 30 seconds
70m -> 70 minutes
Total time: 6 days, 4 hours, 2 minutes and 12 seconds.

Example Input/Output 2:
Input:
15d 500s 30h 60s

Output:
16 6 9 20
*/
#include <stdio.h>
#include <stdlib.h>

struct Time
{
    int days;
    int hours;
    int minutes;
    int seconds;
};

struct Time* calculateTotalTime(char *str)
{
    struct Time *t=malloc(sizeof(struct Time));
    t->days=t->hours=t->minutes=t->seconds=0;
    int n=0;
    for(int i=0;str[i];i++)
    {
        if (isdigit(str[i]))
            n=n*10+(str[i]-'0');
        else
        {
            if (str[i]=='d')
                t->days+=n;
            else if (str[i]=='h')
                t->hours+=n;
            else if (str[i]=='m')
                t->minutes+=n;
            else if (str[i]=='s')
                t->seconds+=n;
            n=0;
            i++;
        }
            
    }
    if (t->seconds>=60)
    {
        t->minutes+=t->seconds/60;
        t->seconds%=60;
    }
    if (t->minutes>=60)
    {
        t->hours+=t->minutes/60;
        t->minutes%=60;
    }
    if (t->hours>=24)
    {
        t->days+=t->hours/24;
        t->hours%=24;
    }
    return t;

}

int main()
{
    char str[101];
    scanf("%[^\n]", str);
    struct Time *time = calculateTotalTime(str);
    if(time == NULL)
    {
        printf("Time is not formed\n");
    }
    printf("%d %d %d %d", time->days, time->hours, time->minutes, time->seconds);
    return 0;
}
