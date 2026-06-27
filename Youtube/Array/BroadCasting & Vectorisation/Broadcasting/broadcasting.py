import numpy as np

# Without broadcasting
# List
prices = [100,200,300,400,500]
discount = 10
final_prices = []
for price in prices:
    final_price = price - (price * discount/100)
    final_prices.append(final_price)
    
print(final_prices)

print() # for spacing
# With broadcasting
prices = np.array([100,200,300,400,500,600,700,800,900,1000])
discount = 10
final_price = prices - (prices * discount/100)
print(final_price)