// Regex > Backreferences > Forward References
// Back reference to a group which appear later in regex.
//
// https://www.hackerrank.com/challenges/forward-references/problem
// challenge id: 14820
//

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
// (skeliton_head) ----------------------------------------------------------------------

public class Solution {

    public static void main(String[] args) {

        Regex_Test tester = new Regex_Test();
        tester.checker("^(\\2tic|(tac))+$"); // Use \\ instead of using \

    }
}

// (skeliton_tail) ----------------------------------------------------------------------
class Regex_Test {

    public void checker(String Regex_Pattern){

        Scanner Input = new Scanner(System.in);
        String Test_String = Input.nextLine();
        Pattern p = Pattern.compile(Regex_Pattern);
        Matcher m = p.matcher(Test_String);
        System.out.println(m.find());
    }

}
