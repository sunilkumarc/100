import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	static int[] trans = null;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		String[] transactions = br.readLine().split(" ");
		trans = Arrays.asList(transactions).stream().mapToInt(Integer::parseInt).toArray();
		int Q = Integer.parseInt(br.readLine());
		int target;

		for (int i = 0; i < Q; ++i) {
			target = Integer.parseInt(br.readLine());
			System.out.println(findMaxTrans(target));
		}
	}

	static int findMaxTrans(int target) {
		int currentSum = 0;

		if (currentSum >= target) {
			return 0;
		}

		for (int i = 0; i < trans.length; ++i) {
			currentSum += trans[i];

			if (currentSum >= target) {
				return i+1;
			}
		}

		return -1;
	}
}
