#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')
x = "World"
y = "Morning"
print("Hello {}".format(x))
print("Hello {} {}".format(x,y))
print("Hello {a} {b}".format(a=x,b=y))
print("Hello {a} {b}  {a}  {a}".format(a=x,b=y))# >>> Hello World Morning  World  World
print("Hello {0:<20} {1:>20}".format(x,y))



print("{:,}".format(10000000000)) #10,000,000,000
print("{:_}".format(10000000000)) #10_000_000_000


print("{:f}".format(1231.8345812312)) #default 6  # 1231.834581
print("{:.3f}".format(1231.8345812312)) # 1231.835


print("{:d}".format(14))#14
print("{:f}".format(14))#14.000000
print("{:b}".format(14))#1110
print("{:o}".format(14))#16
print("{:X}".format(14))#E

print(f"{14:d}")#14
print(f"{14:f}")#14.000000
print(f"{14:b}")#1110
print(f"{14:o}")#16
print(f"{14:X}")#E