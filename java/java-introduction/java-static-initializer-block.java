// Java > Introduction > Java Static Initializer Block
// Initialize some variables using Static initialization blocks!
//
// https://www.hackerrank.com/challenges/java-static-initializer-block/problem
// challenge id: 13800
//

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
// (skeliton_head) ----------------------------------------------------------------------

private static boolean flag;
private static int B, H;

static  {
    Scanner scanner = new Scanner(System.in);
    B = scanner.nextInt();
    H = scanner.nextInt();
    scanner.close();

    flag = (B > 0 && H > 0);

    try {
        if (! flag)
            throw new Exception("Breadth and height must be positive");
    } catch (Exception e) {
        System.out.println(e);
    }
}

// (skeliton_tail) ----------------------------------------------------------------------
public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}

	}//end of main

}//end of class
