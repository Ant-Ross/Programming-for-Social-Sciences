# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:46:18 2018

@author: ts16larp
"""

#TUESDAY 18/09/18
    
    
a = "Hey"
#Retrievinig the last element of the string
a[len(a)-1] 
a[-1]

#Strings are immutable, i.e. I can't change a single value in it.
#i.e, a[1] = 'a' is not allowed


#Concatenate strings by...
a = "Hey"
b = "You"
print(a+b)


# Tuples
# Tuples are indexed in the same way as strings

q = (1,2,3,4)
len(q)
q[1]

#Lists
g = [5,6,7,8]
print(len(g),g[1],g[-2])

# Lists are mutable

g[2] = 33
print(g)

# but you need to be careful 

a = [1,2,3]
b = a

# Now labels a nad b are both attached to the same list
b[0] = 100

#That list has its first element changed
# and both a and b lables are still attached, so
print(a)
# a has also changed


# Slices

a = [1,2,3,4,5,6,7,8,9]
a[2:6] # slicing 4 elements: position 2 up to 5 (last position is not included)
a[:6] # From the first position to 5
a[2:] # From the second to the last
a[:]# Slice of the whole list. An entirely separate object from the original

# Ranges

range(4,17,2)
# the range function makes an *iterable* (more later), here starting
# at 4, ending one number before 17, in steps of 2.


# Functions

def squared(x):
    x_squared = x**2
    return x_squared
# x is only defined within the function and not outside.

def pythagoras(a,b):
    c_squared = a**2+b**2
    return c_squared**0.5,c_squared


# Classes

class Rational:
    
    def __init__(self,a,b):
        
        self.__n = a
        self.__d = b
        
    def getNumerator(self):
        return self.__n
    
    def getDenominator(self):
        return self.__d
    
    def __mul__(self,rhs):
        
        a = self.__n * rhs.getNumerator()
        b = self.__d * rhs.getDenominator()
        return Rational(a,b)
        
    def __repr__(self):
        str = '%d' % self.__n
        str = str + '/'
        str = str + '%d' % self.__d
        return str
        




