#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long ll;
ll ans;
int x;
int prime[500010][21],cnt[500010],a[200010],flag[500010];
void dfs(int t,int num,int tag,int z)
{
    if (t>prime[x][0])
    {
        if (z==-1)
            cnt[num]--;
        ans+=cnt[num]*tag;
        if (z==1) cnt[num]++;
        return;
    }
    dfs(t+1,num,tag,z);
    dfs(t+1,num*prime[x][t],-tag,z);
}
int main()
{
    int n,q;
    scanf("%d%d",&n,&q);
    for (int i=1;i<=n;i++) scanf("%d",&a[i]);
    memset(flag,0,sizeof(flag));
    for (int i=2;i<=500000;i++)//直接暴力筛质数
    {
        if (flag[i]) continue;
        prime[i][0]=1;
        prime[i][1]=i;
        for (int j=i+i;j<=500000;j+=i)
        {
            flag[j]=1;
            prime[j][++prime[j][0]]=i;
        }
    }
    memset(flag,0,sizeof(flag));
    ans=0;
    while (q--)
    {
        scanf("%d",&x);
        flag[x]^=1;
        if (flag[x])
        {
            x=a[x];
            dfs(1,1,1,1);
        }
        else
        {
            x=a[x]; 
            dfs(1,1,-1,-1);
        }
        printf("%lld\n",ans);
    }
    return 0;
}