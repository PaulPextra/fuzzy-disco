import time
for i in range(100):
     user_data = {}
     special_char = ['$', '#', '@']
     isvalid = True

     Activity = input("\nLogin or Signup?\n").lower()

     # Login Page
     if Activity == "login":
          email = input("Enter Email:\n")
          user_password = input("Enter Password:\n")
          print("\n")
          if user_email == email and password == user_password:
               isvalid = True
               print("Login Successful!\n")
          else:
               print("Invalid Login Details!")
               continue

     # Signup page
     elif Activity == "signup":
          first_name = input("Enter first name:\n")
          last_name = input("Enter last name:\n")
          user_email = input("Enter your email address:\n")
          password = input("Enter a password:\n")
          re_password = input("Confirm password:\n")

          # Password Validation
          if password != re_password:
               print("Please enter matching password")
               continue

          elif len(password) < 6:
               print('Password length should be at least 6')
               isvalid = False

          elif len(password) > 16:
               print('Password length should not be greater than 16')
               isvalid = False

          elif not any(char.isdigit() for char in password):
               print('Password should have at least one number from [0-9]')
               isvalid = False

          elif not any(char.isupper() for char in password):
               print('Password should have at least one uppercase letter from [A-Z]')
               isvalid = False

          elif not any(char.islower() for char in password):
               print('Password should have at least one lowercase letter from [a-z]')
               isvalid = False

          elif not any(char in special_char for char in password):
               print('Password should have at least one of the symbols [$ # @]') 
               isvalid = False
               continue
          else:
               user_data[user_email] = password
               print(user_data)
