/*
The function/method encryptMessage accepts two arguments message and key representing two string values. The string message contains only lower case alphabets. The string key
contains only unique lower case alphabets.

The function/method encryptMessage must form a new string by encrypting the given message based on the following conditions.
- All 26 lower case alphabets from a to z must be mapped with the alphabets in the string key.
- If the number of alphabets in the key is less than 26, then the missing lower case alphabets must be added to key in alphabetical order.
- For each alphabet CH in the message, the function must find the alphabet from the key which is mapped to CH and form the encrypted string.
Finally, the function must return the encrypted string.

Your task is to implement the function encryptMessage so that the program runs successfully.

IMPORTANT: Do not write the main() function as it is already defined.

Example Input/Output 1:
Input:
skillrack
master

Output:
pgdhhomsg

Explanation:
Message = "skillrack"
Key = "master"
Here the number of alphabets in the key is less than 26. So the missing lower case alphabets are added in alphabetical order.
abcdefghijklmnopqrstuvwxyz (26 lower case alphabets)
masterbcdfghijklnopquvwxyz (encryption key)
So "skillrack" is encrypted as "pgdhhomsg".

Example Input/Output 2:
Input:
computerscience
abcghimnostuy

Output:
ceyfqphklcohdch
*/
#include <stdio.h>
#include <stdlib.h>

char* encryptMessage(char *message, char *key)
{
    static char result[101];
    int count[26]={0}, ind=strlen(key);
    if (ind<26)
    {
        for(int i=0;key[i];i++)
        {
            count[key[i]-'a']=1;
        }
        for(int i=0;i<26;i++)
        {
            if (count[i]==0)
                key[ind++]=i+'a';
        }
    }
    for(int i=0;message[i];i++)
    {
        result[i]=key[message[i]-'a'];
    }
    return result;
    

}

int main()
{
    char message[101], key[27];
    scanf("%s\n%s", message, key);
    char *encryptedMessage = encryptMessage(message, key);
    if(encryptedMessage == NULL || encryptedMessage == message || encryptedMessage == key)
    {
        printf("New string is not formed\n");
    }
    if(encryptedMessage[0] == ' ' || encryptedMessage[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", encryptedMessage);
    return 0;
}
