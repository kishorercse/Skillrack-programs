"""
There is a per store in a city where dogs can be kept when their owners go for a long tour out of the city or the owners travel abroad. The cage in the pet store can accommodate
two dogs. But certain dogs are very aggressive and must be kept along in a cage and hence cannot be put in the cage along with another dog. Given the number of dogs N and 
assuming that a given dog can be either aggressive or passive, the program must print the number of combinations in which can they be put in the cages (Assume the number of 
cages is always greater than N and hence there is no shortage of cages).

Input Format:
The first line contains N.

Output Format:
The first line contains the number of combinations in which the dogs can be put in the cages.

Boundary Conditions:
1 <= N <= 999

Example Input/Output 1:
Input:
4

Output:
10

Explanation:
4 dogs can be arranged in 10 combinations as shown below. The numbers inside parentheses indicates that the dogs are put in the same cage.
1 2 3 4
(1 2) 3 4
(1 2) (3 4)
(1 3) 2 4
(1 3) (2 4)
(1 4) 2 3
(1 4) (2 3)
1 (2 3) 4
1 3 (2 4)
1 2 (3 4)
Please note that 1 (2 3) 4 is same as 1 4 (2 3) or 4 (2 3) 1 or 4 (3 2) 1.
"""
n=int(input())
if n<=2:
    print(n)
else:
    a,b=1,2
    for i in range(2,n):
        c=a*i+b
        a=b
        b=c
    print(c)
