def Compression(s):
    count = 1;
    ns = "";
    for i in range(0, len(s)):
        if i == (len(s)-1):
            ns = ns + s[i] + str(count);
            count = 1;
            break;
        if s[i] == s[i+1]:
            count += 1;
        else:
            ns = ns + s[i] + str(count);
            count = 1;
    if len(s) > len(ns):
        return ns;
    else:
        return s;

print Compression("aaaaaaaaaaagg");
