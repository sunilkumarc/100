#include <iostream>
#include <cstring>

using namespace std;

int max(int a, int b) {
	return (a > b) ? a : b;
}

int LCSLength(char *str1, char *str2, int m, int n) {
	if (m == 0 || n == 0)
		return 0;

	if (str1[m - 1] == str2[n - 1])
		return 1 + LCSLength(str1, str2, m - 1, n - 1);
	else {
		return max(LCSLength(str1, str2, m - 1, n), LCSLength(str1, str2, m, n - 1));
	}
}

int LCSLengthUsingTabulation(char *str1, char *str2, int m, int n) {

	int L[m + 1][n + 1];
	int i, j;

	for (i = 0; i <= m; ++i) {
		for (int j = 0; j <= n; ++j) {
			if (i == 0 || j == 0) {
				L[i][j] = 0;
			}
			else if (str1[i - 1] == str2[j - 1]) {
				L[i][j] = 1 + L[i - 1][j - 1];
			}
			else {
				L[i][j] = max(L[i - 1][j], L[i][j - 1]);
			}
		}
	}
	return L[m][n];
}

int main() {

	char str1[] = "ABCiiiiiiiiiF";
	char str2[] = "BCaldfDafdjF";
	int m = strlen(str1);
	int n = strlen(str2);

	cout << "Using 2^n solution : " << LCSLength(str1, str2, m, n) << endl;
	cout << "Using tabulation : " << LCSLengthUsingTabulation(str1, str2, m, n) << endl;
	return 0;
}
