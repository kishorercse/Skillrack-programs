"""
A farmer has X kilograms of wheat and Y kilograms of corn. He wants to prepare the fodder for cows and goats. The fodder for a cow is made using 2 kilograms of wheat and 1 
kilogram of corn. The fodder for a goat is made using 1 kilogram of wheat and 2 kilograms of corn. The profit from selling each of the fodder is 1 rupee. The program must 
accept the values of X and Y as the input. The program must print the maximum profit the farmer can earn as the output. 

Boundary Condition(s): 
0 <= X, Y <= 10^8 

Input Format: 
The first line contains X and Y separated by a space. 

Output Format:
The first line contains the maximum profit the farmer can earn by selling the fodders.

Example Input/Output 1:
Input:
4 4 

Output: 
2 

Explanation: 
The maximum profit the farmer can earn is 2.
1 cow fodder and 1 goat fodder. 

Example Input/Output 2:
Input:
8 7 

Output:
5

Example Input/Output 3:
Input:
4 10 

Output:
4
"""
x,y=map(int,input().split())
profit=0
while ((x>=1 and y>=2) or (x>=2 and y>=1)):
    if x>y:
        x-=2
        y-=1
        profit+=1
    else:
        x-=1
        y-=2
        profit+=1
print(profit)
