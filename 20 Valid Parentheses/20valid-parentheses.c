#include<string.h>
bool isValid(char* s) {

char stack[strlen(s)];
int top=-1;
if(strlen(s)==0||strlen(s)==1)
{
    return false;
}
if(s[0]==')'||s[0]==']'||s[0]=='}')
return false;
for(int i=0;i<strlen(s);i++)
{
    if(s[i]=='('||s[i]=='['||s[i]=='{')
    {
        top++;
        stack[top]=s[i];
    }
    else if(s[i]==')')
    {
        if(top==-1||stack[top]!='(')
        return false;
        else {
            top--;
            
        }
    }
    else if(s[i]==']')
    {
        if(top==-1||stack[top]!='[')
        return false;
        else 
        top--;
    }
    else if(s[i]=='}')
    {
        if(top==-1||stack[top]!='{')
        return false;
        else
        top--;
    }
}
if(top!=-1)
{
    return false;
}  
return true; 
}