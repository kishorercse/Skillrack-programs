"""
Given N positive integers, find the maximum sum S that can be obtained by adding exactly M out of the N integers. The program must print the value of the maximum sum S.

Input Format:
The first line will contain N and M separated by a space.
The second line will contain the values of N positive integers separated by a space.

Output Format:
First line will contain S.

Boundary Conditions:
3 <= N <= 100
2 <= M <= N

Example Input/Output 1:
Input:
5 2
9 2 1 5 4

Output:
14

Explanation:
Out of the five given numbers, the sum of 9+5 = 14 is the largest sum and hence printed as the output.

Example Input/Output 2:
Input:
100 12
133 29 706 22 174 296 582 909 691 76 684 29 666 383 737 988 217 646 276 751 195 31 338 258 528 889 112 976 96 399 81 519 1 645 950 637 795 442 368 534 602 308 566 254 195 380 841 413 541 109 618 365 719 49 772 458 336 798 81 406 223 155 240 202 712 254 118 743 715 891 483 256 676 139 178 446 480 263 597 686 213 232 233 592 310 649 939 973 39 931 321 344 802 869 98 222 976 757 560 28

Output:
11132

Explanation:
Out of the 100 given numbers, the sum of the combination of the following 12 numbers - 909 988 889 976 950 841 891 939 973 931 869 976 is the largest.
"""
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
print(sum(l[-m:]))
