"""
The program must accept N lines as the input, which represents a bar graph pattern. The N lines in the bar graph pattern are numbered from 1 to N (bottom to top). Each column 
of the bar graph pattern contains exactly one vertical bar and the bar is denoted by consecutive hash symbols. The program must print the range(from and to positions) of each
vertical bar in the given bar graph pattern as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Number of columns in the bar graph pattern <= 50

Input Format:
The first line contains N.
The next N lines contain the bar graph pattern.

Output Format:
The lines, each contains two integers separated by a space representing the range of a vertical bar.

Example Input/Output 1:
Input:
6
****#***#**
***##**#*#*
#*###*##*#*
#*##*###**#
####*##***#
##*#*#****#

Output:
1 4
1 2
2 4
1 5
4 6
1 3
2 4
3 5
6 6
4 5
1 3

Explanation:
Here N = 6 and the number of columns in the graph is 11.
1st bar = 1 4
2nd bar = 1 2
3rd bar = 2 4
4th bar = 1 5
5th bar = 4 6
6th bar = 1 3
7th bar = 2 4
8th bar = 3 5
9th bar = 6 6
10th bar = 4 5
11th bar = 1 3

Example Input/Output 2:
Input:
5
#***#**
#**#*#*
#*#**#*
**#***#
*#****#

Output:
3 5
1 1
2 3
4 4
5 5
3 4
1 2
"""
n=int(input())
m=[input().strip() for _ in range(n)]
c=len(m[0])
for j in range(c):
    a=-1
    for i in range(n):
        if m[i][j]=='#':
            b=i
            if a==-1:
                a=i
    print(n-b,n-a)
