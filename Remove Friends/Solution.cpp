// https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/remove-friends-5/
#include <iostream>

using namespace std;

int main() {

	int T, N, K;
	cin >> T;
	while (T--) {
		cin >> N; cin >> K;
		int priorities[N];
		for (int i = 0; i < N; ++i) {
			cin >> priorities[i];
		}
		int i = 0;
		int j = i + 1;
		// 5 2
		// 19 12 3 4 17
		// 19 12 3 14
		while (i < N-1 && K > 0) {
			if (priorities[i] < priorities[j]) {
				// cout << priorities[i] << " is less than " << priorities[j] << endl;
				priorities[i] = -1;
				--K;
				if (i - 1 >= 0 and priorities[i-1] != -1) {
					j = i + 1;
					--i;
				}
				else {
					++i; ++j;
				}
			}
			else {
				if (priorities[i + 1] == -1)
					i += 2;
				else
					++i;
				j = i + 1;
			}
		}
		i = N - 1;
		while (i >= 0 && K > 0) {
			if (priorities[i] != -1) {
				priorities[i] = -1;
				--K;
			}
			--i;
		}

		i = 0;
		while (i < N) {
			if (priorities[i] != -1)
				cout << priorities[i] << " ";
			++i;
		}
		cout << endl;
	}

	return 0;
}
