import time

special_char = ['$', '#', '@']
isvalid = True

# Signup page

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
user_email = input("Enter your email address:\n")
password = input("Enter a password:\n")

# Password Validation

if len(password) < 6:
     print('Password length should be at least 6')
     isvalid = False
if len(password) > 16:
     print('Password length should not be greater than 16')
     isvalid = False

if not any(char.isdigit() for char in password):
     print('Password should have at least one number from [0-9]')
     isvalid = False

if not any(char.isupper() for char in password):
     print('Password should have at least one uppercase letter from [A-Z]')
     isvalid = False

if not any(char.islower() for char in password):
     print('Password should have at least one lowercase letter from [a-z]')
     isvalid = False

if not any(char in special_char for char in password):
     print('Password should have at least one of the symbols [$ # @]') 
     isvalid = False
     
if isvalid:
     print("Password is valid")
else:
    print("Password is invalid!")
time.sleep(2)
print("\n")
print("Please wait...")

print("\n")
print("Authenticating...")

print("\n")
print("Account Successfully Created!")
print("\n")

# Login Page

print("Login:\n")
email = input("Enter Email:\n")
user_password = input("Enter Password:\n")
print("\n")

if user_email is email and password is user_password:
    isvalid = True
