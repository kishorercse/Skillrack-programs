/*Moozak the mouse has been placed in the top left corner of a maze. There is a huge chunk of cheese somewhere in the maze which is represented by 9. The maze is represented as a matrix of integers, where 0 denotes a wall, 1 denotes a path and 9 represents the huge chunk of cheese.

Fill in the lines of code for the method isPath to determine if Moozak can reach the huge chunk of cheese. The method should return 1 if there is a path from Moozak (top left corner) to the cheese. The method isPath must return 0 if there is no path. Moozak cannot climb the walls or go out of the maze but can go left, right, up or down.

Input Format:
The first 8 lines contains 8 integer values (one among 0, 1 or 9) separated by a space.

Output Format:
The first line contains either 1 or 0.

Example Input/Output 1:
Input:
1 0 1 1 1 0 0 1
1 0 0 0 1 1 1 1
1 0 0 0 0 0 0 0
1 0 1 0 9 0 1 1
1 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 1

Output:
1

Explanation:
The path to cheese is mentioned using *

* 0 1 1 1 0 0 1
* 0 0 0 1 1 1 1
* 0 0 0 0 0 0 0
* 0 1 0 9 0 1 1
* 1 1 0 * 0 0 1
* 0 1 0 * * 0 1
* 0 0 0 0 * 0 1
* * * * * * 1 1

Example Input/Output 2:
Input:
1 0 9 1 0 0 0 1
1 0 0 0 1 1 1 1
1 0 0 0 0 0 0 0
1 0 1 0 0 0 1 1
1 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 1

Output:
0
*/
int check(int maze[8][8],int i,int j)
{
    if (maze[i][j]==9)
        return 1;
    if (maze[i][j]==1){
        maze[i][j]=-1; // -1 indicates that the element at i,j is already checked
        if (i+1<8 && check(maze,i+1,j))
            return 1;
        if (i-1>=0 && check(maze,i-1,j))
            return 1;
        if (j-1>=0 && check(maze,i,j-1))
            return 1;
        if (j+1<8 && check(maze,i,j+1))
            return 1;
    }
    return 0;
}
int isPath(int maze[8][8])
{
    return check(maze,0,0);
}
int main(){
  int maze[8][8];
  for(int i=0;i<8;i++){
    for(int j=0;j<8;j++){
      scanf("%d",maze[i][j]);
    }
  }
  isPath(maze);
}
