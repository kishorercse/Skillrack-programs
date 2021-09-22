/*
Inverse Two Triangle Pattern: Fill in the missing lines of code to implement the method (function) printPattern(int N) so that the method prints the pattern given in the Example Input/Output section.

Boundary Condition(s):
1 <= N <= 1000

Example Input/Output 1:
Input:
5

Output:
54321
4321
321
21
1
12
123
1234
12345

Example Input/Output 2:
Input:
7

Output:
7654321
654321
54321
4321
321
21
1
12
123
1234
12345
123456
1234567
*/
void printPattern(int N)
{
    for(int i=N;i>=1;i--){
        for(int j=i;j>=1;j--){
            printf("%d",j);
        }
        printf("\n");
    }
    for(int i=2;i<=N;i++){
        for(int j=1;j<=i;j++){
            printf("%d",j);
        }
        printf("\n");
    }
}
