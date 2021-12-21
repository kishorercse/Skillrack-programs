/*
The program accepts N integers and a string S. The program prints the N integers in reverse order and the characters of S in reverse order. Please fill in the blanks with code
so that the program runs successfully.

Example Input/Output 1:
Input:
5
10 20 30 40 50
skillrack

Output:
50 40 30 20 10
k c a r l l i k s

Example Input/Output 2:
Input:
6
1 4 7 2 5 8
pineapple

Output:
8 5 2 7 4 1
e l p p a e n i p
*/
#include <iostream>
using namespace std;

template <typename T>
void printArrayInReverse(int N, T *arr)
{
    for(int index = N-1; index >= 0; index--)
    {
        cout << arr[index] << " ";
    }
    cout << endl;
}

int main()
{
    int N;
    cin >> N;
    int intarr[N];
    for(int index = 0; index < N; index++)
    {
        cin >> intarr[index];
    }
    printArrayInReverse(N, intarr);

    string str;
    cin >> str;
    char chararr[str.length()];
    for(int index = 0; index < str.length(); index++)
    {
        chararr[index] = str[index];
    }
    printArrayInReverse(str.length(), chararr);
    return 0;
}
