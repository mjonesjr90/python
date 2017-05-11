def isUnique(s):
	if len(s) > 256:
		return False;
	else:
		ans = True;
		for i in range(0, len(s)):
			count = i+1;
			holder = s[i];
			while count < len(s):
				if holder == s[count]:
					ans = False;
				count += 1;
			return ans;

uniq = isUnique("catch");
if uniq:
    print "I'm unique"
else:
    print "I'm not unique"
