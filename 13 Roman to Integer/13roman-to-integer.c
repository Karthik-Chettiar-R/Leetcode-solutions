#include<string.h>
int getPower(char p)
{
    if(p=='I')
    {
        return 1;
    }
    else if(p=='V')
    {
        return 5;
    }
    else if(p=='X')
    {
        return 10;
    }
     else if(p=='L')
    {
        return 50;
    }
     else if(p=='C')
    {
        return 100;
    }
        
 else if(p=='D')
    {
        return 500;
    }
       else if(p=='M')
    {
        return 1000;
    }
    return 0;
}
int romanToInt(char* s) {
    int arabic=0;
   for(int i=0;i<strlen(s);i++)
   {
    if(i!=strlen(s)-1&&getPower(s[i])<getPower(s[i+1]))
    {
        arabic-=getPower(s[i]);
    }
    else
    {
        arabic+=getPower(s[i]);
    }
   }
   return arabic;
}
