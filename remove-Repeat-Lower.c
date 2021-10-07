/*
The function/method removeUpperRepeatLower accepts an argument str representing a string value.

The function/method removeUpperRepeatLower must form a new string based on the following conditions.
-Whenever an upper case alphaber occurs, repeat(duplicate) the previous alphaber once and then remove the upper case alphabet.
If there is no previous alphabet for an upper case alphabet, then the function must remove that upper case alphabet.
-Whenever a lower case alphabet occurs, keep the alphabet as it is.
Then the function must return the new string. If all the alphabets in the string str are upper case, then the new string will 
be empty and hence the function must return "-1" as a string value. Your task is to implement the function removeUpperRepeatLower 
so that the program runs successfully. 


Example Input/Output 1:
Input: 
GreenApple 

Output:
reennpple

Explanation: 
Here S = "GreenApple".
1st alphabet G: Upper case alphabet. There is no previous alphabet. So G is removed. 
New string will be empty. 

2nd, 3rd, 4th and 5th alphabets are lower case. They are kept as such. 
New string becomes "reen".

6th alphabet A: Upper case alphabet. The previous alphabet is n. So n is repeated. 
New string becomes "reenn". 

7th, 8th, 9th and 10th alphabets are lower case. They are kept as such. 
New string becomes "reennpple".

Hence the output is 
reennpple 

Example Input/Output 2:
Input:
SKILLRACK 

Output: 
-1 

Example Input/Output 3: 
Input:
aBcDeFGH 

Output:
aacceeee
*/
char* removeUpperRepeatLower(char *str)
{
    static char a[1001];
    char t='\0';
    int index=0;
    for(int i=0;str[i];i++){
        if(isupper(str[i])){
            if (i>0 && t)
                a[index++]=t;
        }
        else{
            a[index++]=str[i];
            t=str[i];
        }
    }
    if (index==0)
        return "-1";
    return a;
}
