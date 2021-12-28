"""
The program must accept an array of integers with some pairs of square brackets as the input. The integers between the open and close square brackets represent a subarray. The
program must reverse all such subarrays in the given array. Then the program must print the revised array without any square brackets and then the program must print the sum of
integers in the revised array as the output.

Note: The maximum size of the array will be 100.

Boundary Condition(s):
1 <= Each integer value <= 10^5

Input Format:
The first line contains an array of integers with some pairs of square brackets.

Output Format:
The first line contains the integers in the revised array without any square brackets.
The second line contains the sum of integers in the revised array.

Example Input/Output 1:
Input:
10 [20 45 15] 19 [10 30]

Output:
10 15 45 20 19 30 10
149

Explanation:
There are 2 subarrays represented by the pairs of square brackets.
1st subarray: [20 45 15] -> [15 45 20]
2nd subarray: [10 30] -> [30 10]
After reversing the 2 subarrays, the array becomes
10 15 45 20 19 30 10
The sum of integers in the array is 149.

Example Input/Output 2:
Input:
[11 26 17 15] 78 [87 95 51] [33 52 59 28] 16 35 [68]

Output:
15 17 26 11 78 51 95 87 28 59 52 33 16 35 68
671
"""
l=input().split()
n=len(l)
total=0
i=0
while i<n:
    if l[i][0]=='[':
        if l[i][-1]==']':
            total+=int(l[i][1:-1])
            print(l[i][1:-1],end=' ')
            i+=1
            continue
        l[i]=int(l[i][1:])
        total+=l[i]
        j=i+1
        t=[l[i]]
        while j<n:
            if l[j][-1]==']':
                total+=int(l[j][:-1])
                t.insert(0,l[j][:-1])
                break
            t.insert(0,l[j])
            total+=int(l[j])
            j+=1
        i=j+1
        print(*t,end=' ')
    else:
        total+=int(l[i])
        print(l[i],end=' ')
        i+=1
print("\n",total)
