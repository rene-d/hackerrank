// Java > Introduction > Java Loops I
// Let's talk about loops.
//
// https://www.hackerrank.com/challenges/java-loops-i/problem
// challenge id: 23447
//

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        for (int i = 1; i <= 10; ++i)
            System.out.printf("%d x %d = %d\n", N, i, N * i);
    }
}
