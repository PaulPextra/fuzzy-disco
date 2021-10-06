# function - segmentation of block of codes which will run when called.
'''
syntax: 
def func_name() # Defining a function
    Block of code
func_name() - # calling a function
'''
# Parameters -
# Arguments -

# Example:
def add_num(x,y):
    a = x + y

def add_num_2(x,y):
    a = x + y
    return a

a = add_num(2,4) # output = None. no return statement.
b = add_num_2(2,4) # output = 6. Return statement.
print(a)
print(b)

# Return Statement - returns the output of the function.
'''
Return statemennt gives the ability to save the output to a variable.
'''

# Arbitrary Argument - used when the number of argument is unknown
'''
syntax:
def fun(*arg):
    block of code
fun(Arg1, Arg2, Arg3)
'''