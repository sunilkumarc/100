package ion.hiring.challenge;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

class Num {
	long num;
	int sign;

	Num(long n, int s) {
		num = n;
		sign = s;
	}
}

class Solution1 {
	public static void main(String args[]) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine().trim();
		int N = Integer.parseInt(line);

		String[] arr = br.readLine().trim().split(" ");
		// Map<Long, Integer> array = new HashMap<>();
		List<Num> array = new ArrayList<>();
		for (String str : arr) {
			long elem = Long.parseLong(str);
			if (elem < 0) {
				elem *= -1;
				array.add(new Num(elem, -1));
			} else {
				array.add(new Num(elem, 1));
			}
		}

		Collections.sort(array, new Comparator<Num>() {
			@Override
			public int compare(Num o1, Num o2) {
				Num n1 = (Num) o1;
				Num n2 = (Num) o2;

				return Long.compare(n1.num, n2.num);
			}
		});

		for (Num n : array) {
			System.out.print((n.num * n.sign) + " ");
		}
	}
}
