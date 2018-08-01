# findMax.py
# To find the maximim value in an array.
# input: A text file with number. First line of file is a header and can be skipped.
# output : the maximum number in the array. If there multiple numbers with the same
# maximum value. It will just choose one of them.

import os

def findMax(file_location, file_name):
      
        """This function finds the maximum value in an array.
        input: A text file with numbers. First line of file is a header and can be skipped
        output : the maximum number in the array. If there multiple numbers with the same
        maximum value. It will just choose one of them. """
        anArray = [] # array for storing the numbers read from text file
        with open(os.path.join(file_location, file_name)) as f: # f is a file handler
                next(f) # first line is a header, can skip this line
                for line in f: 
                        anArray.append(float(line)) # storing the number read from text file to array anArray
                        
        i = 0
        j = 0
        arrayLength = len(anArray)
        
        if not anArray: # special case: an empty array
                return print("The array is empty!\nThere is no maximum value.")
        else:
                while j < arrayLength:
                        if anArray[i] < anArray[j]:
                                i = j
                        j += 1
	
                return print("The maximum value in array is {}".format(anArray[i]))
	
#anArray = [239, 250, 30.5, 1, 1008]
#anArray = [-1]
# file_location = "/Users/JosephineWong/Desktop/Python Programming for Absolute Beginner/How_to_solve_it_by_computer"
# file_name = "numbers.txt"
#anArray = []
findMax("/Users/JosephineWong/Desktop/Python Programming for Absolute Beginner/How_to_solve_it_by_computer", "numbers.txt")

input("\n\nPress the enter key to exit.")
	
