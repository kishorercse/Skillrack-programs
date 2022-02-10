"""
The program must accept an array of N even integers as the input. The program must print the output based on the following conditions.
- For each integer in the array, the program must divide the integer by 2. Then the program must print the integers in the revised array. Then the program must remove all the 
odd integers in the revised array(if present).
- Then the program must repeat the above process on the revised array till the size of the array becomes 0.

Boundary Condition(s):
1 <= N <= 100
2 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The lines contain the integer values separated by a space based on the given conditions.

Example Input/Output 1:
Input:
4
32 60 8 200

Output:
16 30 4 100
8 15 2 50
4 1 25
2
1

Explanation:
Here N = 4, and the four even integers are 32, 60, 8 and 200.
[32, 60, 8, 200] -> [16, 30, 4, 100] (No odd integers obtained).
[16, 30, 4, 100] -> [8, 15, 2, 50] (15 is the only odd integer to be removed).
[8, 2, 50] -> [4, 1, 25] (1 and 25 are the two odd integers to be removed).
[4] -> [2] (No odd integers obtained).
[2] -> [1] (1 is the only odd integer to be removed).
[] -> Now the size of array becomes 0.

Example Input/Output 2:
Input:
5
90 40 80 52 64

Output:
45 20 40 26 32
10 20 13 16
5 10 8
5 4
2
1
"""
n=int(input())
l=list(map(int,input().split()))
count=0
while count<n:
    for i in range(n):
        if l[i]!=-1:
            l[i]//=2
            print(l[i],end=' ')
            if l[i]%2!=0:
                l[i]=-1
                count+=1
    print()
