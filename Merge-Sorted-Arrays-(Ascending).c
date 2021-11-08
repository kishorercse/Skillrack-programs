/*
You must implement the function mergeSorted which accepts two integer arrays arr1 and arr2 and their sizes SIZE1 and SIZE2 respectively as the input. The program must merge the 
two integer arrays in ascending order. Finally, the program must print the merged integers as the output. 

Boundary Condition(s): 
1 <= SIZE1,SIZE2 <= 100 
1 <= Each integer value <= 10^5 

Input Format: 
The first line contains SIZE1. 
The second line contains SIZE2.
The third line contains SIZE1 number of integers separated by a space. 
The fourth line contains SIZE2 number of integers separated by a space. 

Output Format:
The first line contains SIZE1 + SIZE2 sorted integers separated by a space.

Example Input/Output 1: 
Input: 
10
5
12 13 16 23 27 28 31 38 50 78
15 25 33 48 69

Output: 
12 13 15 16 23 25 27 28 31 33 38 48 50 69 78 

Example Input/Output 2: 
Input: 
7 
7 
31 53 70 79 90 91 93
15 39 50 63 77 92 97 

Output: 
15 31 39 50 53 63 70 77 79 90 91 92 93 97
*/
void mergeSorted(int arr1[], int arr2[], int SIZE1, int SIZE2)
{
    int i=0, j=0;
    while (i<SIZE1 && j<SIZE2)
    {
        if (arr1[i]<=arr2[j])
            printf("%d ",arr1[i++]);
        else
            printf("%d ",arr2[j++]);
    }
    
    while(i<SIZE1)
        printf("%d ", arr1[i++]);
        
    while(j<SIZE2)
        printf("%d ",arr2[j++]);
}
