"""
The program must accept N integers representing the sizes of N videos (in MB) as the input. A boy wants to store all the N videos in a single pendrive. The pendrives are 
available in sizes of 2^K (where K >= 0). The program must print the minimum size of pendrive (in MB) required to store all the N videos as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Size of each video(in MB) <= 10^6

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the sizes of the N videos (in MB).

Output Format:
The first line contains an integer representing the minimum size of pendrive (in MB) required to store all the N videos.

Example Input/Output 1:
Input:
7
51 64 80 54 43 27 89

Output:
512

Explanation:
Total size of the 7 videos = 51 + 64 + 80 + 54 + 43 + 27 + 89 = 408.
Since the pendrives are available in powers of 2, the minimum size of the pendrive required is 512.
Hence 512 is printed as the output.

Example Input/Output 2:
Input:
6
2 3 5 9 8 9

Output:
64
"""
from math import log2,ceil
n=int(input())
s=sum(map(int,input().split()))
k=log2(s)/log2(2)
print(2**ceil(k))
