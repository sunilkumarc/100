// https://www.codingame.com/ide/puzzle/power-of-thor

import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt();
            String directionY = "";
            String directionX = "";
            if (initialTY > lightY) {
                directionY = "N";
                initialTY -= 1;
            } else if (initialTY < lightY) {
                directionY = "S";
                initialTY += 1;
            }
            
            if (initialTX > lightX) {
                directionX = "W";
                initialTX -= 1;
            } else if (initialTX < lightX) {
                directionX = "E";
                initialTX += 1;
            }
            System.out.println(directionY + directionX);
        }
    }
}