"""
Given a string S as input which consists only of digits from 0 to 9, print the longest substring such that the sum of the digits in the first half and the second half is the 
same. Print -1 if such a substring does not exist.

Input Format:
The first line contains S

Output Format:
The first line contains the longest substring as per the rules defined above or -1.

Boundary Conditions:
1 <= Length of S <= 100

Example Input/Output 1:
Input:
123123

Output:
123123

Explanation:
The first half is 123 and the second half is 123. Hence the sum of the digits is equal.

Example Input/Output 2:
Input:
1538024

Output:
5380

Explanation:
The first half is 53 and the second half is 80. The sum of the digits is 8 in both the halves.

Example Input/Output 3:
Input:
12345

Output:
-1

Example Input/Output 4:
Input:
989898989

Output:
98989898

Explanation:
Here both 98989898 and 89898989 are of same length. But due to order of occurrence 98989898 is printed as the output.
"""
s=list(map(int,input()))
l=len(s)
t=[0,s[0]]
maxLen=start=end=-1
for i in range(1,l):
    a=t[-1]+s[i]
    t.append(a)
    for j in range(i+1):
        h=a-t[j]
        d=i-j+1
        p=2*d
        if j-d>=0 and p>maxLen and h==t[j]-t[j-d]:
            maxLen=p
            start=j-d
            end=i
            break
if maxLen==-1:
    print(-1)
else:
    print(*s[start:end+1],sep='')
