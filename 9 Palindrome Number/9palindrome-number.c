#include<string.h>
bool isPalindrome(int x) {
int pal=0,y=x;
if(x<0||x%10==0&&x!=0)
{
    return false;
}

while(x>pal)
{pal=pal*10+x%10;
x=x/10;
}
if(x==pal||x==pal/10)
{
    return true;}
else return false;
}