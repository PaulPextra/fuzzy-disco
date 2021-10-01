
'''
# Question.
Build a simple bank program that:
1. Allows customers to create account with pin and automatically generate account number.
2. Customers can login using their account number and pin
3. Can withdraw money
4. Can deposit money
5. Can transfer money to other customers in the bank program
'''
import random, time
user_data = {}
balance = 0
validPin = True

for i in range(100):
    Activity = input("Login or Create Account?\n>>> ").lower()

    # User Login Section
    if Activity == "login":
        Pin = input("Enter Your Pin:\n>>> ").strip()
        if (len(Pin) < 5) or (len(Pin) > 5):
            print("Pin shouldn't be greater/less than 5 digits!\n")
            continue
        Account_number = input("Enter Your Account Number:\n>>> ").strip()
        time.sleep(2)
        if Pin in user_data.keys():
            actual_account_number = user_data.get(Pin)

            if actual_account_number == Account_number:
                print("\nLogin Successful!\n") 
                time.sleep(1)
            else:
                print("Wrong Pin/Account Number!\n")
                continue
        else:
            print("\nThere Is No Active User With This Pin!\n")
            continue
        # ATM Options:
        for i in range(4):
            con = input("1. Withdraw\n2. Deposit\n3. Transfer\n4. Check Balance\n0. Quit!\n>>> ")
            
            # Withdrawal Option
            time.sleep(1)
            if con == "1":
                withdraw = int(input("Enter Amount:\n>>> "))
                if withdraw > balance:
                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print("Insufficient Fund!")
                    continue
                else:
                    balance = balance - withdraw
                    time.sleep(2)
                    print(f"Transaction Successful!\n\nYour Account Balance is ${balance}\n")
                    time.sleep(1)
                    con = input("Press 'y' to Continue and Any key to Quit!\n\n>>> ").lower()
                    print("\n")
                    if con == 'y':
                        continue
                    else:
                        print("please select a valid option!\n")
                        break

            # Deposit Option
            elif con == "2":
                deposit = int(input("Enter Amount:\n>>> "))
                balance = balance + deposit
                print("\nTransaction in Progress...\n")
                time.sleep(2)
                print(f"Transaction Successful!\n\nYour Account Balance is ${balance}\n")
                time.sleep(1)
                con = input("Press 'y' to Continue and Any key to Quit!\n\n>>> ").lower()
                print("\n")
                if con == 'y':
                    continue
                else:
                    print("please select a valid option!\n")
                    break

            # Transfer Option
            elif con == "3":
                transfer = int(input("Enter Amount:\n>>> "))
                recipient = input("Enter Recipient Account Number:\n>>> ")
                if (recipient == user_data.get(Pin)):
                    user_data[recipient].update({"balance": balance})
                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print("Transaction Successful!")
                else:
                    print("Transaction Failed!\n\nAccount Number Not Found in Our Data-Base.")
                    time.sleep(1)
                    con = input("Press 'y' to Continue and Any key to Quit!\n\n>>> ").lower()
                    print("\n")
                if con == 'y':
                    continue
                else:
                    print("please select a valid option!\n")
                    break

            # Check Balance Option
            elif con == "4":
                print("\nTransaction in Progress...\n")
                time.sleep(2)
                print(f"Your Account Balance is: ${balance}\n")
                time.sleep(1)
                con = input("Press 'y' to Continue and Any key to Quit!\n\n>>> ").lower()
                print("\n")
                if con == 'y':
                    continue
                else:
                    print("please select a valid option!\n")
                    break

            # Quit Option
            elif con == "0":
                print("Thank You for Banking With Us!\n")
                break
            else:
                print("Please Enter a Valid Option!\n")
            continue

    # Signup/Create Account Section

    elif Activity == "create account":
        for i in range(100):
            Pin = input("Enter a 5 digit pin:\n>>> ")
            re_Pin = input("Confirm Pin:\n>>> ")
            if len(Pin) != 5:
                print("Pin should be 5 digits.")
                validPin = False
            elif Pin != re_Pin:
                print("Pin doesn't match")
                validPin = False
            else: 
                validPin = True
                user_account_num = random.sample(range(11), 9)
                accountNum_str = [str(i) for i in user_account_num]
                Account_number = "".join(accountNum_str)
                time.sleep(1)
                print("\nGenerating Your Account Number...\n")
                time.sleep(2)
                print("Account Number Successfully Generated!")
                print(f"Your Account Number is {Account_number}\n")
                user_data[Pin] = Account_number
                break
        # Continue Option to Login/ Create Account
        con = input("Press 'y' to Continue and Any key to Quit!\n>>> ").lower()
        if con == 'y':
            continue
        else:
            break
    else:
        print("Please Enter a Valid Option!\n")
        continue
    
