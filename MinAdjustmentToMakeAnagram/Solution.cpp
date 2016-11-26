#include <iostream>
#include <string>
#include <map>
using namespace std;

int findMinAdjLength(string one, string two) {
	map<char, int> myMap;
	int l1 = one.length();
	int l2 = two.length();
	string temp;
	int res = 0;

	if (l2 < l1) {
		temp = one; one = two; two = temp;
		l1 = one.length(); l2 = two.length();
	}

	for (int i = 0; i < l1; ++i) {
		myMap[one[i]] = 1;
	}

	for (int i = 0; i < l2; ++i) {
		if ((myMap.find(two[i]) != myMap.end()) == 0) {
			res += 1;
		}
	}

	return res;
}

int main() {

	string one, two;
	cin >> one;
	cin >> two;

	cout << findMinAdjLength(one, two);

	return 0;
}
