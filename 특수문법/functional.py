# map : apply a function to the elements of a data structure
mp = list(map(lambda x: x**2, range(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 


# filter : selects the elements according to a conditional function
ft = list(filter(lambda x: x%2==0, range(10)))
# [0, 2, 4, 6, 8]


# reduce : apply a binary function to the elements to produce a single value
from functools import reduce
rd = reduce(lambda x,y: x+y, range(1,10+1))
# 55

print(f'{mp} /// {ft} /// {rd}')
