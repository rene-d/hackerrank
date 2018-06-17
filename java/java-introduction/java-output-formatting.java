// Java > Introduction > Java Output Formatting
// Format a string using printf.
//
// https://www.hackerrank.com/challenges/java-output-formatting/problem
// challenge id: 9472
//

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                System.out.printf("%-15s%03d\n", s1, x);
            }
            System.out.println("================================");

    }
}
