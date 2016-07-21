#!/usr/bin/python3

# program to make calculater

a = input('Please enter first no : ')
b = input('Please enter second no : ')

N1=int(a)
N2=int(b)

c = input('What mathematical operation you want to perform : ')


print(' Your First no N1 is :',N1)
print('Mathematical operator:',c)
print('Your Second no N2 is :',N2)


for ops in c:

	if c not in "'+' , '-' , '*' , '**' , '/' , '%' , '//'":
		print('Please enter valid operator :')


	elif	c == '+':
		print('Addition of a and b is:' , N1 + N2)

	elif	c == '-':
		print('Subtraction of N1 and N2 is:' , N1 - N2)

	elif	c == '*':
		print('Multiplication of N1 and N2 is' , N1 * N2)

	elif	c == '/':
		print('Division of N1 and N2 is' , N1 / N2)

	elif	c == '%':
		print('Modulas of N1 and N2 is' , N1 % N2)

	elif	c == '**':
		print('Exponenet of N1 to N2 is' , N1 ** N2)

	elif	c == '//':
		print('Floor Division of N1 to N2 is' , N1 // N2)

	else:
		print('This is out of the scop of this calc')

print('\nCongratulations hj!!')

