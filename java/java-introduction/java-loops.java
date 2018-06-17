// Java > Introduction > Java Loops II
// Use loops to find sum of a series.
//
// https://www.hackerrank.com/challenges/java-loops/problem
// challenge id: 8018
//

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int x = a;
            for (int j = 0; j < n; ++j) {
                x += Math.pow(2, j) * b;
                System.out.printf("%d ", x);
            }
            System.out.println();
        }
        in.close();
    }
}
