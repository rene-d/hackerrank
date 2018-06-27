// Algorithms > Warmup > Solve Me First
// This is an easy challenge to help you start coding in your favorite languages!
//
// https://www.hackerrank.com/challenges/solve-me-first/problem
// challenge id: 2532
//

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int solveMeFirst(int a, int b) {
      	// Hint: Type return a+b; below
        return a + b;
   }

 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int sum = solveMeFirst(a, b);
        System.out.println(sum);
        in.close();
   }
}
