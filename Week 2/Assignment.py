# 1.  Write a Python program to clone a list. my_list = ['this', True, 'student', 45, 66.43]
# 2. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output = ['Green', 'White', 'Black']
# 3. Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# 4. Exercise 7: Add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


# Problem 1 Solution.

my_list = ['this', True, 'student', 45, 66.43]

cloned_list = list(my_list)

print(cloned_list)

# Problem 2 Solution.

list_of_animals = ['Dog', 'Cat', 'Lion', 'Horse', 'Monkey', 'Goat', 'Elephant', 'Donkey']

list_of_animals.pop(0)

list_of_animals.pop(3)

list_of_animals.pop(3)

print(list_of_animals)

# Problem 3 Solution.

colour_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

user_fav_colour = input('Enter Your Favourite Colour:\n')

colour_list.append(user_fav_colour)

print(colour_list)


# Problem 4 Solution.

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)

















