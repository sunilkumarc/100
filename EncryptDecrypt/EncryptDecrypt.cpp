#include <iostream>
#include <cstring>

using namespace std;

void encryptDecrypt(char *arr) {
	int len = strlen(arr);
	char secretKey = 'A';

	for (int i = 0; i < len; ++i) {
		arr[i] ^= secretKey;
	}
}

int main(void) {

	char myLockerNumber[] = "HelloString";

	encryptDecrypt(myLockerNumber);
	cout << "After Encrypting : " << myLockerNumber << endl;

	encryptDecrypt(myLockerNumber);
	cout << "After Decrypting : " << myLockerNumber << endl;

	return 0;
}
