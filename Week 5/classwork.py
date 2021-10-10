num_list = [2,3,4,5,2,4,5,2,6,2,7,8,9,10,11]

# For Mean
def mean(num):
    num_sum = sum(num)
    size = len(num)
    result = num_sum // size
    return result
print(mean(num_list))

# For Median
def median(num):
    sorted(num)
    size = len(num)
    mid_point = size//2
    if size % 2 != 0:
        return num[mid_point]
    else:
        first = num[mid_point - 1]
        second = num[mid_point]
        return (first + second)/2
    
print(median(num_list))

# For Mode 
def mode(num):
    dict = {}
    for i in num:
        if i in dict:
            dict[i] = dict.get(i, 0)
            dict[i] += 1
        else:
            dict[i] = 1
    max_key = max(dict, key= dict.get)
    # [key for key, value in dict.items() if value == max(dict.values())]
print(mode([2, 3, 5, 2, 5, 2, 2, 7, 11]))


# For Standard Deviation
def standard_deviation(num):
    size = len(num)
    m = mean(num)
    a = [((i - m)**2) for i in num]
    summation = sum(a)/size
    result = summation ** 0.5
    return result
print(standard_deviation(num_list))


# For Variance 
def variance(num):
    sd = standard_deviation(num)
    result = sd**2
    return result
print(variance(num_list))

# For Prime Numbers
def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(prime(5))

def prime_in_list(num):
    return list(filter(lambda x: prime(x), num))
print(prime_in_list(num_list))