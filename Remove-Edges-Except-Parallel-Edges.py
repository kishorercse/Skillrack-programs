"""
There are N nodes in a directed graph. The program must accept the adjacency matrix of the directed graph as the input. If there are two edges between the two nodes, then the
edges are called parallel edges. The program must remove all the edges other than the parallel edges in the graph. Then the program must print the revised adjacency matrix of
the graph as the output.

Note: The value 0 in the matrix indicates that there is no edge between the two nodes.

Boundary Condition(s):
2 <= N <= 50
0 <= Matrix element value <= 1000

Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.

Output Format:
The first N lines contain the revised adjacency matrix of the graph.

Example Input/Output 1:
Input:
5
0 9 5 0 0
0 0 0 8 2
2 0 0 0 0
0 3 7 0 1
0 4 0 6 0

Output:
0 0 5 0 0
0 0 0 8 2
2 0 0 0 0
0 3 0 0 1
0 4 0 6 0

Explanation:
There are 5 nodes in the directed graph.
The parallel edges are present between the nodes 1 and 3.
1 -> 3 = 5
3 -> 1 = 2
The parallel edges are present between the nodes 2 and 4.
2 -> 4 = 8
4 -> 2 = 3
The parallel edges are present between the nodes 2 and 5.
2 -> 5 = 2
5 -> 2 = 4
The parallel edges are present between the nodes 4 and 5.
4 -> 5 = 1
5 -> 4 = 6
So the edges other than the parallel edges are removed from the graph.

Example Input/Output 2:
Input:
5
0 2 0 0 0
4 0 3 0 0
0 0 0 0 9
0 5 0 0 6
0 0 0 3 0

Output:
0 2 0 0 0
4 0 0 0 0
0 0 0 0 0
0 0 0 0 6
0 0 0 3 0
"""
n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
res=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if m[i][j]!=0 and m[j][i]!=0:
            res[i][j]=m[i][j]
            res[j][i]=m[j][i]
    print(*res[i])
