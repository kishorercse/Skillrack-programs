"""
The program must accept a list of N integers and an integer T as the input. The program must remove T unit digits in the given list of integers based on the following conditions.
- The program must start removing the unit digits from the 1st integer.
- If the removed unit digit is even, then the program must remove the unit digit of the next integer. Else the program must remove the unit digit of the previous integer.
- Similarly, the program must remove T unit digits in the given list of integers.
- Once all the digits in an integer are removed, then the integer itself must be removed from the given list.
- Consider the given list of integers in circular fashion when finding the previous and next integers.
Finally, the program must print the sum S of the modified integers in the list as the output. If all integers are removed, then the program must print -1 as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^8
1 <= T <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains T.

Output Format:
The first line contains S or -1.

Example Input/Output 1:
Input:
4
87369 4012 22312 39845
6

Output:
3903

Explanation:
Here N = 4 and T = 6.
t = 1 -> 8736 4012 22312 39845 (The unit digit of the 1st integer is removed).
t = 2 -> 8736 4012 22312 3984 (The unit digit of the 4th integer is removed).
t = 3 -> 8736 4012 2231 3984 (The unit digit of the 3rd integer is removed).
t = 4 -> 8736 4012 2231 398 (The unit digit of the 4th integer is removed).
t = 5 -> 873 4012 2231 398 (The unit digit of the 1st integer is removed).
t = 6 -> 873 401 2231 398 (The unit digit of the 2nd integer is removed).
Now the sum of the modified integers is 3903 (873 + 401 + 2231 + 398).
So 3903 is printed as the output.

Example Input/Output 2:
Input:
4
22 44 33 55
7

Output:
5

Explanation:
Here N = 4 and T = 7.
t = 1 -> 2 44 33 55
t = 2 -> 2 4 33 55
t = 3 -> 2 4 3 55
t = 4 -> 2 X 3 55 (X indicates the integer to be removed)
t = 5 -> 2 X 55 (X indicates the integer to be removed)
t = 6 -> X 55 (X indicates the integer to be removed)
t = 7 -> 5
Hence 5 is printed as the output.

Example Input/Output 3:
Input:
3
123 456 789
9

Output:
-1
"""
n=int(input())
l=list(map(int,input().split()))
t=int(input())
ind=0
c=0
for _ in range(t):
    unit=l[ind]%10
    l[ind]=l[ind]//10
    if l[ind]==0:
        c+=1
        if c==n:
            print(-1)
            break
    if unit%2==0:
        ind=(ind+1)%n
        while l[ind]==0:
            ind=(ind+1)%n
    else:
        ind=(ind-1)%n
        while l[ind]==0:
            ind=(ind-1)%n
else:
    print(sum(l))
