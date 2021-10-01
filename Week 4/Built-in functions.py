# input() function - allows interaction between the user and the python code.

# sum() function - sums up all the items in the iterable and returns the total.

# lambda() function - 

# map() - 
# Example:

# li = [1,2,3,4,5]
# sqr = list(map(lambda i : i**2, li))
# print(sqr)


# Class work

'''
Write a program that takes input from the user asking him for the 
a list of the total prices of items bought in 7 days seperated by a comma.
1. calculate the sum
2. calculate the average.

Return a student(standard output) telling him how much (s)he has spe
'''

price_list = input("Enter a list of numbers:\n").split(",")
total = list(map(lambda string : int(string), price_list))
sum_total = sum(total)
average = sum_total / len(total)
print(sum_total)
print(average)

# zip() function - 

# Example:
c = ["002", "014", "029"]
p = [2000, 4000, 2015]
d = dict(zip(c, p)) # converting to dictionary
l = list(zip(d, p)) # converting to list
print(d)
print(l)

# enumerate() function - 

# Example:
# enumerate_c = list(enumerate(c))
# print(enumerate_c)

# filter() function - 

# Example:
# mylist = [2,3,5,7,8,20,4,1,9]
# filtered_list = list(filter(lambda x : x % 2 != 0, mylist))
# print(filtered_list)

# range() function - 
# Example:
# print(list(range(1,6,2)))

