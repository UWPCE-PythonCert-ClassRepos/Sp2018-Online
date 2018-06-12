from calc import trap_int # regualr py 6.1sec
from calc1 import trap_int #cypthon 2.1 sec


from time import time

t_start = time()
for i in range(10000):
    answer = trap_int(start=0, stop=10, dx=0.01)

print(f'calculation took {time() - t_start} seconds.')