// Java > Introduction >  Java Stdin and Stdout I
// Get started with standard input and output.
//
// https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem
// challenge id: 9762
//

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        scan.close();
    }
}
