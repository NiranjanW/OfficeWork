from functools import partial
import re
import os
from pathlib import Path

def multiplier (x,y):
    return x*y

double = partial(multiplier, y=2)
triple = partial(multiplier, y=3)

print(double(4), triple(4))

def partialMoc(func , *parargs):
    def wrapper(*extraargs):
         args = list(parargs)
         args.extend(extraargs)

         return func(*args)

    return wrapper()

is_spaced_apart = partial(re.search, '[a-zA-Z]\s\=')
is_grouped_together = partial(re.search, '[a-zA-Z]\=')





dirname  = os.path.abspath(__file__)
file = os.path.join(dirname, 'test.txt')
suffix ='.csv'
Path(dirname,file).with_suffix(suffix)

with open(file) as handle:
    lines = [line.strip() for line in handle]
for text in lines:
    if is_grouped_together(text):
        pass
    elif is_spaced_apart(text):
        pass
    else:
       pass