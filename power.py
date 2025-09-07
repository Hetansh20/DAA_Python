# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base ** exponent

# Iterative Approch
def power(base, exponent):    #Time Complexity: O(n)
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Recursive Approch
def recursive_power(base, exponent):   #time complexity T(n) = T(exp - 1) + 1     Therefore, O(n)
    if exponent == 0:
        return 1
    else:
        if (exponent < 0):
            exponent = abs(exponent)
            return 1 / recursive_power(base, exponent)
        else:
            return base * recursive_power(base, exponent - 1)
        
# Optimized Approch
def optimized_power(base, exponent):   #time complexity O(logn)
    if(exponent == 0):
        return 1
    temp = optimized_power(base, exponent // 2)
    if(exponent % 2 == 0):
        return temp * temp
    else:
        return base * temp * temp

    
a = 2
b = 5
print(optimized_power(a, b))
# print(recursive_power(a, b)) 
# print(power(a, b))