"""
The program must accept an array of N unique integers (where N is always odd) and an integer T as the input. The program must modify the array T times based on the following 
conditions.
- Compare the middle three integers (arr[mid-1], arr[mid], arr[mid+1]) and find the minimum value among them. 
- If arr[mid-1] is the minimum integer, then it must be moved to the beginning of the array. 
- If arr[mid+1] is the minimum integer, then it must be moved to the end of the array. 
- If arr[mid] is the minimum integer, then compare the first integer and the last integer in the array, then it must be moved to the side with the minimum value. 
Finally, the program must print the integers in the modified array as the output. 

Boundary Condition(s): 
5 <= N <= 99 
1 <= Each integer value <= 10^8
1 <= T <= 100 

Input Format: 
The first line contains N.
The second line contains N integers separated by a space. 
The third line contains T. 

Output Format:
The first line contains the N integers in the modified array separated by a space.

Example Input/Output 1: 
Input: 
7
15 100 11 48 10 69 42 
4 

Output: 
11 15 100 69 10 48 42 

Explanation: 
Here N = 7 and T = 4. 
For T = 1, 15 100 11 48 10 69 42 -> 15 100 11 48 69 42 10 (Moved to the end) 
For T = 2, 15 100 11 48 69 42 10 -> 11 15 100 48 69 42 10 (Moved to the beginning)
For T = 3, 11 15 100 48 69 42 10 -> 11 15 100 69 42 10 48 (Moved to the end) 
For T = 4, 11 15 100 69 42 10 48 -> 11 15 100 69 10 48 42 (Moved to the end)

Example Input/Output 2:
Input: 
9
17 38 32 59 89 15 14 88 53
3

Output:
59 17 38 32 89 88 53 15 14
"""
n=int(input())
l=list(map(int,input().split()))
t=int(input())
m=n//2
while t>0:
    a=min(l[m-1],l[m],l[m+1])
    b=min(l[0],l[n-1])
    if l[m-1]==a:
        l.insert(0,l.pop(m-1))
    elif l[m+1]==a:
        l.append(l.pop(m+1))
    else:
        b=min(l[0],l[n-1])
        if b==l[0]:
            l.insert(0,l.pop(m))
        else:
            l.append(l.pop(m))
    t-=1
print(*l)
