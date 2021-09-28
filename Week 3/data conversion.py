# Data Conversion - converting from one data type to another data type.

my_dict = {
'name': 'Jerry',
'courses' : ['Data Science', 'Backend'],
'scores': {
    'Data science': 20,
    'Backend': 15.7
    }
}

a = my_dict['scores']
print(type(a)) # checking for the data  type.

# list to str
# Example:
my_list =  [1,2,3,4]
print(str(my_list))

# dictionary to list
# Example:
print(list(my_dict))

