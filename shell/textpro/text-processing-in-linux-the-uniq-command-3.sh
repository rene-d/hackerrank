# Linux Shell > Text Processing > 'Uniq' command #3
# Let's learn about the 'uniq' command.
#
# https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-3/problem
#

uniq -c -i | while read a b ; do
    echo $a $b
done
