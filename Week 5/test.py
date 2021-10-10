import pickle
import ast
import os
os.system("cls")

dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'}
dictionary["names"] = ["paul","pete","kelly"]
test = open("test.txt", "r")
# data = str(dictionary)
data = test.read()

dict_to_string = ast.literal_eval(data)
print(dict_to_string)