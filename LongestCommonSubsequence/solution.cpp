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

int main() {

	char str1[] = "ABCiiiiiiiiiF";
	char str2[] = "BCaldfDafdjF";
	int m = strlen(str1);
	int n = strlen(str2);

	cout << LCSLength(str1, str2, m, n);

	return 0;
}
