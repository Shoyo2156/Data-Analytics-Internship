import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Printer", "Keyboard", "Mouse"]
sales = [55000, 22000, 15000, 3000, 1000]

plt.bar(products, sales)

plt.title("Product Wise Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.savefig("charts/bar_chart.png", dpi=300, bbox_inches="tight")
plt.show()