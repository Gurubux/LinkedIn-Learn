#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = [x for x in seq if x % 3 != 0]
    seq4 = [(x,x * 2) for x in seq]
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    seq5 = {x : x * 2 for x in seq}
    print_dict(seq5)
    
    
def print_list(o):
    for x in o: print(x, end = ' ')
    print()
def print_dict(o):
    for k,v in o.items(): print(f"{k} : {v}")
    print()
if __name__ == '__main__': main()
