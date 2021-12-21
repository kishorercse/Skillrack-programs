/*
There are N boxes containing gold coins and silver coins. The number of gold coins and the number of silver coins in each box are passed as the input. The program must print 
the total number of gold coins and silver coins in the N boxes as the output. Please fill in the missing lines of code to define the function getBoxes so that the program runs
successfully.

Input Format:
The first line contains N.
The next N lines, each contains two integers separated by a space representing the number of gold coins and the number of silver coins in a box.

Output Format:
The first line contains two integers separated by a space representing the total number of gold coins and silver coins in the N boxes.

Example Input/Output 1:
Input:
3
10 25
20 6
25 4

Output:
55 35

Example Input/Output 2:
Input:
4
10 5
20 5
15 100
15 200

Output:
60 310
*/
#include <iostream>
using namespace std;

class Box
{
    int goldCoins;
    int silverCoins;
public:
    Box(int gCoins, int sCoins)
    {
        goldCoins = gCoins;
        silverCoins = sCoins;
    }
    int getGoldCoinsCount()
    {
        return goldCoins;
    }
    int getSilverCoinsCount()
    {
        return silverCoins;
    }
}; // End of Box class

Box **getBoxes(int n)
{
    Box **arr=(Box**)malloc(sizeof(Box)*n);
    int x,y;
    for(int i=0;i<n;i++)
    {
        cin >> x >> y;
        arr[i]=new Box(x,y);
    }
    return arr;
}
int main()
{
    int N;
    cin >> N;
    Box** box = getBoxes(N);
    int totalGoldCoins = 0, totalSilverCoins = 0;
    for(int index = 0; index < N; index++)
    {
        totalGoldCoins += box[index]->getGoldCoinsCount();
        totalSilverCoins += box[index]->getSilverCoinsCount();
    }
    cout << totalGoldCoins << " " << totalSilverCoins;
    return 0;
} // End of main function
