#include<string.h>
char* longestCommonPrefix(char** strs, int strsSize) {
    int i;
    char* result=malloc(201*sizeof(char));
    if(strsSize==0)
    {
        return "";
    }
    if(strsSize==1)
    {strcpy(result,strs[0]);
        return result;
    }
    for(int k=0;k<strsSize;k++)
    {
        if(strs[k][0]=='\0')
        return "";
    }
for(i=0;strs[0][i]!='\0';i++)
{char ref=strs[0][i];

    for(int j=1;j<strsSize;j++)
    {
if(ref!=strs[j][i]||strs[j][i]=='\0')
{
result[i]='\0';
return result;
}

    }
    result[i]=ref;
    
} result[i]='\0';
    return result;
}