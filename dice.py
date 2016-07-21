#!/usr/local/bin/

import random
x = random.randint(1,6)
print "dice has rolled",x

while True:
	if 6 == x:
		print "\n\ncongratulations you got 6"
		y = random.randint(1,6)
		print "dice has rolled again",y
		break;
	else:
		raw_input("\n\nPress the enter key to exit.");
		break;
