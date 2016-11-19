package ion.hiring.challenge;

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

		List<Integer> A = new ArrayList<>();
		for (String str : line) {
			A.add(Integer.parseInt(str));
		}

		line = br.readLine().trim().split(" ");

		List<Integer> B = new ArrayList<>();
		for (String str : line) {
			B.add(Integer.parseInt(str));
		}

		List<Integer> AFx = new ArrayList<>();
		List<Integer> AGx = new ArrayList<>();

		List<Integer> BFx = new ArrayList<>();
		List<Integer> BGx = new ArrayList<>();

		Collections.sort(A);
		Collections.sort(B);

		int i = 0, j = 0;
		while (i < A.size() && j < B.size()) {
			if (A.get(i) > B.get(j)) {
				BFx.add(i);
				++j;
			} else if (A.get(i) < B.get(j)) {
				AFx.add(j);
				++i;
			} else {
				++i;
				++j;
			}
		}

		while (i < A.size()) {
			AFx.add(j);
			++i;
		}

		while (j < B.size()) {
			BFx.add(i);
			++j;
		}

		for (Integer fx : AFx)
			System.out.print(fx + " ");
		System.out.println();
		for (Integer fx : BFx)
			System.out.print(fx + " ");
		System.out.println();

		Collections.reverse(A);
		Collections.reverse(B);
		i = 0; j = 0;
		while (i < A.size() && j < B.size()) {
			if (A.get(i) < B.get(j)) {
				BGx.add(i);
				++j;
			} else if (A.get(i) > B.get(j)) {
				AGx.add(j);
				++i;
			} else {
				++i;
				++j;
			}
		}

		while (i < A.size()) {
			AGx.add(j);
			++i;
		}

		while (j < B.size()) {
			BGx.add(i);
			++j;
		}

		for (Integer gx : AGx)
			System.out.print(gx + " ");
		System.out.println();
		for (Integer gx : BGx)
			System.out.print(gx + " ");
		System.out.println();

		int VAx = 0;
		for (i = 0; i < AFx.size(); ++i)
			VAx += AFx.get(i) * AGx.get(N-i-1);

		int VBx = 0;
		for (i = 0; i < BFx.size(); ++i) {
			VBx += BFx.get(i) * BGx.get(M-i-1);
		}

		if (VAx > VBx)
			System.out.println("Monk " + VAx);
		else if (VAx < VBx)
			System.out.println("!Monk " + VBx);
		else
			System.out.println("Tie");
	}
}
