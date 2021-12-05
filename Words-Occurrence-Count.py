"""
The program must accept N string values containing only lower case alphabets as the input. The program must sort the words based on their occurrence count in descending
order and the words that are occurring in the same number of times must be sorted alphabetically as the output.

Boundary Condition(s):
1 <= N <= 50
1 <= Length of each string <= 1000

Input Format:
The first line contains N.
The next N lines each contain a space separated string.

Output Format:
The lines contain string value(s) based on the given conditions.

Example Input/Output 1:
Input:
2
squirrel lion dog cat
lion dog dog cat

Output:
dog
cat
lion
squirrel

Explanation:
The occurrence count of the string squirrel is 1.
The occurrence count of the string lion is 2.
The occurrence count of the string dog is 3.
The occurrence count of the string cat is 2.
After sorting those string values based on the given conditions, the string values becomes
dog
cat
lion
squirrel

Example Input/Output 2:
Input:
4
hello good morning
hi good afternoon
see you good night we will meet tomorrow morning
have a good day

Output:
good
morning
a
afternoon
day
have
hello
hi
meet
night
see
tomorrow
we
will
you

Example Input/Output 3:
Input:
5
peacock dove sparrow owl ostrich
peacock sparrow
sparrow owl ostrich ostrich owl ostrich
owl
ostrich

Output:
ostrich
owl
sparrow
peacock
dove
"""
n=int(input())
d={}
for _ in range(n):
    for i in input().split():
        d[i]=d.get(i,0)+1
d=sorted(d.items(),key=lambda x:(-x[1],x[0]))
for i in d:
    print(i[0])
