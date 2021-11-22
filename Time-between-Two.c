/*
The program must accept the starting time and the ending time in 24Hrs format hh:mm:ss as the input. The program must print the time of each second from the starting time to the 
ending time as the output. 
  
Boundary Condtion(s): 
1 <= hh <= 24
0 <= mm, ss <= 59 
Starting time <= Ending time 

Example Input/Output:
Input:
11:59:55 
12:00:05 

Output:
11:59:55
11:59:56
11:59:57
11:59:58
11:59:59
12:00:00
12:00:01
12:00:02
12:00:03
12:00:04
12:00:05
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int sh,sm,ss,eh,em,es;
    scanf("%d:%d:%d\n%d:%d:%d",&sh,&sm,&ss,&eh,&em,&es);
    while (!(sh==eh && sm==em && ss==es))
    {
        printf("%02d:%02d:%02d\n",sh,sm,ss);
        ss+=1;
        if (ss==60)
        {
            ss=0;
            sm+=1;
            if (sm==60)
            {
                sm=0;
                sh+=1;
                if (sh==24)
                    sh=0;
            }
        }
    }
    printf("%02d:%02d:%02d",eh,em,es);

}
