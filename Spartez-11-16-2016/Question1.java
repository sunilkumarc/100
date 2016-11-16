import java.util.ArrayList;
import java.util.List;

public class Prog1 {

	static public int findArray(int[] array, int[] subArray) {

		List<Integer> results = new ArrayList<>();
		if (array.length == 0 || subArray.length == 0)
			return -1;

		if (subArray.length > array.length)
			return -1;

		int i = 0;
		while (i < (array.length - subArray.length)+1) {
			boolean found = true;
			int j = 0;
			while (j < subArray.length) {
				if (subArray[j]  != array[i]) {
					found = false;
					break;
				}
				++i;
				++j;
			}
			if (found == true) {
				results.add(i-subArray.length);
			}
			++i;
		}
		if (results.size() > 0)
			return results.get(results.size()-1);

		return -1;
    }

	public static void main(String[] args) {

		/*int[] arr1 = new int[5];
		int[] arr2 = new int[2];
		arr1[0] = 4; arr1[1] = 9; arr1[2] = 3; arr1[3] = 7; arr1[4] = 8;
		arr2[0] = 3; arr2[1] = 7;*/

		/*int[] arr1 = new int[3];
		int[] arr2 = new int[1];
		arr1[0] = 1; arr1[1] = 3; arr1[2] = 5;
		arr2[0] = 1;*/

		/*int[] arr1 = new int[3];
		int[] arr2 = new int[3];
		arr1[0] = 7; arr1[1] = 8; arr1[2] = 9;
		arr2[0] = 8; arr2[1] = 9; arr2[2] = 10;*/

		int[] arr1 = new int[8];
		int[] arr2 = new int[2];
		arr1[0] = 4; arr1[1] = 9; arr1[2] = 3; arr1[3] = 7; arr1[4] = 8; arr1[5] = 3; arr1[6] = 7; arr1[7] = 1;
		arr2[0] = 3; arr2[1] = 7;

		System.out.println(findArray(arr1, arr2));
	}
}
