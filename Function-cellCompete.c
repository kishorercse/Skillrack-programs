/*
There is a colony of 8 cells arranged in a straight line where each day every cell competes with it's adjacent cells (neighbour). Each day, for each cell, if it's neighbours are 
both active and both inactive, the cell becomes inactive the next day, otherwise it becomes active the next day.

Assumptions: The two cells on the ends have single adjacent cell, so the other adjacent cell can be assumed to be always inactive. Even after updating the cell state. Consider 
it's previous state for updating the state of other cells. Update the cell information of all cells simultaneously. Write a function cellCompete which takes one 8 element array 
of integer’s cells representing the current state of 8 cells and one integer days representing the number of days to simulate. An integer value of 1 represents an active cell 
and value of 0 represents an inactive cell. 

Example Input/Output 1:
Input: 
1 0 0 0 1 0 0 0 
3

Output: 
0 1 0 0 0 1 0 1 

Explanation: 
Day 1: 0 1 0 1 0 1 0 0 
Day 2: 1 0 0 0 0 0 1 0 
Day 3: 0 1 0 0 0 1 0 1 

Example Input/Output 2: 
Input: 
1 0 0 0 0 1 0 0 
1 

Output: 
0 1 0 0 1 0 1 0 

Example Input/Output 3: 
Input:
1 1 1 0 1 1 1 1 
2 

Output:
0 0 0 0 0 1 1 0
*/
void cellCompete(int cells[8], int days)
{
    while (days > 0)
    {
        int prev=0, curr;
        for(int i=0; i<=6; i++)
        {
            curr=cells[i];
            cells[i]=(prev==cells[i+1])?0:1;
            prev=curr;
        }
        cells[7]=prev;
        days-=1;
    }

}
