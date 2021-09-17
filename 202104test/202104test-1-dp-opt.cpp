#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main(){
	double n = 0;
	cin >> n;
	vector<vector<long long int> > dp(n + 1, vector<long long int>(2));
	dp[1][0] = 3, dp[2][0] = 9, dp[2][1] = 3;
	for(int i = 3; i <= n; ++i) {
		dp[i][1] = (dp[i - 1][0] - dp[i - 1][1]) % 10000000000000000;
		dp[i][0] = (dp[i - 1][0] * 3 - dp[i - 1][1]) % 10000000000000000; 
	}
	long long int result = dp[n][0];
	long long int length = (int)log10(result) + 1;
	if (n <= 36) {
		cout << result;
	} else {
		cout << "......" << result % 10000000000;
	}
} 
