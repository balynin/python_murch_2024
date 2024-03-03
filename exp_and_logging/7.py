import random
import logging
logging.basicConfig(level=logging.INFO, filename="py_log7.log", filemode="w")

rand_list = []
n = 30
for i in range(n):
	rand_list.append(random.randint(0, 99))
print(sum(rand_list)/len(rand_list))