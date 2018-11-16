import Python_Statement_Comments
'''
This module expalinexample of Docstring.
'''
#Docstring is short for documentation string.

# It is a string that occurs as the first statement in a module, function
# class, or method.  We must write a function/class does in the docstring

# Triple quptes are used while writing docstrings. For example
def double(num):
    '''Function to double the value'''
    return 2*num

# When we need the docstring of double function, we just print(double.__doc__)
# When we need the docstring of this module, we just need print(__doc__)

# If we import another module inside this module. See the top we import Python_Statement_Comments. We need print(Python_Statement_Comments.__doc__)
