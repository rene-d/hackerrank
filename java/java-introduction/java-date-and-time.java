// Java > Introduction > Java Date and Time
// Print the day of a given date.
//
// https://www.hackerrank.com/challenges/java-date-and-time/problem
// challenge id: 23448
//

import java.util.Scanner;
// (skeliton_head) ----------------------------------------------------------------------

import java.util.*;

public class Solution {

    private static String getDay(String day, String month, String year) {

        Calendar cal = Calendar.getInstance();

        cal.set(Integer.parseInt(year), Integer.parseInt(month) - 1, Integer.parseInt(day));

        String s = cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.US);

        return s.toUpperCase();
    }

// (skeliton_tail) ----------------------------------------------------------------------
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}
