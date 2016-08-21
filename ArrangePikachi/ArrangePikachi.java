import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Collections;

public class ArrangePikachi {

    public static void main(String [] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        int N;
        ArrayList<Integer> fightingPower = new ArrayList<>();

        for (int i = 0; i < T; ++i) {
            N = Integer.parseInt(br.readLine().trim());
            String outputString = "";
            for (int j = 0; j < N; ++j) {
                fightingPower.add(br.read());
            }
            Collections.sort(fightingPower);

            int size = fightingPower.size();
            for (int j = 0; j < size - 1; ++j) {
                outputString += fightingPower.get(j) + " ";
            }
            if (size > 1)
                outputString += fightingPower.get(fightingPower.size()-1);
            else if (size == 1)
                outputString += fightingPower.get(0);

            System.out.println(outputString);
        }
    }
}
