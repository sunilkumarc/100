import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Collections;

public class PokeDivisors {
    static ArrayList<Integer> primeFactors = new ArrayList<>();

    public static void main(String [] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int T = Integer.parseInt(line);
        int num;


        for (int i = 0; i < T; ++i) {

            num = Integer.parseInt(br.readLine().trim());
            PokeDivisors.getPrimeFactors(num);

            Collections.sort(primeFactors);
            String outputString = "";
            int size = primeFactors.size();
            for (int j = 0; j < size - 1; ++j) {
                outputString += primeFactors.get(j) + " ";
            }
            if (size > 1)
                outputString += primeFactors.get(primeFactors.size()-1);
            else if (size == 1)
                outputString += primeFactors.get(0);
            System.out.println(outputString);
        }
    }

    static void getPrimeFactors(int num) {
        primeFactors.clear();
        if (num < 2)
            return;
        /*
        int i = 2;
        while (num > 1) {
            if (num % i == 0) {
                primeFactors.add(i);
                num /= i;
            } else {
                ++i;
            }
        }
        */
        while (num % 2 == 0) {
            primeFactors.add(2);
            num /= 2;
        }

        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            while (num % i == 0) {
                primeFactors.add(i);
                num /= i;
            }
        }

        if (num > 2)
            primeFactors.add(num);
    }
}
