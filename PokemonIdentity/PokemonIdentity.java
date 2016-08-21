import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Iterator;

public class PokemonIdentity {

    static ArrayList<Triplet> triplets = new ArrayList<>();
    static LinkedList<Character> ll = new LinkedList<>();
    static ArrayList<Triplet> incorrectTriplets = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        /*
		 * Read T - No of test cases
		 * Read and put all the triplets in a list of strings
		 * Loop through each string until it is checked
		 * 		Read and put each char in correct position
		 * 			if the char is already present
		 * 				check if it is in correct position
		 * 				else reorder chars so that they are in correct position
		 * 			else put the char
		 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int T = Integer.parseInt(line);

        String triplet;
        char ch;
        Triplet tripletObj;

        for (int i = 0; i < T; ++i) {
            triplet = br.readLine().replace(" ", "");
            tripletObj = new Triplet(triplet);
            triplets.add(tripletObj);
        }

        Iterator<Triplet> it = triplets.iterator();

        int index;

        /*
        7
        i v a
        i v s
        s u r
        y s u - -1
        s a u
        i v u
        v y a

        i, v, s, y, a, u, r
        i v s y a u r

        */
        int index0, index1, index2;
        while (it.hasNext()) {
            tripletObj = it.next();
            triplet = tripletObj.getTriplet();
            for (int j = 0; j < triplet.length(); ++j) {
                ch = triplet.charAt(j);
                if (!ll.contains(ch))
                    ll.add(ch);
                else {
                    // chekc if it is present at the correct location
                    // if not
                    //      reorder the position
                    index0 = ll.indexOf(triplet.charAt(0));
                    index1 = ll.indexOf(triplet.charAt(1));
                    index2 = ll.indexOf(triplet.charAt(2));
                    if (j == 1) {
                        if (index1 < index0) {
                            ll.remove(index0);
                            ll.add(index1, triplet.charAt(0));
                        }
                    } else if (j == 2) {
                        if (index2 < index1) {
                            ll.remove(index1);
                            ll.add(index2, triplet.charAt(1));
                        } else if (index1 < index0) {
                            ll.remove(index0);
                            ll.add(index1, triplet.charAt(0));
                        }
                    }
                }
            }
        }

        while (! isNotOrdered()) {
            // Correct all the incorrect triplets
            correct();
        }

        Iterator it2 = ll.iterator();
        while (it2.hasNext()) {
            System.out.print(it2.next());
        }
    }

    private static void correct() {

        Iterator<Triplet> it = incorrectTriplets.iterator();
        Triplet tripletObj;
        char ch;
        String triplet;
        int index0, index1, index2;
        while (it.hasNext()) {
            tripletObj = it.next();
            triplet = tripletObj.getTriplet();
            for (int j = 0; j < triplet.length(); ++j) {
                index0 = ll.indexOf(triplet.charAt(0));
                index1 = ll.indexOf(triplet.charAt(1));
                index2 = ll.indexOf(triplet.charAt(2));
                if (j == 1) {
                    if (index1 < index0) {
                        ll.remove(index0);
                        ll.add(index1, triplet.charAt(0));
                    }
                } else if (j == 2) {
                    if (index2 < index1) {
                        ll.remove(index1);
                        ll.add(index2, triplet.charAt(1));
                    } else if (index1 < index0) {
                        ll.remove(index0);
                        ll.add(index1, triplet.charAt(0));
                    }
                }
            }
        }
    }

    private static boolean isNotOrdered() {
        // populate incorrect triplets and return true
        Iterator<Triplet> it = triplets.iterator();
        Triplet tripletObj;
        char ch;
        String triplet;
        int index0, index1, index2;
        boolean notOrdered = true;
        incorrectTriplets.clear();
        while (it.hasNext()) {
            tripletObj = it.next();
            triplet = tripletObj.getTriplet();
            index0 = ll.indexOf(triplet.charAt(0));
            index1 = ll.indexOf(triplet.charAt(1));
            index2 = ll.indexOf(triplet.charAt(2));
            if (index0 > index1 || index1 > index2) {
                incorrectTriplets.add(tripletObj);
                notOrdered = false;
            }
        }
         return notOrdered;
    }
}

class Triplet {
    String triplet;
    boolean checked;

    public Triplet(String triplet) {
        this.triplet = triplet;
        checked = false;
    }

    String getTriplet() {
        return this.triplet;
    }

    boolean getStatus() {
        return this.checked;
    }
}
