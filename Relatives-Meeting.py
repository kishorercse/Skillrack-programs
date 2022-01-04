"""
There is a village festival happening in which several group of relatives meet every year. Each person is allocated an identifier which is a positive integer.
N pairs of relatives identifiers are passed as input. Then finally given a person's identifier I, the program must print the count of the relatives C  in the group of the person
with the identifier I.

Input Format:
The first line contains the values of N.
N lines contain the identifiers of two persons who are related.
The next line (N+2)th line, will contain the identifier I of the person for whom the relative count of his group is to be printed.

Output Format:
The first line will contain the count of relatives C in the group of the person with identifier I.

Boundary Conditions:
1 <= N <= 10000
1 <= I <= 1000000

Example Input/Output 1:
Input:
5
10 20
30 20
40 10
55 35
55 22
40

Output:
4

Explanation:
10, 20, 30, 40 form a relative group.
55, 35, 22 form another relative group.
So the count of relatives for the person with identifier 40 is 4.
"""
