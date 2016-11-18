import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class PrimesAndFactors {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		int noOfPrimes = N/2;
		int isPrime[] = new int[noOfPrimes + 1];

		for (int i = 0; i <= noOfPrimes; ++i) {
			isPrime[i] = 1;
		}

		int n = (int) Math.sqrt(noOfPrimes);
		for (int i = 2; i <= n; ++i) {
			if (isPrime[i] == 1) {
				for (int j = i * 2; j <= noOfPrimes; j += i) {
					isPrime[j] = 0;
				}
			}
		}

		Map<Integer, Integer> result = new HashMap<>();
		for (int i = 2; i <= noOfPrimes; ++i) {
			if (isPrime[i] == 1) {
				int j = i;
				while (j <= N/2) {
					if (N%j == 0) {
						if (result.containsKey(i))
							result.put(i, result.get(i)+1);
						else
							result.put(i, 1);
					}
					j = j * i;
				}
			}
		}

		for (Integer key : result.keySet()) {
			System.out.println(key + " : " + result.get(key));
		}
	}
}
