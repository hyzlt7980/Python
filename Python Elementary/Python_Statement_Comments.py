"""
This module explain the Python statement and comments
"""
# Python  Statement

#In Python.

#End of a statement is marked by a new line character.
#But we can make a statment extend over multiple lines
#with the line continuation character(\).

#For example
a=1+2+3\
   +4+5+6+\
   7+8+9
print(a)  # 45
print('a type: '+str(type(a)))

#The above is explicit line continuation
# We can also use (),[],{} 

# ()
b=(1+2+3+4
   +5+6+7+8
   +9)

print(b)  # 45
print('b type: '+str(type(b)))

# [], it is actually forming a list
c=[1+2+3+4
   +5+6+7+8
   +9]
print(c)  #[45]
print('c type: '+str(type(c)))

# {}, it is actuall forming a set
d={1+2+3+4
   +5+6+7+8
   +9}
print(d)  # {45}
print('d type: '+str(type(d)))

# [] with string 
colors = ['red'
          'blue'
          'green']
print(colors)
print('colors type: '+str(type(colors)))


# Comment
'''This is also a
perfect example of
multi-line comments'''
