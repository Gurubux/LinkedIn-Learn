#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

x= {"One":1,"Two":2}
for k in x:
    print('k is {}'.format(k))

for k,v in x.items():
    print(f'k is {k} and v i {v}')