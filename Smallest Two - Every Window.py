"""
The program must accept N integers and an integer K as the input. The program must print the smallest two integers(in descending order) in each window of size K among the N integers as the output. Boundary Condition(s): 2 <= K <= N <= 1000 1 <= Each integer value <= 10^5 Input Format: The first line contains N and K separated by a space. The second line contains N integers separated by a space. Output Format: The first (N-K+1) lines, each contains two integers representing the smallest two integers in a window of size K among the N integers. Example Input/Output 1: Input: 6 3 3 53 45 97 84 20 Output: 45 3 53 45 84 45 84 20 Explanation: Here N=6 and K=3. There are four windows of size 3. 1st Window: 3 53 45 The smallest two values are 45 3. 2nd Window: 53 45 97 The smallest two values are 53 45. 3rd Window: 45 97 84 The smallest two values are 84 45. 4th Window: 97 84 20 The smallest two values are 84 20. Hence the output is 45 3 53 45 84 45 84 20 Example Input/Output 2: Input: 7 5 47 51 60 32 64 50 41 Output: 47 32 50 32 41 32
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n-k+1):
    print(*sorted(l[i:i+k])[1::-1])
