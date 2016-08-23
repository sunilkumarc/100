import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Collections;

public class FindDualNumber {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int length ;
        int prime1 = -1, prime2 = -1;
        int num;
        ArrayList<Integer> primes = new ArrayList<>();

        for (int i = 0; i < T; ++i) {
            prime1 = prime2 = -1;

            length = Integer.parseInt(br.readLine().trim());
            String [] line = br.readLine().trim().split(" ");
            for (String n : line) {
                num = Integer.parseInt(n);
                if (FindDualNumber.isBoolean(num)) {
                    if (prime1 == -1)
                        prime1 = num;
                    else if (prime2 == -1)
                        prime2 = num;
                    else {
                        if (num > prime1)
                            prime1 = num;
                        else if (num > prime2)
                            prime2 = num;
                    }
                }
            }

            if (prime1 == -1 && prime2 == -1)
                System.out.println(prime1 + "," + prime2 + " - " +  "-1");
            else if (prime2 == -1)
                System.out.println(prime1 + "," + prime2 + " - " +  prime1 * prime1);
            else
                System.out.println(prime1 + "," + prime2 + " - " +  prime1 * prime2);
        }
    }

    public static boolean isBoolean(int num) {

		if (num < 2)
			return false;
		else if (num == 2)
			return true;
        else if (num % 2 == 0)
            return false;
        else {
            for (int i = 3; i*i <= num; i += 2) {
                if (num % i == 0)
                    return false;
            }
        }
        return true;
    }
}
