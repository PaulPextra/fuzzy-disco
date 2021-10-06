# time module:
# Example:
import time
user = input("Enter Your Name:\n>")
print("Creating account, please wait...")
time.sleep(3)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("Almost there...")
time.sleep(2)
print(f"Welcome {user}, your account has been created!")

# random module:

# Example:
import random
my_list = [2,3,5,6,7,8]
random.shuffle(my_list)
random.choice(my_list)
random.sample(my_list, 3)
random.seed(1)
print(random.randrange(3, 7))

# datetime module:

# Example:
from datetime import datetime
date = datetime.now()

# strftime() function for datetime:

# Example:
print(datetime.strftime(date, "%A, %d %B %Y"))

