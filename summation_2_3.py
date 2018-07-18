# summation_2_3.py
# Summation of a set of numbers
# Given a set of n numbers design an algorithm that adds these numbers
# and returns the resultant sum. Assume n is greater than or equal to zero.
#
# Algorithms
# 1. Prompt and read in the number of numbers to be summed.
# 2. Initialise sum for zero numbers.
# 3. While less than n numbers have been summed repeatedly do
#    (a) read in next number,
#    (b) compute current sum by adding the number read to the most recent sum.
# 4. Write out sum of n numbers.

number_of_elements = int(input("Enter the number of numbers to be added: "))
sum = 0.0
i =0

while i < number_of_elements:
    element = float(input("Enter the value of number to be added: "))
    sum += element
    i += 1

print("\nThe sum of {0} numbers is {1:.2f}".format(number_of_elements, sum))
input("\n\nPress the enter key to exit.")




