import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class prog {

	static List<Integer> convertToIntArray(String N) {
		List<Integer> result = new ArrayList<>();
		for (Character ch : N.toCharArray()) {
			result.add(ch - '0');
		}
		return result;
	}

	static void nextSmallestPalindrome(String N) {
		List<Integer> arr = convertToIntArray(N);
		int size = arr.size();
		int left = (int)size/2-1;
		int right = (size % 2 == 0) ? (int) size / 2 : (int) size / 2 + 1;
		int mid = (int) (left + right) / 2;
		boolean hasChanged = false;
//		System.out.println("Left: " + left + ", Mid : " + mid + ", Right : " + right);

		/*for (Integer i : arr)
			System.out.print(i + " ");
		System.out.println();*/

		while (left >= 0) {
			if (arr.get(left) != arr.get(right)) {
				if (arr.get(right) < arr.get(left)) {
					arr.set(right, arr.get(left));
					hasChanged = true;
				} else {
					if (hasChanged == true)
						arr.set(right, arr.get(left));
					else {
						hasChanged = true;
						if (left == mid) {
							arr.set(left, arr.get(left) + 1);
							arr.set(right, arr.get(left));
						} else {
							// Propagate logic here.
							arr.set(right, arr.get(left));
							int l = (mid%2 == 0) ? mid : mid-1;
							int m = mid+1;
							// 71499422
							// 149941
							while (l > left) {
								if (arr.get(l) != 9) {
									arr.set(l, arr.get(l)+1);
									arr.set(m, arr.get(l));
									break;
								}
								--l;
								++m;
							}
						}
					}
				}
			}
			left -= 1;
			right += 1;
		}

//		for(Integer i : arr)
//			System.out.print(i);
//		System.out.println();

		if (hasChanged == false) {
			if (arr.get(mid) != 9) {
				arr.set(mid, arr.get(mid) + 1);
				if (mid % 2 != 0) {
					arr.set(mid+1, arr.get(mid));
				}

			} else
				arr = convertToIntArray(Integer.parseInt(N)+2 + "");
		} else {
			if (size % 2 != 0)
				arr.set(mid, 0);
		}

		for(Integer i : arr)
			System.out.print(i);
	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		String N;
		while (T-- > 0) {
			N = br.readLine().trim();
			nextSmallestPalindrome(N);
		}
	}
}
