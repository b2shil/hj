#!/usr/bin/python3

#program of fibonacci sequence

a = input('enter a starting number of fibonacci sequence : ')
b = input('enter an ending number of fibonacci sequence : ')

a = int(a)
b = int(b)

print ('your febonacci sequence range is :' , a ,'to', b)

for i in range(a, b):
	print(a)
	a , b = b , a+b
