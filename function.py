#!/usr/bin/python3.4

#function program to check prime number

def isprime(n):
	if n == 1:
		print('1 is a special')
		return False
	for x in range(2,n):
		if n % x == 0:
			print('{} equals {} x {}'.format(n, x, n // x))
			return False
	else:
		print('ok!', n, 'is a prime number')
		return True

n = int(input('please enter number till which you want prime numbers: '))
for n in range (1,n):
	isprime(n)
