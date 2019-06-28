#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')
    puppy(10,3)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')
    
def puppy(a,b=2,c=True):
    if c:
        print('a+b = ',a+b)
    else: print('Meow.')
if __name__ == '__main__': main()
