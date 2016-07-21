#!/usr/local/bin/

import random

y = random.randint(1,10)
x = int(raw_input("Please guess the number up to 10:"))

if y == x:
	print "you have guessed the correct number %s" % y,

elif x < y:
	print "your guessed number is laser then correct number %s" % y,

else:
	print "your guessed number is higher then correct number %s" % y,

#else:
	#print "bye bye"
