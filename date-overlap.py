"""
The program must accept two date ranges as the input. The program must print YES if the date ranges are overlapping. Else the program must print NO as the output.

Input Format:
The first line contains the start date of the first date range.
The second line contains the end date of the first date range.
The third line contains the start date of the second date range.
The fourth line contains the end date of the second date range.

Output Format:
The first line contains either ‘YES’ or ‘NO’.

Example Input/Output:
Input:
20160302
20160402
20160303
20160304

Output:
YES
"""
a=int(input().strip())
b=int(input().strip())
x=int(input().strip())
y=int(input().strip())
if x<=a<=y or x<=b<=y or a<=x<=b or a<=y<=b:
    print('YES')
else:
    print('NO')
