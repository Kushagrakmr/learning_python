import time
# g = (num for num in range(1, 34))

# k = sum(num for num in range(1,50))

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_stop = time.time() - gen_start_time
print(gen_stop)


list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_stop = time.time() - list_start_time
print(list_stop)