/*
You must implement the function mergeSorted which accepts two integer arrays arr1 and arr2 and their sizes SIZE1 and SIZE2 respectively as the input. The program must merge the
two integer arrays in descending order. Finally, the program must print the merged integers as the output. 

Boundary Condition(s): 
1 <= SIZE1, SIZE2 <= 100 
1 <= Each integer value <= 10^4 

Input Format: 
The first line contains SIZE1. 
The second line contains SIZE2. 
The third line contains SIZE1 number of integers separated by a space. 
The fourth line contains SIZE2 number of integers separated by a space.

Output Format: 
The first line contains SIZE1 + SIZE2 sort integers separated by space. 

Example Input/Output 1: 
Input: 
3 
5 
13 45 50 
12 15 17 25 26

Output: 
50 45 26 25 17 15 13 12

Example Input/Output 2: 
Input: 
6 
7 
22 34 47 58 69 78
56 62 72 88 92 132 346 

Output: 
346 132 92 88 78 72 69 62 58 56 47 34 22
*/
void mergeSorted(int arr1[], int arr2[], int SIZE1, int SIZE2)
{
    SIZE1--;
    SIZE2--;
    while(SIZE1>=0 && SIZE2>=0){
        if(arr1[SIZE1]>=arr2[SIZE2])
            printf("%d ",arr1[SIZE1--]);
        else
            printf("%d ",arr2[SIZE2--]);
    }
    while(SIZE1>=0)
        printf("%d ",arr1[SIZE1--]);
    while(SIZE2>=0)
        printf("%d ",arr2[SIZE2--]);

}
