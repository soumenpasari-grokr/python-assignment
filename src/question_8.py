import math

get_square_number = lambda a : math.pow(a,2)

list_one = map(get_square_number,range(1,21))

print(list(list_one))