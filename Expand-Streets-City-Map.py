"""
The program must accept a matrix of size R*C representing the map of a city and an integer K as the input. The hash symbols (#) in the columns represent the buildings and
the pipe symbols (|) in the columns represent the streets. The program must set the gap between buildings as K units by widening the streets. Finally, the program must print
the matrix representing the revised city map.
Note: In the given city map, there are no streets more than 1 unit wide.

Boundary Condition(s):
2 <= R, C <= 50
2 <= K <= 20

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters representing the city map.
The R+2nd line contains K.

Output Format:
The first R lines contain the matrix representing the revised city map.

Example Input/Output 1:
Input:
5 11
###|#|##|##
###|#|##|##
###|#|##|##
###|#|##|##
###|#|##|##
3

Output:
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##

Explanation:
Here R=5, C=11 and K=3.
The below 5*11 matrix represents the map of the city.
###|#|##|##
###|#|##|##
###|#|##|##
###|#|##|##
###|#|##|##
After widening the streets as 3 units, the city map becomes
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##
###|||#|||##|||##

Example Input/Output 2:
Input:
6 12
#|#|####|#|#
#|#|####|#|#
#|#|####|#|#
#|#|####|#|#
#|#|####|#|#
#|#|####|#|#
2

Output:
#||#||####||#||#
#||#||####||#||#
#||#||####||#||#
#||#||####||#||#
#||#||####||#||#
#||#||####||#||#
"""
r,c=map(int,input().split())
m=[input().strip() for _ in range(r)]
k='|'*int(input())
for i in range(r):
    for j in range(c):
        if m[i][j]=='|':
            print(k,end='')
        else:
            print(m[i][j],end='')
    print()
