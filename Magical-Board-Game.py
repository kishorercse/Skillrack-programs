"""
In a magical board, there are R red coins and B black coins. There are two magnets on the board that pull the coins towards them. One magnet is present on the top of the board 
that will pull only red coins column wise. The other magnet is present in the right side of the board that will pull only black coins row wise. Only one magnet can pull coins 
at a time. At any point of time, the coin cannot move outside the board. If there is no coin in the next cell when moving towards up or right, then the coins can move without
any change. But if there are X coins in the next cell, the coins will change the color based on the following conditions.
- If X is greater than the number of coins to be added (i.e., If X is greater than the number of coins in the current cell), then all coins will be the same color as in the next 
cell. 
- If X is less than the number of coins to be added, then all coins will be the same color as in the current cell.
- If X is equal to the number of coins to be added, then compare the color in the current cell and the next cell, if both are same then the coins can move without any change in 
color. Else all the coins will become red color. So both red and black coins can not be present in the same cell. Every second, all the coins move towards up or right 
simultaneously by exactly 1 cell. The program must accept the size of the board MxN and the positions of the R red coins, B black coins as the input. The program must print the 
number of coins in each cell and its color (R or B) after T seconds as the output. 

Note: The magnet on the top of the board always starts to pull first.

Boundary Condition(s): 
2 <= M, N <= 20 
1 <= R+B <= M*N 
1 <= T <= 50 

Input Format:
The first line contains M and N separated by a space. 
The second line contains R.
The next R lines from the 3rd line, each containing two integers representing the positions of a red coin.
The (R+3)rd line contains B.
The next B lines from the (R+4)th line, each containing two integers representing the positions of a B black coins.
The (R+B+4)th line contains T.

Output Format:
The first M lines containing the number of coins in each cell and its color (R or B) after T seconds.

Example Input/Output 1: 
Input: 
8 8
7 
1 1
2 1
3 1
4 1
8 1
4 4
6 2
6 
5 1
6 1
7 1
5 2
5 3
4 5
5

Output: 
4R 0 0 1R 0 0 0 0
0 0 0 0 0 0 0 0 
0 3R 0 0 0 0 0 0 
0 0 0 0 0 0 1B 0
2R 0 0 0 1B 0 0 0
0 0 1B 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 

Explanation:
The number of coins in each cell and its color (R or B) in the given board is 
1R 0 0 0 0 0 0 0 
1R 0 0 0 0 0 0 0 
1R 0 0 0 0 0 0 0
1R 0 0 1R 1B 0 0 0
1B 1B 1B 0 0 0 0 0 
1B 1R 0 0 0 0 0 0
1B 0 0 0 0 0 0 0
1R 0 0 0 0 0 0 0 

After 1 second, the board becomes 2R 0 0 0 0 0 0 0 1R 0 0 0 0 0 0 0 1R 0 0 1R 0 0 0 0 0 0 0 0 1B 0 0 0 1B 2R 1B 0 0 0 0 0 1B 0 0 0 0 0 0 0 2R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 After 2 seconds, the board becomes 2R 0 0 0 0 0 0 0 1R 0 0 0 0 0 0 0 1R 0 0 1R 0 0 0 0 0 0 0 0 0 1B 0 0 0 3R 0 1B 0 0 0 0 0 1B 0 0 0 0 0 0 2R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 After 3 seconds, the board becomes 3R 0 0 0 0 0 0 0 1R 0 0 1R 0 0 0 0 0 0 0 0 0 0 0 0 0 3R 0 0 0 1B 0 0 0 0 0 1B 0 0 0 0 2R 1B 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 After 4 seconds, the board becomes 3R 0 0 0 0 0 0 0 1R 0 0 1R 0 0 0 0 0 0 0 0 0 0 0 0 0 3R 0 0 0 0 1B 0 0 0 0 0 1B 0 0 0 2R 0 1B 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 After 5 seconds, the board becomes 4R 0 0 1R 0 0 0 0 0 0 0 0 0 0 0 0 0 3R 0 0 0 0 0 0 0 0 0 0 0 0 1B 0 2R 0 0 0 1B 0 0 0 0 0 1B 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Example Input/Output 2: Input: 4 5 6 4 1 3 2 3 1 1 1 2 1 3 5 10 2 2 4 4 2 4 1 5 2 5 1 4 4 3 4 5 1 3 2 3 3 Output: 3R 2R 0 1B 5R 1R 0 0 1B 0 0 0 0 0 0 0 0 0 1B 2B
"""
