"""
There are N products in a shop. Each product has a name, weight and price. The name, weight and price of each product are passed as the input. The program must print the count 
of unique products in the shop as the output. The duplicate products contain identical values for all three fields (name, weight and price).

Boundary Condition(s):
1 <= N <= 50
1 <= Length of each product's name <= 10
1 <= Weight of each product <= 1000
1 <= Price of each product <= 1000

Input Format:
The first line contains N.
The second line contains the names of the N products separated by a space.
The third line contains the weights of the N products separated by a space.
The fourth line contains the prices of the N products separated by a space.

Output Format:
The first line contains an integer value representing the count of unique products in the shop.

Example Input/Output 1:
Input:
5
Wheat Rice Sugar Rice Rice
10 25 5 25 25
500 750 800 900 750

Output:
4

Explanation:
2nd and 5th products are duplicates.
2nd Product: Rice 25 750
5th Product: Rice 25 750
So the count of unique products is 4, which is printed as the output.

Example Input/Output 2:
Input:
6
Salt Salt Salt Salt Salt Salt
1 1 2 2 3 3
10 15 10 15 10 15

Output:
6

Example Input/Output 3:
Input:
3
Rice Rice Rice
5 5 5
400 400 400

Output:
1
"""
n=int(input())
s=set()
m=[input().split() for _ in range(3)]
for j in range(n):
    t=""
    for i in range(3):
        t+=m[i][j]
    s.add(t)
print(len(s))
