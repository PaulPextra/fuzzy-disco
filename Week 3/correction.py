# Assignment 1 Correction.

# Question 1:

my_list = ['this', True, 'student', 45, 66.43]
cloned_list = my_list.copy()
print(cloned_list)

# Question 2:

Sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

Sample_list.pop(0)
Sample_list.pop(3)
Sample_list.pop(3)
print(Sample_list)

# Question 3:

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
user_colour = input('Enter your favourite color:\n')
color_list.append(user_colour)
print(color_list)

# Question 4:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
