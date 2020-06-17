import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)  # convert string to int

start = time.time()

total_price = 0
length = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax
        length += 1

print(total_price)
print(length)
print('Duration: {} seconds'.format(time.time() - start))

# optimized code
start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))
