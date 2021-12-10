"""
The program must accept an array of N unique integers and an integer K as the input. The value of N is always divisible by K. The program must split the given array into N/K 
subarrays of equal size K. Then the program must sort the subarrays based on the first integer. Finally, the program must print the revised array as the output.

Boundary Condition(s):
1 <= K <= N <= 1000
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains the revised N integers separated by a space.

Example Input/Output 1:
Input:
9
30 38 33 50 55 59 10 15 12
3

Output:
10 15 12 30 38 33 50 55 59

Explanation:
Here N = 9 and K = 3.
1st subarray: 30 38 33
2nd subarray: 50 55 59
3rd subarray: 10 15 12
After sorting the 3 subarrays based on the first integer, the array becomes
10 15 12 30 38 33 50 55 59

Example Input/Output 2:
Input:
8
3 4 7 6 2 9 5 1
2

Output:
2 9 3 4 5 1 7 6

Explanation:
Here N = 8 and K = 2.
1st subarray: 3 4
2nd subarray: 7 6
3rd subarray: 2 9
4th subarray: 5 1
After sorting the 4 subarrays based on the first integer, the array becomes
2 9 3 4 5 1 7 6
"""
n=int(input())
l=list(map(int,input().split()))
k=int(input())
l=sorted([l[i:i+k] for i in range(0,n,k)],key=lambda x:x[0])
for i in l:
    print(*i,end=' ')
