
'''
# Bank App Modification.
1. Allow user to check account balance
2. Get the 5 most recent transactions
3. Log transaction details (Debit/Credit)
4. Validate pin before saving
5. Keep user logged in till he logs out.
'''
import random, time 
from datetime import datetime
user_data = {}
# transaction_log = {}
validPin = True
logged_in = True
keep_running = True
date = datetime.now()
now = date.strftime('%x')

while keep_running:
    Activity = input("Login or Create Account?\n>>> ").lower()

    # User Login Section
    if Activity == "login":
        Account_number = input("Enter Your Account Number:\n>>> ").strip()
        Pin = input("Enter Your Pin:\n>>> ").strip()
        if (len(Pin) < 4) or (len(Pin) > 4):
            print("Pin should be 4 digits!\n")
            continue
        account_details = user_data.get(Account_number, False)

        if account_details and account_details.get('Pin') == Pin:
            time.sleep(2)
            print(f"\nWelcome, {user_data[Account_number]['First Name']}!\n") 
        else:
            print("\nThere Is No Active User With This Pin!\n")
            continue

        # ATM Options:
        while logged_in:
            progress = input("1. Withdraw\n2. Deposit\n3. Transfer\n4. Check Balance\n5. Account Statement\n0. Logout!\n>>> ")
            
            # Withdrawal Option
            time.sleep(1)
            if progress == "1":
                Amount = float(input("Enter Amount:\n>>> "))
                if Amount >= user_data[Account_number]['Balance']:
                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print("Insufficient Fund!\n")
                    time.sleep(1)
                    print("Session Expired!\n")

                    progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                    print("\n")
                    if progress == 'y':
                        continue
                    elif progress == "0":
                        time.sleep(1)
                        print("Thank You for Banking With Us!\n")
                        logged_in = False
                    else:
                        print("Invalid option!\n")
                        break
                else:
                    user_data[Account_number]["Balance"] -= Amount
                    transaction_log = {}
                    transaction_log[Account_number] = {}
                    data_ = [("Amount",Amount),("Alert Type","Debit"),("Transaction Type","Withdrawal")]
                    transaction_log[Account_number].update(data_)
                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print(f"Debit!\nAmt:NGN{Amount}\nTime:{now}\nAvailable Balance:NGN{user_data[Account_number]['Balance']}\n")
                    time.sleep(1)
                    progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                    print("\n")
                    if progress == 'y':
                        time.sleep(1)
                        continue
                    elif progress == "0":
                        time.sleep(1)
                        print("Thank You for Banking With Us!\n")
                        logged_in = False
                    else:
                        print("Invalid option!\n")
                        break

            # Deposit Option
            elif progress == "2":
                Amount = float(input("Enter Amount:\n>>> "))
                user_data[Account_number]["Balance"] += Amount
                transaction_log = {}
                transaction_log[Account_number] = {}
                data_ = [("Amount",Amount),("Alert Type","Credit"),("Transaction Type","Deposit")]
                transaction_log[Account_number].update(data_)
                print("\nTransaction in Progress...\n")
                time.sleep(2)
                print(f"Credit!\nAmt:NGN{Amount}\nTime:{now}\nAvailable Balance:NGN{user_data[Account_number]['Balance']}\n")
                time.sleep(1)
                progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                print("\n")
                if progress == 'y':
                    time.sleep(1)
                    continue
                elif progress == "0":
                    time.sleep(1)
                    print("Thank You for Banking With Us!\n")
                    logged_in = False
                else:
                    print("Invalid option!\n")
                    break

            # Transfer Option
            elif progress == "3":
                Amount = float(input("Enter Amount:\n>>> "))
                recipient_account = input("Enter Recipient Account Number:\n>>> ")
                recipient = user_data.get(recipient_account, False)

                if recipient:
                    if Amount >= user_data[Account_number]['Balance']:
                        time.sleep(1)
                        print("Insufficient funds!")
                    else:
                        user_data[Account_number]['Balance'] -= Amount
                        recipient['Balance'] += Amount
                        transaction_log = {}
                        transaction_log[Account_number] = {}
                        data_ = [("Amount",Amount),("Alert Type","Debit"),("Transaction Type","Transfer")]
                        transaction_log[Account_number].update(data_)
                        print("\nTransaction in Progress...\n")
                        time.sleep(2)
                        print(f"Transfer Successful!\nDebit!\nAmt:NGN{Amount}\nTime:{now}\nAvailable Balance:NGN{user_data[Account_number]['Balance']}\n")

                        time.sleep(1)
                        progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                        print("\n")
                        if progress == 'y':
                            time.sleep(1)
                            continue
                        elif progress == "0":
                            time.sleep(1)
                            print("Thank You for Banking With Us!\n")
                            logged_in = False
                        else:
                            print("Invalid option!\n")
                            break
                else:
                    time.sleep(1)
                    print("Transaction Failed!\n\nNo active customer for this account number.")
                    

            # Check Balance Option
            elif progress == "4":
                print("\nTransaction in Progress...\n")
                time.sleep(2)
                print(f"Your Account Balance is NGN{user_data[Account_number]['Balance']}\n")
                time.sleep(1)
                progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                print("\n")
                if progress == 'y':
                    time.sleep(1)
                    continue
                elif progress == "0":
                    time.sleep(1)
                    print("Thank You for Banking With Us!\n")
                    logged_in = False
                else:
                    print("Invalid option!\n")
                    break
            # Print Account Statement Option
            elif progress == "5":
                print("\nTransaction in Progress...\n")
                time.sleep(2)
                print(f"Hello {firstName}, Here is Your Account Statement:\n{transaction_log.get(Account_number)}\n")
                time.sleep(1)
                progress = input("Press 'y' to Continue or 0 to Logout!\n\n>>> ").lower()
                print("\n")
                if progress == 'y':
                    time.sleep(1)
                    continue
                elif progress == "0":
                    time.sleep(1)
                    print("Thank You for Banking With Us!\n")
                    logged_in = False
                else:
                    print("Invalid option!\n")
                    break

            # Logout Option
            elif progress == "0":
                time.sleep(1)
                print("Thank You for Banking With Us!\n")
                logged_in = False
            else:
                print("Please Enter a Valid Option!\n")
            continue

    # Signup/Create Account Section

    elif Activity == "create account":
        for i in range(100):
            firstName = input("First Name:\n>>> ").title()
            lastName = input("Last Name:\n>>> ").title()
            Pin = input("Enter a 4 digit pin:\n>>> ")
            re_Pin = input("Confirm Pin:\n>>> ")
            if len(Pin) != 4:
                print("Pin should be 4 digits.")
                validPin = False
            elif Pin != re_Pin:
                print("Pin doesn't match")
                validPin = False
            else: 
                validPin = True
                Random_num = [str(i) for i in range(10)]
                Start_Num = ["1"]
                Start_Num.extend([random.choice(Random_num) for i in range(9)])
                Account_number = "".join(Start_Num)

                data = [("First Name", firstName),("Last Name", lastName), ("Pin", Pin), ("Balance", 0)]
                user_data[Account_number] = {}
                user_data[Account_number].update(data)
                time.sleep(1)
                print("\nGenerating Your Account Number...\n")
                time.sleep(2)
                print(f"Hello {firstName}, Your account has been successfully activated!")
                print(f"Your Account Number is {Account_number}\nYour current balance is NGN0.\nPlease login to perform other transactions.\nThank You!\n")
                break

        # Continue Option to Login/ Create Account
        progress = input("Press 'y' to Continue and Any key to Quit!\n>>> ").lower()
        if progress == 'y':
            time.sleep(1)
            continue
        else:
            break
    else:
        print("Please Enter a Valid Option!\n")
        continue
    
