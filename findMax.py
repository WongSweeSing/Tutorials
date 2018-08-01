# findMax.py
# To find the maximim value in an array
# input: An array of number
# output : the maximum number in the array. If there multiple numbers with the same
# maximum value. It will just choose of them

anArray = [239, 25, 30.5, 1, 8]

i = 0
j = 0 
arrayLength = len(anArray)

while j < arrayLength:
	if anArray[i] < anArray[j]:
		i = j
	j += 1
	
print("The maximum value in array is {}".format(anArray[i]))
	

	
