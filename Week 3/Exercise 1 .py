# Exercise 1:

set1 = {10,20,30,40,50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

# Exercise 2:
set_1 = {10,20,30,40,50}
set_2 = {30,40,50,60,70}
set_3 = set_1.union(set_2)
print(set_3)

# Exercise 3:

set_a = {10, 20,30}
set_b = {20, 40, 50}
set_a.difference_update(set_b)
print(set_a)

# Exercise 4:
set_c = {10,20,30,40,50}
set_c.difference_update({10,20,30})
print(set_c)

# Exercise 5:

set_x = {10,20,30,40,50}
set_y = {30,40,50,60,70}
print(set_x.symmetric_difference(set_y))

# Exercise 6:

set_g = {10,20,30,40,50}
set_h = {30, 40, 50, 60, 70}
set_g.intersection_update(set_h) # using intersection_update method
print(set_g.intersection(set_h)) # using intersection method
print(set_g)

# Class work:

from decimal import Decimal
l1 = [11, 12, 0, -17, -18, 20, 0, 40]
positive = []
negative  = []
zero = []
for i in l1:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        zero.append(i)
# print(positive)
# print(negative)
# print(zero)

ratio_p = len(positive) / len(l1)
ratio_n = len(negative) / len(l1)
ration_z = len(zero) / len(l1)

print(round(Decimal(ratio_p), 6))
print(round(Decimal(ratio_n), 6))
print(round(Decimal(ration_z), 6))
