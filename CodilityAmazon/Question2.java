package amazon.scotland;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Question1 {

	public static void main(String[] args) throws IOException {

		int[] A = new int[7];
		A[0] = 1; A[1] = 2; A[2] = 4; A[3] = 5; A[4] = 7; A[5] = 29; A[6] = 30;

		int res = solution(A);
		System.out.println(res);
 	}

	public static int solution(int[] A) {
        // write your code in Java SE 8

		List<Integer> diffArr = new ArrayList<Integer>();
		int difference = 0;
		int totalPrice = 0;
		int firstElem = A[0];

		for (int date : A) {
			difference = date - firstElem;
			if (difference <= 6) {
				diffArr.add(difference);
			} else {
				if (diffArr.size() <= 3 ) {
					totalPrice += (diffArr.size() * 2);
				} else {
					totalPrice += 7;
				}
				diffArr.clear();
				diffArr.add(0);
				firstElem = date;
			}
		}

		if (diffArr.size() <= 3 ) {
			totalPrice += (diffArr.size() * 2);
		} else {
			totalPrice += 7;
		}

		if (totalPrice > 25) {
			return 25;
		}

		return totalPrice;
    }

	public static void printArr(List<Integer> A) {
		for (int i : A) {
			System.out.print(i + " ");
		}
		System.out.println();
	}
}
