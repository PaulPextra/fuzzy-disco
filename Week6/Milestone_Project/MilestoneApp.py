import ast
import time
import os
os.system("cls")

def password_isvaid(password):
    '''Password Validation Function'''
    if (len(password) < 6) or (len(password)>16):
        print("Password length should not be less than 6")
        isValid = False
    elif not any(char.isdigit() for char in password):
        print("Password should contain at least a number")
        isValid = False
    elif not any(char.islower() for char in password):
        print("Password should contain at least a lowercase letter [a-z]")
        isValid = False
    elif not any(char.isupper() for char in password):
        print("Password should contain at least a uppercase letter [A-Z]")
        isValid = False
    else:
        isValid=True
        
    return isValid


def write_to_file(data, username = None):
    '''Writing/Storing User Data And Note to Text File'''

    # Writing/storing User Note to a note text file if the username exist.
    if username is not None:
        file = f'Week6/Milestone_Project/{username}.txt'
        with open(file, 'w') as note_file:
            note_file.write(data)
        return
    # Writing/storing user data to users text file.
    file = 'Week6/Milestone_Project/users.txt'
    with open(file, 'w') as data_file:
        data_file.write(f'{data}')
    return

def read_file_data(username = None):
    '''Reading stored User Data and notes from Text File'''
    
    # Reading User Note File
    if username is not None:
        user_note = f'Week6/Milestone_Project/{username}.txt'
        try:
            with open(user_note, 'r') as file:
                notes = file.read()
                return notes
        except Exception as e:
            return False

    # Reading User Data file   
    user_file = 'Week6/Milestone_Project/users.txt'
    
    with open(user_file, 'r') as users:
        user_data = ast.literal_eval(users.read())
    
    return user_data

user_data = read_file_data()

keep_running = True

while keep_running:
    activity = input("Press 'l' to Login or 's' to Signup:\n>>> ").lower()
    
    if activity == 's':
        firstName = input("Enter First Name:\n>>> ").title()
        lastName = input("Enter Last Name:\n>>> ").title()
        userName = input("Enter UserName:\n>>> ").lower()
        email = input("Enter Email:\n>>> ").title()
        password = input("Enter Password:\n>>> ")
        re_password = input("Confirm Password:\n>>> ")

        print("Validating username...")
        time.sleep(2)

        if userName in user_data.keys():
            print("Username already exists. Try again")
            continue

        print("validating password...")
        time.sleep(2)

        if password == re_password and password_isvaid(password):
            data = [('First Name',firstName),('Last Name', lastName), ('Email', email), ('Password', password)]
            user_data[userName] = {}
            user_data[userName].update(data)

            time.sleep(1)

            print(f"\nHello {firstName}, Your Account has been created and Activated Successfully!\n")
            print("\nPlease Login To Setup Your Profile.\n")
    
    elif activity == 'l':

        userName = input("Enter Username:\n>>> ").strip()
        password = input("Enter Password:\n>>> ").strip()

        if userName in user_data.keys():

            user_details = user_data.get(userName, False)

            if user_details and user_details.get('Password') == password:

                time.sleep(1)

                print(f"Welcome {user_details.get('First Name')},\n")

                login = True

                while login:
                    time.sleep(1)
                    progress = input("1. View Profile\n2. Edit Profile\n3. Change Password\n4. Create Note\n5. View Note\n6. Edit Note\n7. Clear Note\n0. Logout\n\nEnter An Option:\n>>> ")

                    if progress == '1':
                        time.sleep(1)

                        print(f"First Name: {user_details['First Name']}\nLast Name: {user_details['Last Name']}\nEmail: {user_details['Email']}\nPassword: {user_details['Password']}\n")
                            
                        time.sleep(1)

                        progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")

                        if progress == 'y':
                            continue
                        else:
                            break

                    elif progress == '2':
                        edit_profile = True

                        while edit_profile:
                            time.sleep(1)
                            action = input("1. Edit First Name\n2. Edit Last Name\n3. Edit Email\n>>> ")
                            if action == '1':
                                new_firstName = input("Enter First Name:\n>>> ")
                                user_details['First Name'] = new_firstName

                                print("\n")

                                progress = input("Press 'y' to continue or any other key to go back:\n>>> ")
                                if progress == 'y':
                                    continue
                                else:
                                    break
                            elif action == '2':
                                new_lastName = input("Enter last Name:\n>>> ")
                                user_details['Last Name'] = new_lastName

                                print("\n")

                                progress = input("Press 'y' to continue or any other key to go back:\n>>> ")
                                if progress == 'y':
                                    continue
                                else:
                                    break

                            elif action == '3':
                                new_email = input("Enter Email:\n>>> ")
                                user_details['Email'] = new_email

                                print("\n")

                                progress = input("Press 'y' to continue or any other key to go back:\n>>> ")
                                if progress == 'y':
                                    continue
                                else:
                                    break
                            else:
                                break
                    elif progress == '3':
                        current_password = input("Enter Current Password:\n>>> ")
                        password_update = input("Enter New Password:\n>>> ")

                        user_data[userName]['Password'] = password_update

                        time.sleep(1)

                        print("Password Successfully Changed!\n")

                        print("\n")

                        progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")

                        if progress == 'y':
                            continue
                        else:
                            break
                    elif progress == '4':
                        note = input("Type Note:\n>>> ")
                        write_to_file(note, userName)
                        time.sleep(1)
                        print("\nNote successfully saved.\n")

                        print("\n")

                        progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")
                        if progress == 'y':
                            continue
                        else:
                            break

                    elif progress == '5':
                        user_note = read_file_data(userName)

                        if user_note == False:
                            time.sleep(1)
                            print("You currently have no notes. Plese add one.\n")
                        else:
                            time.sleep(1)
                            print(user_note)
                            print("\n")
                            progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")
                            if progress == 'y':
                                continue
                            else:
                                break

                    elif progress == '6':
                        time.sleep(1)
                        print("Note that editing this note overwrites the original content. Copy your contents to a safe place before proceeding.\n")
                        note_content = input("Write Note:\n>>> ")
                        write_to_file(note_content, userName)
                        print("\n")
                        progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")
                        if progress == 'y':
                            continue
                        else:
                            break

                    elif progress == '7':
                        write_to_file("", userName)
                        time.sleep(1)
                        print("\nNote Cleared successfully.\n")
                        print("\n")
                        progress = input("Press 'y' to continue or any other key to Quit:\n>>> ")
                        if progress == 'y':
                            continue
                        else:
                            break

                    elif progress == '0':
                        time.sleep(1)
                        print("It was Nice Having You. Good Bye!\n")
                        login = False
                        write_to_file(user_data)
                    else:
                        time.sleep(1)
                        print("Invalid Option!\n")
                        break

            elif user_details and user_details.get('Password') != password:
                time.sleep(1)
                print("Wrong Password!\n")
                time.sleep(1)
                print("\n")
                progress = input("Press 'r' To Reset Your Password or any other key to Quit:\n>>> ")

                if progress == 'r':
                    new_password = input("Enter New Password:\n>>> ")
                    re_new_password = input("Confirm New Password:\n>>> ")

                    if new_password == re_new_password:
                        user_data[userName]['Password'] = new_password
                        time.sleep(1)
                        print(f"Hello {user_data[userName]['First Name']}, Your Password Reset was Successful!\n")
                        continue
                        
                    else:
                        time.sleep(1)
                        print("Password Doesn't Match!")
                        continue
            else:
                time.sleep(1)
                print("Login Failed!\n\nPlease Enter A Valid Username and Password.")
                continue
    else:
        print("Sorry to see you go!\n")
        break

write_to_file(user_data)


