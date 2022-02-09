"""
The program must accept an integer N, a string S and N integers as the input. The string S contains N words without any space. The N integers represent the length of words in 
the string S. The program must sort the words in the string S based on their length. If two or more words have the same length, then the program must sort those words in the 
order of their occurrence. Finally, the program must print the revised string S as the output.

Boundary Condition(s):
2 <= N <= 100
2 <= Length of S <= 10^4
1 <= Each integer value <= 100

Input Format:
The first line contains N.
The second line contains S.
The third line contains N integers separated by a space.

Output Format:
The first line contains the revised string S.

Example Input/Output 1:
Input:
4
lioncattigerrat
4 3 5 3

Output:
catratliontiger

Explanation:
There are 4 words in the given string.
4 -> lion
3 -> cat
5 -> tiger
3 -> rat
After sorting the words based on their length, the string S becomes
catratliontiger

Example Input/Output 2:
Input:
7
applegrapesmangocuckooPineappleNoodlesPizza
5 6 5 6 9 7 5

Output:
applemangoPizzagrapescuckooNoodlesPineapple
"""
n=int(input())
s=input().strip()
l=list(map(int,input().split()))
res=[]
for i in l:
    res.append(s[:i])
    s=s[i:]
print(*sorted(res,key=lambda x:len(x)),sep='')
