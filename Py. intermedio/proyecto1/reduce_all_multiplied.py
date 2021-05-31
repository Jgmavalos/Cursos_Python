my_list = [2,2,2,2,2]


# Método 1

all_multiplied = 1

for i in my_list:
    all_multiplied *= i

print(all_multiplied)

# Método 2
from functools import reduce

all_multiplied = reduce[lambda a, b:a*b, my_list]

print(all_multiplied)

