#Factorial Of N

def fact(n):    #Time complexity T(n) = T(n - 1) + 1    Therefore, O(n)
    if(n == 0):
        return 1
    else:
        return n * fact(n - 1)
    

n = 5
print(fact(n))