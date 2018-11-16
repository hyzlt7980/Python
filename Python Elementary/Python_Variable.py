import constant
'''
This module take about create variable in python
and Python variables and Memory Management

'''
# Assign multiple values to multiple variables
print('Variable part')
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

print()
# Assign same values to multiple variables

x=y=z='same'

print(x)
print(y)
print(z)
print()

'''--------------Variable and Memory Management--------------------'''
print('Memory part')

a=1
b=1

print(id(a),id(b))

# Why a,b has the same Id. That is because
# CPython implementation keeps an array of integer objects for all integers between -5 and 256. So when we create an integer in that range, they simply back reference to the existing object.
# Also, looks like,Emmmmm
# I guess when you initialize c=1000 and d=1000, they do not refer to same obejct in idle command line but refer to the same if you write them in a file is becuase that
# The compiler is smater when they compile you code from a file.
c=1000
print(id(c))
d=1000
print(str(c is d))
print(id(d))

a='fafafafafafafa'
b='fafafafafafafa'
print(a is b)
print(id(a),id(b))

'''---------------------Constant-------------------------------------'''
print()
print('Constant part')
print(constant.PI)
print(constant.GRAVITY)
