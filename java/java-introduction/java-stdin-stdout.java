// Java > Introduction > Java Stdin and Stdout II
// Familiarize yourself with Standard Input/Output.
//
// https://www.hackerrank.com/challenges/java-stdin-stdout/problem
// challenge id: 9458
//

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // Write your code here.
        double d = scan.nextDouble();
        scan.nextLine();                // lit le retour à la ligne après le double
        String s = scan.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
