/*
The function/method printEveryRowCharacters accepts three arguments R, C and matrix. The integers R and C represents the size of the character matrix. The function/method 
printEveryRowCharacters must print the characters of the matrix based on the following conditions. - In the 1st row, the function must print every character. - In the 2nd 
row, the function must print every 2nd character. - In the 3rd row, the function must print every 3rd character. - Similarly, the characters in the remaining rows of the
matrix must be printed.
Your task is to implement the function printEveryRowCharacters so that the program runs successfully. 
Example Input/Output 1:
Input: 
7 9 
f n m d h b o c r
i o u m g x y u m
t o g m n p e y w
o p j a g g k s i
x y z q x a b s w
p o r e i c a r b
c z c b e l u m f

Output: 
f n m d h b o c r o m x u g p w a s x c u

Explanation: 
1st row: Every character -> f n m d h b o c r 
2nd row: Every 2nd character -> o m x u 
3rd row: Every 3rd character -> g p w 
4th row: Every 4th character -> a s 
5th row: Every 5th character -> x 
6th row: Every 6th character -> c 
7th row: Every 7th character -> u 

Example Input/Output 2: 
Input: 
5 5 
a b c d e 
f g h i j 
k l m n o 
p q r s t 
u v w x y 

Output: 
a b c d e g i m s y 

Example Input/Output 3: 
Input: 
5 3 
v e s 
f k w
u e q
q m r
g p l

Output: 
v e s k q 
*/
#include <stdio.h> 
#include <stdlib.h> 
void printEveryRowCharacters(int R, int C, char *matrix)
{
  for(int i=0;i<R;i++)
    {
        for(int j=i;j<C;j+=i+1)
        {
            printf("%c ",matrix[i*C+j]);
        }
    }
} 

int main() 
{ 
  int R, C; 
  scanf("%d %d", &R, &C); 
  char matrix[R][C]; 
  for(int row = 0; row < R; row++)
  {
    for(int col = 0; col < C; col++)
    {
      scanf(" %c", &matrix[row][col]);
    } 
  } 
  printEveryRowCharacters(R, C, matrix); 
  return 0; 
}
