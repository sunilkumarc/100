import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution2 {
	public static void main(String args[]) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] line = br.readLine().trim().split(" ");
		int N = Integer.parseInt(line[0]);
		int M = Integer.parseInt(line[1]);
		line = br.readLine().trim().split(" ");

		List<Long> A = new ArrayList<>();
		for (String str : line) {
			A.add(Long.parseLong(str));
		}

		line = br.readLine().trim().split(" ");

		List<Long> B = new ArrayList<>();
		for (String str : line) {
			B.add(Long.parseLong(str));
		}

		List<Long> AFValue = new ArrayList<>();
		List<Long> AGValue = new ArrayList<>();

		List<Long> BFValue = new ArrayList<>();
		List<Long> BGValue = new ArrayList<>();

		Collections.sort(A);
		Collections.sort(B);

		int i = 0, j = 0;
		while (i < A.size() && j < B.size()) {
			if (A.get(i) > B.get(j)) {
				BFValue.add((long) i);
				++j;
			} else if (A.get(i) < B.get(j)) {
				AFValue.add((long) j);
				++i;
			} else {
				++i;
				++j;
			}
		}

		while (i < A.size()) {
			AFValue.add((long) j);
			++i;
		}

		while (j < B.size()) {
			BFValue.add((long) i);
			++j;
		}

		/*System.out.print("AFValue : ");
		for (Integer fx : AFValue)
			System.out.print(fx + " ");
		System.out.println();
		System.out.print("BFValue : ");
		for (Integer fx : BFValue)
			System.out.print(fx + " ");
		System.out.println();*/

		Collections.reverse(A);
		Collections.reverse(B);
		i = 0; j = 0;
		while (i < A.size() && j < B.size()) {
			if (A.get(i) < B.get(j)) {
				BGValue.add((long) i);
				++j;
			} else if (A.get(i) > B.get(j)) {
				AGValue.add((long) j);
				++i;
			} else {
				++i;
				++j;
			}
		}

		while (i < A.size()) {
			AGValue.add((long) j);
			++i;
		}

		while (j < B.size()) {
			BGValue.add((long) i);
			++j;
		}


		long AValue = 0;
		N = AFValue.size();
		for (i = 0; i < AFValue.size(); ++i)
			AValue += AFValue.get(i) * AGValue.get(N-i-1);

		long BValue = 0;
		M = BFValue.size();
		for (i = 0; i < BFValue.size(); ++i) {
			BValue += BFValue.get(i) * BGValue.get(M-i-1);
		}

		if (AValue > BValue)
			System.out.println("Monk " + (AValue-BValue));
		else if (AValue < BValue)
			System.out.println("!Monk " + (BValue-AValue));
		else
			System.out.println("Tie");
	}
}
