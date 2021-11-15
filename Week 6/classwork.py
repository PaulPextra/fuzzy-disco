import os
os.system('cls')

# Question 1:
'''
Create a vehicle class with maspeed and millage instance attributes.
create that calculates acceleration.
'''

class vehicle():
    def __init__(self, max_speed, millage):
        self.max_speed = max_speed
        self.millage = millage

    def acceleration(self, time):
        a = 2*(self.millage) / (time**2)
        return a

honda = vehicle(120, 100)
print(honda.acceleration(60))


