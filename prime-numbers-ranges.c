/*
The program must accept T pairs of integers as the input. For each pair P (P contains two integers X and Y) among the T pairs, the program must print all 
the prime numbers from X to Y (inclusive) in ascending order as the output. If there is no prime number from X to Y then the program must print -1 for that
pair as the output. 

Boundary Condition(s): 
1 <= T <= 10^4 
1 <= X < Y <= 10^9 

Input Format: 
The first line contains the value of T. 
The next T lines containing a pair of integers separated by a space.

Output Format:
The first T lines containing the prime numbers of each pair separated by a space as per the given conditions. 

Example Input/Output 1:
Input: 
3
10 20
1 15 
32 36

Output: 
11 13 17 19
2 3 5 7 11 13
-1

Explanation:
The first pair is (10, 20). So the prime numbers from 10 to 20 are printed. 
The second pair is (1, 15). So the prime numbers from 1 to 15 are printed. 
The third pair is (32, 36). Here there is no prime number from 32 to 36. So -1 is printed.

Example Input/Output 2:
Input:
6
51 68 
15 75 
21 97
2 55
8 81
80 100

Output:
53 59 61 67 
17 19 23 29 31 37 41 43 47 53 59 61 67 71 73
23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 
11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79
83 89 97
*/
#include<stdio.h>
#include<stdlib.h>

int isprime(int n){
    if (n<=1)
        return 0;
    if (n<=3)
        return 1;
    if (n%2==0 || n%3==0)
        return 0;
    int i=5;
    while(i*i<=n){
        if (n%i==0 || n%(i+2)==0)
            return 0;
        i+=6;
    }
    return 1;
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t-- > 0){
        long long int x,y;
        scanf("%lld %lld",&x,&y);
        int flag=0;
        if (x<=2){
            printf("2 ");
            flag=1;
            x=3;
        }
        else
            x+=(x%2==0);
        while(x<=y){
            if(isprime(x)){
                printf("%d ",x);
                flag=1;
            }
            x+=2;
        }
        if (flag==0)
            printf("-1");
        printf("\n");
    }
    

}
