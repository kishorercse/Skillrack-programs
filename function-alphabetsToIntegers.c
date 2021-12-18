/*
The function/method alphabetsToIntegers accepts an argument str. The string str contains only alphabets(a - j) and minus symbol(-). The alphabets from a to j indicate the
digits from 0 to 9 respectively. The minus symbol(-) indicates the sign of an integer.

The function/method alphabetsToIntegers must form integers from the given alphabets and return the resulting integers as an array.

Your task is to implement the function alphabetsToIntegers so that it passes all the test cases.

The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
bc dff eaaj -hi

Output:
12 355 4009 -78

Explanation:
bc -> 12
dff -> 355
eaaj -> 4009
-hi -> -78

Example Input/Output 2:
Input:
-aaae -gab ajai

Output:
-4 -601 908
*/
