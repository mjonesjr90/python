def naive(a,b):
	x =  a;
	y = b;
	z = 0;
	while x > 0:
		z = z + y;
		x = x - 1;
	return z

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

print naive(3,2)

print countdown(50)