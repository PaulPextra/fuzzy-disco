# Set: collection of data in curly braces {}.

# Example of a set
my_set = {23, 34, 'cat', True}

'''
The difference between remove() and discard() method is, 
remove() throws an error when a specified item doesn't exist in the set while discard will not throw an error.

'''

s = {'True', 'Born', 45, 'water'}
s.remove('Johnson') # Error will be raise.
print(s)

s.discard('Johnson') # No Error will be raised.

print(s)

# union() Method : combining the values or contents of two or more sets together.
s = {'True', 'Born', 45, 'water'}
b = {'mary', 'Favour', 'Tunde', 50}

u = s.union(b)
print(u)

# intersection() method: what is common between two or more sets
a = s.intersection(b)
print(a) # output is an empty set.

# Alternatively - The operator (&) can also be used as the intersection operator.

s = set('Hack')
t =  set('Rank')
print(s & t)


# difference() Method: unique value between two or more set.
set_a = {100, 200, 300, 400}
set_b = {500, 100, 300}
output = set_a.difference(set_b)
print(output)

# update() Method: updates a given set with the values of another set.
s.update(b) # Updating set s with the value of set b.
print(s)

# Symmetric difference (A - B) union (B - A)
# Example:
x = {2,4,6}
y = {3,6,9}
output = x.symmetric_difference(y)
print(output)

# pop() Method: randomly removes a value from a given set.
z = {3,5,6,7,8}
z.pop()
print(z)

