"""
The program must accept two integer matrices M1 and M2 are of the same size R*C as the input. The program must swap the integers in the same positions between the given two matrices only if their unit digits are equal. Finally, the program must print the modified two matrices as the output. Boundary Condition(s): 2 <= R, C <= 25 Input Format: The first line contains R and C separated by a space. The next R lines, each contains C integers representing the matrix M1. The next R lines from the (R+2)th line, each contains C integers representing the matrix M2. Output Format: The first R lines, each contains C integers representing the modified matrix M1. The next R lines, each contains C integers representing the modified matrix M2. Example Input/Output 1: Input: 3 4 452 345 355 836 654 899 959 963 582 879 408 18 932 447 598 110 851 222 979 813 807 738 78 438 Output: 932 345 355 836 654 899 979 813 582 879 78 438 452 447 598 110 851 222 959 963 807 738 408 18 Explanation: The integers swapped in the matrix M1 are highlighted below. 932 345 355 836 654 899 979 813 582 879 78 438 The integers swapped in the matrix M2 are highlighted below. 452 447 598 110 851 222 959 963 807 738 408 18 Example Input/Output 2: Input: 3 2 679 655 203 526 918 172 309 455 673 876 198 863 Output: 309 455 673 876 198 172 679 655 203 526 918 863 Max Execution Time Limit: 50 millisecs Ambiance Python3 (3.x ) Python3 (3.x ) Reset Great! Your code has passed. SUCCESS Save & Show Next Program Custom test case (Click to toggle)
"""
r,c=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(r)]
b=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if a[i][j]%10==b[i][j]%10:
            a[i][j],b[i][j]=b[i][j],a[i][j]
for i in a:
    print(*i)
for i in b:
    print(*i)
