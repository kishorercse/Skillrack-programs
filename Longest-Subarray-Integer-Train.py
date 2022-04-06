"""
The program must accept N integers as the input. The program must print the sum of the integers in the longest subarray of minimum size 2 where the first digit of
each integer(except the first integer) is equal to the last digit of the previous integer. If two or more such longest subarrays occur, then the program must consider
the subarray which gives the maximum sum. If there is no such subarray, then the program must print the maximum integer among the given N integers as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains an integer representing the sum of integers in the longest subarray based on the given conditions.

Example Input/Output 1:
Input:
8
67 12 24 49 901 54 48 806

Output:
986

Explanation:
The longest subarray where the first digit of each integer(except the first integer) is equal to the last digit of the previous integer is given below.
12, 24, 49 and 901.
The sum of the integers in the longest subarray is 986 (12 + 24 + 49 + 901).
Hence the output is 986.

Example Input/Output 2:
Input:
10
24 48 86 60 41 100 66 61 18 82

Output:
227

Example Input/Output 3:
Input:
5
12 45 990 23 405

Output:
990
"""
