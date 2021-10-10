# Write Mode "w"

# myfile = open('Week 5\paul.txt', mode='w')
# myfile.write("This is line 1\nThis is line 2\n\tThis is a tab.")

# myfile.writelines(['\nThis is line 1.\n', 'This is line 2.\n', '\tThis is a tab.'])

# Append Mode "a"

# myfile = open('Week 5\paul.txt', mode='a')
# myfile.writelines(['\nThis is line 1.\n', 'This is line 2.\n\t', 'This is a tab.'])

# Read Mode "r"
# myfile = open('Week 5\paul.txt', mode='r')
# myfile.writelines(['\nThis is line 1.\n', 'This is line 2.\n\t', 'This is a tab.'])
# text = myfile.readlines()
# print(text)

# Using the "With" keyword on write mode "w"
with open('mary.txt', 'w') as paul:
    paul.write("My name is paul")
paul.write("I have risen")

# Using the "With" keyword on read mode "r"
with open('mary.txt', 'r') as mercy:
    favour =mercy.read()
    print(favour)

#  converting string type dictionary to a dictionary type 
import ast
a = ast.literal_eval(favour)
print(a)