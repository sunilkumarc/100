package amazon.scotland;

public class Question2 {

	public static void main(String[] args) {

		int[] A = new int[5];
		A[0]  =  1;
		A[1]  =  0;
	  	A[2]  =  0;
	  	A[3]  =  1;
	  	A[4]  =  1;

	  	int res = solution(A);
	  	System.out.println(res);
	}

	public static int solution(int [] A) {

		if (A.length == 0) {
			return 0;
		}

		int globalMaxSliceLength = 1;
		int localMaxSliceLength = 1;
		int prevElemSign;

		if (A[0] > 0)
			prevElemSign = 1;
		else if (A[0] < 0)
			prevElemSign = -1;
		else
			prevElemSign = 0;

		for (int i = 1; i < A.length; ++i) {
			if (prevElemSign == 0) {
				localMaxSliceLength += 1;
				if (A[i] > 0)
					prevElemSign = 1;
				else if (A[i] < 0)
					prevElemSign = -1;
			} else if (prevElemSign == 1) {
				if (A[i] <= 0) {
					localMaxSliceLength += 1;
					prevElemSign *= -1;
				} else {
					if (localMaxSliceLength > globalMaxSliceLength)
						globalMaxSliceLength = localMaxSliceLength;
					localMaxSliceLength = 1;
				}
			} else {
				if (A[i] >= 0) {
					localMaxSliceLength += 1;
					prevElemSign *= -1;
				} else {
					if (localMaxSliceLength > globalMaxSliceLength)
						globalMaxSliceLength = localMaxSliceLength;
					localMaxSliceLength = 1;
				}
			}
		}

		if (localMaxSliceLength > globalMaxSliceLength)
			globalMaxSliceLength = localMaxSliceLength;

		return globalMaxSliceLength;
	}
}
