#include <stdio.h>
#include <stdlib.h>

static float power(int a, int b)
{
    float temp;
    if(!b)return 1;
    temp=power(a,b/2);
    if(b%2==0)return temp*temp;
    else
    {
        if(b>0)return temp*temp*a;
        else return temp*temp/a;
    }
}
int main()
{
    printf("%d^%d = %.2f",3,4,power(2,-2));
    return 0;
}
