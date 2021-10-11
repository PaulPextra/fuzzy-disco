
from datetime import datetime
import random, time 
import ast
import os
os.system("cls")

user_data = {}
transaction_log = {}
validPin = True
keep_running = True
date = datetime.now()
now = date.strftime('%x')

def update_transaction_log(Amount, Trans_type, Transaction, Account_number):
    """This function takes in the amount and other transaction details. Then it updates the transaction dictionary. It doesn't return anything."""
    
    trans_data = {
        'Amount':Amount,
        'Trans_type':Trans_type,
        'Transaction':Transaction
        }

    transaction_log[Account_number].append(trans_data)

def generate_acc_num():
    Random_num = [str(i) for i in range(10)]
    Start_Num = ["1"]
    Start_Num.extend([random.choice(Random_num) for i in range(9)])
    Account_number = "".join(Start_Num)
    
    if Account_number in user_data.keys():
        return generate_acc_num() # Recursive Function
    
    return Account_number

while keep_running:
    Activity = input("Login or Create Account?\n>>> ").lower()

    # User Login Section
    if Activity == "login":
        Account_number = input("Enter Your Account Number:\n>>> ").strip()
        Pin = input("Enter Your Pin:\n>>> ").strip()
        if (len(Pin) < 4) or (len(Pin) > 4):
            print("Pin should be 4 digits!\n")
            continue

        # Reading User Data from Text File
        # with open("customer.txt", "r") as login:
        #     # login_data = login.read()
        #     # str_dict = ast.literal_eval(login_data)

        account_details = user_data.get(Account_number, False)
        if account_details and account_details.get('Pin') == Pin:
            time.sleep(2)
            print(f"\nWelcome, {user_data[Account_number]['First Name']}!\n")
        else:
            time.sleep(1)
            print("Login Failed!\n\nNo active customer for this account number.")
            
        logged_in = True

        while logged_in: 

            # ATM Options:
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

                    #save transaction detail
                    update_transaction_log(Amount,"Debit", "Withdrawl", Account_number)

                    # Storing Customer Transaction Log to a text file
                    with open("customer.txt", "a") as log:
                        log.write(f"{transaction_log}\n")

                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print(f"Debit!\nAmt:NGN{Amount}\nTime:{now}\nAvailable Balance:NGN{user_data[Account_number]['Balance']}\n")
                    time.sleep(1)
                    progress = input("Press 'y' to Continue or 0 tocreate account Logout!\n\n>>> ").lower()
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
                update_transaction_log(Amount,"Credit", "Deposit", Account_number)

                # Storing Customer Transaction Log to a text file
                with open("customer.txt", "a") as log:
                    log.write(f"{transaction_log}\n")

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

                        #save transaction detail
                        update_transaction_log(Amount,"Debit", "Transfer", Account_number)

                        # Storing Customer Transaction Log to a text file
                        with open("customer.txt", "a") as log:
                            log.write(f"{transaction_log}\n")

                        recipient['Balance'] += Amount

                        #save transaction detail
                        update_transaction_log(Amount,"Credit", "Transfer", recipient_account)

                        # Storing Customer Transaction Log to a text file
                        with open("customer.txt", "w") as log:
                            log.write(f"{transaction_log}\n")
                            
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
                if len(transaction_log[Account_number]) > 0:
                    last_5_transactions = transaction_log[Account_number][-5:]

                    print("\nTransaction in Progress...\n")
                    time.sleep(2)
                    print(f"Hello {user_data[Account_number]['First Name']}, Here is Your Account Statement:\n")
                    for transaction in last_5_transactions:
                            print("Amount: ", transaction['Amount'])
                            print("Transaction Type: ", transaction['Trans_type'])
                            print("Transaction Ref.: ", transaction['Transaction'])
                else:
                    print("You have not made any transactions. Please make a transaction.")
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

                Account_number = generate_acc_num()

                data = [("First Name", firstName),("Last Name", lastName), ("Pin", Pin), ("Balance", 0)]
                user_data[Account_number] = {}
                user_data[Account_number].update(data)

            # Storing Customer Data to a text file
            with open("customer.txt", "a") as Data:
                Data.write(f"{user_data}\n")

            #Create Empty Transaction log
            transaction_log[Account_number] = []

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
    
