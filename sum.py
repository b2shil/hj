#!/usr/bin/python3

# summing of sequence

a = input('enter first number: ')
b = input('enter last number: ')

a = int(a)
b = int(b)
sum = 0

for i in range (a,b):
	#print('current number is : ',i)
	sum += i
	#print('summetion of', sum , 'and', i ,'is: ', sum += i )
	print(sum)
