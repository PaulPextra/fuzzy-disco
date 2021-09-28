# Tuple: collection of data in enclosed in parentesis().

# Example
t1 = (False, 'True', 100)
t2 = (1, 2, 3)

# Tuples can be added together using the "+" operator.

t3 = t1 + t2 # t3 is a new tuple
print(t3)

# Tuples can be deleted.
# Tuples cannot be updated.
# Tuples can be created without parentesis.
# Tuples are seperated by a comma.
# Tuples can be unpacked. 

aTuple = ('red', 'white', 'blue')
a, b, c = aTuple # Unpacking a tuple.
print(a)

my_tuple = 'This', 'is', 'a', 'tuple'
print(my_tuple)
print(type(my_tuple))