// Java > Introduction > Java End-of-file
// Learn how to read from standard input until EOF.
//
// https://www.hackerrank.com/challenges/java-end-of-file/problem
// challenge id: 8279
//

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */

        Scanner sc = new Scanner(System.in);
        int line = 0;
        while (sc.hasNextLine()) {
            System.out.printf("%d %s\n", ++line, sc.nextLine());
        }
        sc.close();
    }
}