/*The program must accept a character matrix of size NxN as the input. For each column in the matrix, the program must bring all the consonants at the top of the column in the same order as in the input. Finally, the program must print the modified matrix as the output.
Boundary Condition(s):
2 <= N <= 100
Input Format:
The first line contains the value of N.
The next N lines each contain N characters separated by a space.
Output Format:
The first N lines each contain N characters of the modified matrix separated by a space.
Example Input/Output 1:
Input:
4
U I c N
a x S b
g a O L
R m L M
Output:
g x c N
R m S b
U I L L
a a O M
Explanation:
The consonants in the matrix are highlighted below. 
U I c N
a x S b 
g a O L 
R m L M 
After bringing the consonants at the top of each column, the matrix is 
g x c N 
R m S b 
U I L L 
a a O M
*/
#include<stdio.h>
#include<stdlib.h>

int isvowel(char ch){
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    int n;
    scanf("%d\n",&n);
    char m[n][n],ans[n][n];
    int t[n];
    memset(t,0,sizeof(int)*n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%c ",&m[i][j]);
            if (!isvowel(m[i][j])){
                ans[t[j]][j]=m[i][j];
                t[j]++;
            }
        }
    }
    for(int j=0;j<n;j++){
        for(int i=0;i<n;i++){
            if (t[j]==n)
                break;
            if (isvowel(m[i][j])){
                ans[t[j]][j]=m[i][j];
                t[j]++;
            }
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%c ",ans[i][j]);
        }
        printf("\n");
    }
}
