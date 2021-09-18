#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int str[105], str2[105], str3[105];
 
int main()
{
    int n, l, t;
    scanf("%d%d%d", &n, &l, &t);
    for (int i = 0; i < n; i++)
        scanf("%d", &str[i]);
    memcpy(str2, str, sizeof(str));
    sort(str2, str2+n);
    for (int i = 0; i < n; i++)
        str3[i] = (str[i]+t)%(2*l)>l ? 2*l-(str[i]+t)%(2*l) : (str[i]+t)%(2*l);
    sort(str3, str3+n);
    for (int i = 0; i < n; i++)
        printf(" %d"+!i, str3[lower_bound(str2, str2+n, str[i])-str2]);
    return 0;
}