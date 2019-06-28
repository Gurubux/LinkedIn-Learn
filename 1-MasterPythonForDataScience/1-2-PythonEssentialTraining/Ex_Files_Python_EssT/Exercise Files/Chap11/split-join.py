#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s.split())
#['This', 'is', 'a', 'long', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it.']

print(s.split('a'))
#['This is ', ' long string with ', ' bunch of words in it.']

#Join takes in list argument and joints the list with the string character on which join is called
print("_".join(s.split('a')))