"""
There are four products A, B, C and D in a shop. The price of the four products are given below.
A - Rs.40 each or Rs.100 for a pack of 4
B - Rs.60 each
C - Rs.55 each or Rs.200 for a pack of 6
D - Rs.95 each
The program must accept a string S representing the products in a cart. The program must print the total price for the entire cart based on the given price list.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the total price for the entire cart based on the given price list.

Example Input/Output 1:
Input:
ABACDBAAA

Output:
410

Explanation:
A - quantity 5 - (100 + 40)
B - quantity 2 - (60 + 60)
C - quantity 1 - 55
D - quantity 1 - 95
Total price - 410

Example Input/Output 2:
Input:
CACCCDAADCCCCCCCBC

Output:
770
"""
s=input().strip()
count={'A':0,'B':0,'C':0,'D':0}
for i in s:
    count[i]+=1
print(count['A']//4 * 100 + count['A']%4 * 40 + count['B']*60 + count['C']//6 * 200 + count['C']%6*55 + count['D']*95)
