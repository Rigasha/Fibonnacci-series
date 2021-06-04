#import dictionary
from collections import defaultdict

#define the variable
def isFibonacci(s):

    # map to store the characters of the string
    C = defaultdict(lambda: 0)

    for i in range(0, len(s)):
        C[s[i]] += 1

    # start the  vector value
    v = []

    # Get the size of the map
    ci = len(C)

    # a and b are first and second terms of fibonacci series
    a = b = 1

    v.append(a)
    v.append(b)

    # vector v contains elements of fibonacci series
    for i in range(0, ci - 2):
        v.append(a + b)
        c = a + b
        a, b = b, c

    flag, i = 1, 0

    # Compare vector elements with values in Map
    for itr in sorted(C):
        if C[itr] != v[i]:
            flag = 0
            break

        i += 1

    if flag == 1:
        return "Dynamic"
    else:
        return "Not dynamic"

if __name__ == "__main__":
    s = input("Enter the input\n")
    print(isFibonacci(s))

