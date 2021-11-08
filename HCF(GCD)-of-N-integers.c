/*
You must implement the function getHCF(unsigned long long int arr[], int SIZE) which accepts an integer array arr and it's size SIZE as the input. The function must return the 
HCF of all the integers in the array. 

Boundary Condition(s): 
2 <= N <= 100 
1 <= Each integer value <= 10^18 

Input Format: 
The first line contains the value N. 
The second line contains N integers each separated by a space.

Output Format: 
The first line contains the HCF of the N integers. 

Example Input/Output 1: 
Input: 
4 
15 20 30 50 

Output: 
5 

Example Input/Output 2: 
Input: 
5 
14 28 35 70 92 

Output:
1
*/
#include <stdio.h>
unsigned long long int GCD(unsigned long long int a, unsigned long long int b)
{
    return (b==0) ? a : GCD(b,a%b);
}
unsigned long long int getHCF(unsigned long long int arr[], int SIZE)
{
    unsigned long long int hcf=arr[0];
    for(int i=1; i<SIZE; i++)
    {
        hcf=GCD(arr[i],hcf);
        if (hcf==1)
            break;
    }
    return hcf;

}

int main()
{
  int N;
  scanf("%d",&N);
  unsigned long long int arr[N];
  for(int i=0; i<N; i++)
  {
    scanf("%llu",&arr[i]);
  }
  printf("%llu",getHCF(arr, N));
  return 0;
}
