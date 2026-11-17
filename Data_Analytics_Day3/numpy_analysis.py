import numpy as np

sales = np.array([55000, 22000, 15000, 3000, 1000])

print("===== NUMPY SALES ANALYSIS =====")

print("Sales Data:", sales)
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))
print("Standard Deviation:", np.std(sales))