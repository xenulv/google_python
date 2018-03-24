#!/bin/env python

import sys

def hello(name):
  
  if name == 'Alice' or name == 'Nick':
    name = name + '???'
  else:
    DoesNotExist(name)
    print('Else')
  
  name = name + '!!!'
  print('Hello', name)

#in python each line is evaluated in the moment
# Python checks a line when it runs said line.
