from functools import reduce

# Calculates the GCD of the List using Lambda REduce
def gcdList(nums):    
    return reduce(lambda a,b: gcd(a,b), nums)

# Functional GCD    
def gcd( dividend, divisor):
    if divisor == 0 :
        return dividend
    else:
        return gcd(divisor, dividend % divisor) 