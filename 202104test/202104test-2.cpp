#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int maxn=500000;
int p[maxn+10],cnt;
short int vis[maxn+10],mu[maxn+10];
void read(int &x){  //输入 
    x=0; char c=getchar();
    while(c>'9'||c<'0') c=getchar();
    while(c>='0'&&c<='9') x=(x<<3)+(x<<1)+c-'0',c=getchar();
}
void Put(ll x)   //输出 
{
    if(x>9) Put(x/10);
    putchar(x%10+'0');
}
void prime() //筛莫比乌斯数 
{
    mu[1]=1; for(int i=2;i<=maxn;i++){
        if(!vis[i]) p[++cnt]=i,mu[i]=-1;
        for(int j=1;j<=maxn&&i*p[j]<=maxn;j++){
            vis[i*p[j]]=1; mu[i*p[j]]=-mu[i];
            if(i%p[j]==0) { mu[i*p[j]]=0; break; }
        }
    }
}
int a[200010],num[maxn+10];ll ans;
vector<int>G[maxn+10];
int main()
{
    prime();
    int N,Q,x,i,j,Max=0;
    scanf("%d%d",&N,&Q);
    for(i=1;i<=N;i++) read(a[i]),Max=max(Max,a[i]),vis[i]=0;
    for(i=1;i<=Max;i++){ //筛约数 
      for(j=i;j<=Max;j+=i)
         G[j].push_back(i);
    } 
    while(Q--){
        read(x);
        int L=G[a[x]].size();
        if(vis[x]==1){
            for(i=0;i<L;i++) num[G[a[x]][i]]--;
            for(i=0;i<L;i++) ans-=mu[G[a[x]][i]]*num[G[a[x]][i]];        
        }
        else {        
            for(i=0;i<L;i++) ans+=mu[G[a[x]][i]]*num[G[a[x]][i]];
            for(i=0;i<L;i++) num[G[a[x]][i]]++;
        }    
        vis[x]=vis[x]^1;    
        Put(ans); puts("");
    }
    return 0;
}