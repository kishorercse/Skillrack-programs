"""
There are N stones arranged as a circle. The weights of the N stones are passed as the input. Initially, two boys B1 and B2 stand on the 1st stone. Every second, boy B1 jumps one 
stone and boy B2 jumps two stones. The program must print the weights of the stones on which the two boys jump till they jump on the same stone. 

Boundary Condition(s): 
3 <= N <= 1000 
1 <= Weight of each stone <= 1000

Input Format:
The first line contains N.
The second line contains N integer values separated by a space representing the weights of N stones.

Output Format: 
The lines, each contains two integer values separated by a space representing the weights of the stones on which the two boys jump.

Example Input/Output 1:
Input: 
5
10 20 30 40 50 

Output:
10 10 
20 30 
30 50 
40 20 
50 40 
10 10 

Explanation:
Here N=5. 
Initially, the two boys stand on the 1st stone. So 10 10 are printed.
After 1 second, B1 jumps to the 2nd stone and B2 jumps to the 3rd stone. So 20 30 are printed.
After 2 seconds, B1 jumps to the 3rd stone and B2 jumps to the 5th stone. So 30 50 are printed.
After 3 seconds, B1 jumps to the 4th stone and B2 jumps to the 2nd stone. So 40 20 are printed.
After 4 seconds, B1 jumps to the 5th stone and B2 jumps to the 4th stone. So 50 40 are printed.
After 5 seconds, B1 jumps to the 1st stone and B2 jumps to the 1st stone. So 10 10 are printed.
Now the two boys reached the same stone, so they stop jumping. 

Example Input/Output 2:
Input:
6
11 22 33 44 55 66

Output: 
11 11
22 33
33 55
44 11
55 33
66 55
11 11
"""
n=int(input())
l=list(map(int,input().split()))
i,j=0,0
while True:
    print(l[i],l[j])
    i=(i+1)%n
    j=(j+2)%n
    if i==j:
        break
print(l[i],l[j])
