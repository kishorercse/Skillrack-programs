/*

*/
void printKrepeatingChar(char *str, int K)
{
    char ch=str[0];
    int l=strlen(str),count=1;
    for(int i=1;i<l;i++){
        if(ch!=str[i]){
            if (count>=K)
                printf("%c",ch);
            ch=str[i];
            count=1;
        }
        else
            count+=1;
    }
    if (count>=K)
        printf("%c",ch);

}
