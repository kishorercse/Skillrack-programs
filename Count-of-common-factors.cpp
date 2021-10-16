/*
Given a set of numbers where all other numbers are multiple of smallest number, the program must find the count of the common factor C excluding 1.

Example 1:
Input:
2
100
75

Output:
2

Explanation: The common factors excluding 1 are 5,25. Hence output is 2.

Example 2:
Input:
3
10
20
30

Output:
3

Explanation:
The common factors excluding 1 are 2,5,10. Hence output is 3.
*/
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int n,min=9999999;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
        if (arr[i]<min)
            min=arr[i];
    }
    int f=2,count=0;
    while(f<=min){
        int t=n;
        for(int i=0;i<n;i++){
            if (arr[i]%f==0)
                t--;
        }
        count+=(t==0);
        f+=1;
    }
    cout << count;

}
