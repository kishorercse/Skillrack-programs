"""
A person receives N messages in his messenger app. The messenger app shows the contacts and their last message in reverse chronological order based on the time of the last
received message. The person receives N messages. The names of the senders and their messages are passed as the input to the program in chronological order. The program must 
print the names of the contacts who sent the messages to the person and their last message in the order as in the messenger app.

Boundary Condition(s):
2 <= N <= 100
3 <= Length of each line (name and message) <= 100

Input Format:
The first line contains N.
The next N lines, each contains the name of the sender and his/her message separated by a colon.

Output Format:
The lines contain the names of the contacts and their last message in the order as in the messenger app.

Example Input/Output 1:
Input:
8
Hector:Hi
Arun:Good Morning
Hector:How are you?
John:r u there?
Arun:Have a good day.
John:Pls call me
John:Urgent
Arun:Where are you?

Output:
Arun:Where are you?
John:Urgent
Hector:How are you?

Explanation:
The person receives the messages from three different persons(Hector, Arun and John).
Hector's last message is "How are you?".
Arun's last message is "Where are you?".
John's last message is "Urgent".
So their names and their last message are printed in reverse chronological order.

Example Input/Output 2:
Input:
7
Rachel:hi
Rachel:how are you?
Anitha:ok
Babloo:Hmm
Jhanvi:100 times sorry!
Babloo:ok, good night
Anitha:thanks

Output:
Anitha:thanks
Babloo:ok, good night
Jhanvi:100 times sorry!
Rachel:how are you?
"""
n=int(input())
d={}
pos={}
for i in range(n):
    s,m=input().split(':')
    pos[s]=i
    d[s]=m
l=sorted(d,key=lambda x:-pos[x])
for i in l:
    print(i,d[i],sep=':')
