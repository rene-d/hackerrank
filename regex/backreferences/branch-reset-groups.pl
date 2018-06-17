# Regex > Backreferences > Branch Reset Groups
# Alternatives having same capturing group
#
# https://www.hackerrank.com/challenges/branch-reset-groups/problem
# challenge id: 14816
#

$Regex_Pattern = '^\d\d(?|(---)|(-)|(:)|(\.))\d\d\1\d\d\1\d\d$';

# (skeliton_tail) ----------------------------------------------------------------------
$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}
