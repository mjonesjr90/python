def isPerm(s1, s2):
    if(len(s1) != len(s2)):
        return False;
    else:
        found = False;
        ans = True;
        for i in range(0, len(s1)): #get first letter from string one, iterate as you check
            for j in range(0, len(s2)): #iterate through the letters of string two
                if s1[i] == s2[j]: #check if the letter from string one matches the letter from string two
                    s2[j] == " "; #set the matching letter to a blank
                    found = True; #if there was a match, set found to True
                    break; #if found, break out of the loop and move on to the next number
            if found:
                found = False #set found back to False
            else:
                ans = False;
        return ans;

def isPerm2(s1, s2):
    if(len(s1) != len(s2)):
        return False;
    else:
        ns1 = sorted(s1);
        ns2 = sorted(s2);
        if(ns1 == ns2):
            return True;
        else:
            return False;

perm = isPerm("catch", "tcahc");
if perm:
    print "I'm a permutation\n"
else:
    print "I'm not a permutation\n"

perm = isPerm2("catch", "tcahc");
if perm:
    print "p2: I'm a permutation\n"
else:
    print "p2: I'm not a permutation\n"
