#!/usr/bin/python3.4

def square_numbers(nums):
	#result = []
	for i in nums:
		#result.append(i*i)
	#return result
		yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

#####
#with list comprihennsitions

#my_nums = (x*x for x in [1,2,3,4,5])


############
print (next(my_nums))


for num in my_nums:
	print (num)
