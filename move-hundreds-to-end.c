/*

Move Hundreds to End: Fill in the missing lines of code to implement the method (function) moveHundreds(int array[], int size) so that the method moves all the integer values with 100 to the end of the array. The order of the remaining integers must be maintained.

Boundary Condition(s):
1 <= N <= 1000

Example Input/Output 1:
Input:
6
12 100 45 8 100 25

Output:
12 45 8 25 100 100

Explanation:
There are two integer values as 100 which are moved to the end.
The remaining integers 12 45 8 25 are printed in the same order as given in the input.

Example Input/Output 2:
Input:
8
100 100 65 100 14 100 100 56

Output:
65 14 56 100 100 100 100 100
*/
void moveHundreds(int array[], int size)
{
    int index=0;
    for(int i=0;i<size;i++){
        if(array[i]!=100){
            int temp=array[i];
            array[i]=array[index];
            array[index]=temp;
            index++;
        }
    }
}
