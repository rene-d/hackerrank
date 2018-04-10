# The Time in Words
# Display the time in words.
#
# https://www.hackerrank.com/challenges/the-time-in-words/problem
#


numbers = ["", "one", "two", "three", "four", "five", "six",
           "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen", "twenty"]

def timeInWords(h, m):
    # Complete this function
    if m == 0:
        return "{} o' clock".format(numbers[h])

    if m > 30:
        verb = "to"
        h += 1
        if h == 13:
            h = 1
        m = 60 - m
    else:
        verb = "past"

    if m == 1:
        return "one minute {} {}".format(verb, numbers[h])

    if m == 30:
        return "half past {}".format(numbers[h])

    if m == 15:
        return "quarter {} {}".format(verb, numbers[h])

    if m > 20:
        return "{} {} minutes {} {}".format(numbers[20], numbers[m - 20], verb, numbers[h])

    return "{} minutes {} {}".format(numbers[m], verb, numbers[h])



if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
