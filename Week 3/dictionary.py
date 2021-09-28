# Dictionary - collection of key-value paired data in curly braces.

my_diction = {'pet': 'Dog', 'color': 'Brown'}
my_diction['color'] = 'Red' # changing the value of color.
print(my_diction)
# key error is raised when the key doesn't exist.

# Dictionary Methods

# copy() Method
# Example: 
dictionary = my_diction.copy()
print(dictionary)

# get() Method
# Example:
print(my_diction.get('pet'))

# Adding new key-value pair to a dictionay
# Example 1:
our_diction = {'car': 'Honda'}
our_diction['country'] = 'Nigeria'
print(our_diction)

# Example 2: 
'''
Get an input from the user ask for his course and score.
Add his course to the courses and his score.
'''
my_dict ={'name': 'Jerry',
'courses' : ['Data Science', 'Backend'],
'scores': {'Data science': 20,
'Backend': 15.7}}

user_course = input('Enter your course:\n')
user_score = input('Enter your score\n')
my_dict['courses'].append(user_course)
my_dict['scores'][user_course] = user_score

print(my_dict)

# items() Method - getting all the items in a dictionary as a group of tuples.
# Example:
print(my_dict.items())

# update() Method - 
# Example:
my_dictionary = {
    'name': 'John',
    'gender': 'Male'
}

my_dictionary.update({'key': 'Value'})
print(my_dictionary)
list_of_tuples = [('john', 'Abuja'), ('Nigeria', 'Canada')]
my_dictionary.update(list_of_tuples)
print(my_dictionary)

# pop() Method
# Example:
val = my_dict.pop('scores')
print(my_dict)
print(val)
my_dict['results'] = val # Alternatively - my_dict.update({'results':val})
print(my_dict)

a = my_dict['results']
print(type(a))

print(type(my_dict.keys()))