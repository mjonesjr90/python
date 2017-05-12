#Compresses a string and outputs the number of repeated characters in a sequence

#Add the ability to read in command line arguments
import sys


#Function definitions
def compression(s):
    count = 1
    ns = ""
    for i in range(0, len(s)):
        if i == (len(s)-1):
            ns = ns + s[i] + str(count)
            count = 1
            break
        if s[i] == s[i+1]:
            count += 1
        else:
            ns = ns + s[i] + str(count)
            count = 1
    if len(s) > len(ns):
        return ns
    else:
        return s

#Function calls
if len(sys.argv) == 1: #No aragument was passed
    w = raw_input("Enter a string to compress: ")
    print(compression(w))
elif len(sys.argv) > 2: #Too many arguments were passed
    print("You entered too many arguments.")
    v = raw_input("Enter a string to compress: ")
    print(compression(v))
else:
    print(compression(sys.argv[1]))
