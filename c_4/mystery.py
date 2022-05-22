""" MUTABLE(on the link/by reference) + IMMUTABLE(by value) 

If the variable refers to a mutable value, the semantics of passing an argument by reference apply.
If the data type referenced by the variable is immutable, the argument is passed by value.

Lists, dictionaries, and sets (being mutable) 
are always passed to a function by reference —
changes made to them inside the function are reflected in the calling code.

Strings, integers, and tuples (being immutable) are always passed to a function by value
—changes made to them inside the function are not reflected in the calling code. 
If the data type is immutable, then the function cannot change it.
"""
# 1 - from Roman = Roman's function Clearly showed that arguments are passed on value

def double(arg):
    print("Before:", arg)
    arg = arg * 2
    print("After:", arg)

num = 10
double(num)
print("1 attempt - integer: ", num)
print('--'*20)

saying = 'Hello '
double(saying)
print("2 attempt - string: ", saying)
print('--'*20)

numbers = [ 42, 256, 16 ]
double(numbers)
print("3 attempt - list: ", numbers)
print('--'*20)

# 2 - from Julia = Julia's function demonstrates transfer on the link

def change(arg):
   print("Before:", arg)
   arg.append("More data")
   print("After:", arg)
   
numbers = [ 42, 256, 16 ]
change(numbers)
print("3 attempt - list: ", numbers)   