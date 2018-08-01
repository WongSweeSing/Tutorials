# findMax.py
# To find the maximim value in an array.
# input: An array of number
# output : the maximum number in the array. If there multiple numbers with the same
# maximum value. It will just choose of them


def findMax(anArray):
      
        """This function finds the maximum value in an array.
        input: An array of number
        output : the maximum number in the array. If there multiple numbers with the same
        maximum value. It will just choose of them. """

        i = 0
        j = 0
        arrayLength = len(anArray)

        while j < arrayLength:
                if anArray[i] < anArray[j]:
                        i = j
                j += 1
	
        print("The maximum value in array is {}".format(anArray[i]))
	
anArray = [239, 250, 30.5, 1, 1008]

findMax(anArray)

input("\n\nPress the enter key to exit.")
	
