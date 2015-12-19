from functools import reduce

def main(): 
    number = [4, 7, 8, 5, 2, 9, 13, 22, 3 ]
    print(number)
    
    minFunction = iterateList(number)
    print( "The minimum is ", minFunction() )

def iterateList(nums):
    
    #the min function
    def getMinimun(a,b):
        if a > b :
            return b 
        else :
            return a
    
    #iterate over the list    
    def getCalcMin():    
        return reduce(lambda a,b: getMinimun(a,b), nums)

    # returns a function fron a function
    return getCalcMin

# This code show Python Function Composition    
main()