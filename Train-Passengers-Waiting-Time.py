"""
The program must accept the departure time of a train (in 24-hr format HH:MM) at a station S as the input. The name and the arrival time (in 24-hr format HH:MM) of 
N persons to the station S are also passed as the input to the program. The program must print the name of each person and his/her waiting time (in minutes) at the 
station S as the output. If a person arrives at the station after the train departs, then the program must print the name of the person followed by -1 as the output.

Boundary Condition(s):
1 <= N <= 50
1 <= Length of each person's name <= 15

Input Format:
The first line contains the departure of a train.
The second line contains N.
The next N lines, each contains the name of a person and the arrival time to the station separated by a space.

Output Format:
The first N lines, each contains the name of a person followed by his/her waiting time at the station S or -1 based on the given conditions.

Example Input/Output 1:
Input:
10:53
7
Rajesh 09:15
Catherine 10:05
Anu 10:17
Pravin 09:52
Deepa 10:53
Mambo 10:33
Anita 11:00

Output:
Rajesh 98
Catherine 48
Anu 36
Pravin 61
Deepa -1
Mambo 20
Anita -1

Explanation:
The departure time of the train is 10:53.
The value of N is 7.
Rajesh 98: Rajesh arrives at the station at 09:15. His waiting time in the station is 98 minutes.
Catherine 48: Catherine arrives at the station at 10:05. Her waiting time in the station is 48 minutes.
Anu 36: Anu arrives at the station at 10:17. Her waiting time in the station is 36 minutes.
Pravin 61: Pravin arrives at the station at 09:52. His waiting time in the station is 61 minutes.
Deepa -1: Deepa arrives at the station at 10:53 which is after the train departs.
Mambo 20: Mambo arrives at the station at 10:33. His waiting time in the station is 20 minutes.
Anita -1: Anita arrives at the station at 11:00 which is after the train departs.

Example Input/Output 2:
Input:
16:25
6
Ramesh 16:30
Jhanvi 16:11
Bhuvana 16:25
Kavin 16:24
Anu 16:18
Hector 16:29

Output:
Ramesh -1
Jhanvi 14
Bhuvana -1
Kavin 1
Anu 7
Hector -1
"""
def minutes(l):
    return l[0]*60+l[1]
d=minutes(list(map(int,input().split(":"))))
n=int(input())
for _ in range(n):
    s,a=input().split()
    a=minutes(list(map(int,a.split(":"))))
    if d>a:
        print(s,d-a)
    else:
        print(s,-1)
