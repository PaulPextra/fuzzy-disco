# Loops: way of going over a block of code.

# 1. For loop
# 2. while loop

# Example of for loop:
for i in range(5):
    print(i + 1)

# List Comprehension
a = [1,2,3,4,5,6,7,8,9]
b = [i for i in a if i%2 == 0]
print(b)

a = [(0, 'sheldon'), (1, 'penny')]
for e in a:
    print(e[0])

# Nested for loop:

# Example:
a = [0, 1, 2]
b = [2, 4, 6]
c = []

for i in a:
    for x in b:
        c.append(i + x)
print(c)


# ClassWork:

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for x, y in zip(list1, list2):
    print(x, y)

# Example of a while loop:

# Eg 1:
x = 10
while x > 0:
    print(x)
    x-= 1

# Eg 2:
y = True
while y:
    print("I am a boy")
    y = False

