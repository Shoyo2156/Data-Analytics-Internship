import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Printer", "Keyboard", "Mouse"]
sales = [55000, 22000, 15000, 3000, 1000]

plt.figure(figsize=(10, 7))

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.75,
    labeldistance=1.12,
    textprops={"fontsize": 10},
    explode=(0.05, 0, 0, 0.12, 0.18)
)

plt.title("Product Wise Sales Contribution", fontsize=16)
plt.tight_layout()
plt.savefig("charts/pie_chart.png", dpi=300, bbox_inches="tight")
plt.show()


# LINE CHART

months = ["Jan", "Feb", "Mar", "Apr", "May"]
monthly_sales = [12000, 18000, 15000, 25000, 30000]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    monthly_sales,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("charts/line_chart.png", dpi=300, bbox_inches="tight")
plt.show()