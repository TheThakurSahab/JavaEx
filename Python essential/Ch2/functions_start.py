#
# Example file for working with functions
#

# define a basic function
def basicFunction():
    ab=19
    print(ab)
basicFunction()
# function that takes arguments
def basicFunction1(a, b):
    t=a
    a=b
    b=t
    print(a, b)
basicFunction1(5, 7)
# function that returns a value
def cube(x):
    return x*x*x
print(cube(5))
# function with default value for an argument
def power(num, x=1):
    result=1
    for i in range(x):
        result = result*num
    return result
print(power(2))
print(power(2,3))
print(power(x=2, num=5)) #python let us call the function with reverce order of parameters

#function with variable number of arguments
def multi_add(*args):
    result=0
    for x in args:
        result = result + x
    return result
print(multi_add(5,6,4,5,3,7))
'''You can combine a variable argument list with a set of formal arguments,
but just keep in mind that the variable argument list always has to be the last parameter.'''
