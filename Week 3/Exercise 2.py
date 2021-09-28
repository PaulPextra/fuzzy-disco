# Exercise 1:
'''
Question: Change Brad's salary to 8500 from the given python dictionary.

'''
sampleDict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary'] = 8500
print(sampleDict)

# Exercise 2:

'''
Users = {
    'user name': {'first name': 'first name',
                'last name': 'last name'}
}
Write a program that takes in the user details and
saves it in the user dictionary following the format above.
'''

user_dict = {}
user_firstName = input('Enter your first name:\n')
user_lastName = input('Enter your last name:\n')
username = user_firstName[:3] + user_lastName[-2:]
user_dict[username] = {}
user_dict[username].update({'first name': user_firstName})
user_dict[username].update({'last name': user_lastName})
print(user_dict)

# Exercise 3:
'''
Given the list below:
[2,2,4,6,7,2,4,4,3,6,2,1]
Write a program to remove duplicates from the list and sort it.
Expected output: [1,2,3,4,5,6,7]
'''
my_list = [2,2,4,6,7,2,4,4,3,6,2,1]
list_to_set = set(my_list)
new_list = list(list_to_set)
new_list.sort()
print(new_list)



# Exercise 3:
'''
Write a program to convert a list of multiple integers to a single integer.
['11', '55', '33']
Expected output: 115533
'''

multi_integers = ['11', '55', '33']
integer_to_strings = ''.join(multi_integers)
print(integer_to_strings)



# Exercise 4:
'''
Write a program to unpack a tuple into serveral variables
'''

my_tupple = ('stella', 'Ejiro', 'Tosin')

a,b,c = my_tupple
print(a)
print(b)
print(c)


# Exercise 5:
'''
Write a program to convert the tuple below to a string. 
('u', 'n', 'i', 'v', 'e', 'l', 'c', 'i', 't', 'y')
Expected output: 'univelcity'
'''
my_tuple_ = ('u', 'n', 'i', 'v', 'e', 'l', 'c', 'i', 't', 'y')
tuple_to_string = ''.join(my_tuple_)
print(tuple_to_string)

# Exercise 6:

english_num = int(input())
english = input()
french_num = int(input())
french = input()

word_english = set(english.split())
word_french = set(french.split())
final = word_english.symmetric_difference(word_french)
print(len(final))