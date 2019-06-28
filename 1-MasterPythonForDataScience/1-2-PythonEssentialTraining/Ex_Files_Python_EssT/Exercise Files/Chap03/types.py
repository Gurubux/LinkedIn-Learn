#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 'seven'.upper()
print('x is {}'.format(x))

a=8
b=9
print(f"x is {a:<010} and  {b:>010}")

x = 8//9
print(x,type(x))


x = .1+.1+.1-.3
print(x,type(x))

from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a+a+a-b
print(x,type(x))

x = False
print(x,type(x))
if x :
    print("True" )
else: 
    print("False" )
x = 0
print(x,type(x))
if x :
    print("True" )
else: 
    print("False" )
x = None
print(x,type(x))
if x :
    print("True" )
else: 
    print("False" )
    
x = ""
print(x,type(x))
if x :
    print("True" )
else: 
    print("False" )    
a='type And Id'
print("-"*5,a,"-"*5)
a = (1, "Two", {"Three":3})
b = (1, "Two", {"Three":3})
print(a is b)
print(a[0] is b[0])


print(isinstance(a,tuple))
print(isinstance(a,list))
