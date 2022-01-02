"""
An array of N numbers is passed as the input. The program must sort the odd numbers and even numbers separately in ascending order. The odd and even numbers must 
retain their original odd even slots in the input.

Input Format:
The first line contains N indicating the count of numbers in the array.
The second line contains the N array elements separated by a space.

Output Format:
The first line contains the N sorted array elements separated by a space.

Boundary Conditions:
2 <= N <= 100

Example Input/Output 1:
Input:
9
169 181 298 16 147 263 102 155 141

Output:
141 147 16 102 155 169 298 181 263
"""
n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
evenN=oddN=0
for i in range(n):
    if l[i]%2==0:
        even.append(i)
        evenN+=1
    else:
        odd.append(i)
        oddN+=1
for i in range(evenN-1):
    for j in range(evenN-i-1):
        if l[even[j]]>l[even[j+1]]:
            l[even[j]],l[even[j+1]]=l[even[j+1]],l[even[j]]
for i in range(oddN-1):
    for j in range(oddN-i-1):
        if l[odd[j]]>l[odd[j+1]]:
            l[odd[j]],l[odd[j+1]]=l[odd[j+1]],l[odd[j]]
print(*l)
