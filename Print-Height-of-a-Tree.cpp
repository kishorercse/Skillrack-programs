/*
The program must accept an integer representing the height of a tree as the input. The program must print the height of the tree if the height is a positive value. 
Else the program must print the string value "Height of a tree cannot be negative or zero" as the output. Please fill in the blanks with code so that the program runs
successfully.

Example Input/Output 1:
Input:
45

Output:
45

Example Input/Output 2:
Input:
0

Output:
Height of a tree cannot be negative or zero

Example Input/Output 3:
Input:
-10

Output:
Height of a tree cannot be negative or zero
*/
#include <iostream>
using namespace std;

void printTreeHeight(int height)
{
    if(height<=0)
    {
        throw "Height of a tree cannot be negative or zero";
    }
    cout << height;
}

int main()
{
    int height;
    cin >> height;
    try
    {
        printTreeHeight(height);
    }
    
    catch (const char* msg)
    {
        cout << msg;
    }
    return 0;
}
