#!/usr/bin/python3.4

#prog with for loop with opening file
a=0
fh = open('test.txt')
for line in fh.readlines():
	a=a+1
	print('line no:',a ,line)
