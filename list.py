#!/usr/bin/python3.4

## write a program to find out values in list which are less then 5

List = []

for i in range(1,10):
	List.append(int(input('enter up to 10 numbers: ')))
print ('This is the entered list : ',List)

p = int(input('enter a number : '))
#print(len(List))
n=0
newList=[]
while n < len(List):
	#print('lenght no:',n)
	if p > List[n]:
		#print('this number is less then',p,' in list: ', List[n])
		num=List[n]
		newList.append(num)
		#print(newList)
		n=n+1
	else:
		#print('no number is less then',p, ':')
		n=n+1

print('This is the final list which contains number less then ',p,':',newList)
