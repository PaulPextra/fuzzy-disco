# Question 1 Solution:

# special_char = ['$', '#', '@']
# isvalid = True
# password = input('Enter a password:\n')

# if len(password) < 6:
#      print('Password length should be at least 6')
#      isvalid = False
# if len(password) > 16:
#      print('Password length should not be greater than 16')
#      isvalid = False

# if not any(char.isdigit() for char in password):
#      print('Password should have at least one number from [0-9]')
#      isvalid = False

# if not any(char.isupper() for char in password):
#      print('Password should have at least one uppercase letter from [A-Z]')
#      isvalid = False

# if not any(char.islower() for char in password):
#      print('Password should have at least one lowercase letter from [a-z]')
#      isvalid = False

# if not any(char in special_char for char in password):
#      print('Password should have at least one of the symbols [$ # @]') 
#      isvalid = False
     
# if isvalid:
#      print("Password is valid")
# else:
#     print("Password is invalid!") 



# Question 2 Solution:

import time

Side_A = int(input('Enter the length of side A:\n'))
Side_B = int(input('Enter the length of side B:\n'))
Side_C = int(input('Enter the length of side C:\n'))
print('\n')
print('Checking if the Triangle is an Equilateral, an Isosceles, or a Scalene Triangle...')
time.sleep(2)
print('\n')
if (Side_A == Side_B == Side_C):
    print('The Triangle is an Equilateral Triangle')
elif (Side_A == Side_B or Side_B == Side_C or Side_A == Side_C):
    print('The Triangle is an Isosceles Triangle')
else:
    print('The Triangle is a Scalene Triangle')


# Question 3 Solution:

# Original_list = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]
# sorted_list = sorted(Original_list, key = lambda k : k['color'])
# print(sorted_list)