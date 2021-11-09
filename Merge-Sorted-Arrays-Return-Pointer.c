/*
You must implement the function mergeSorted which accepts two integer arrays arr1 and arr2 and their sizes SIZE1 and SIZE2 respectively as the input. The function must merge the 
two sorted arrays in ascending order and store them a new array. Finally, the function must return the new array.
Note: Do not define the main function. 

Boundary Condition(s):
1 <= SIZE1, SIZE2 <=100 
1 <= Each integer value <= 10^5 

Input Format: 
The first line contains the two integers SIZE1, SIZE2 separated by a space. 
The second line contains the SIZE1 number of integers separated by space(s). 
The third line contains the SIZE2 number of integers separated by space(s). 

Output Format:
The first line contains the SIZE1+SIZE2 sorted integers separated by a space. 

Example Input/Output 1: 
Input: 
5 5
10 20 30 40 50 
15 25 35 45 55

Output: 
10 15 20 25 30 35 40 45 50 55

Example Input/Output 2: 
Input: 
6 7 
22 34 47 58 69 78
56 62 72 88 92 132 346 

Output: 
22 34 47 56 58 62 69 72 78 88 92 132 346
*/
int* mergeSorted(int arr1[], int arr2[], int SIZE1, int SIZE2)
{
    int i=0, j=0, index=0, *mergedArr=(int*)malloc(sizeof(int)*(SIZE1+SIZE2));
    while(i<SIZE1 && j<SIZE2)
    {
        if (arr1[i]<=arr2[j])
            mergedArr[index++]=arr1[i++];
        else
            mergedArr[index++]=arr2[j++];
    }
    
    while (i<SIZE1)
        mergedArr[index++]=arr1[i++];
        
    while (j<SIZE2)
        mergedArr[index++]=arr2[j++];
        
    return mergedArr;

}
