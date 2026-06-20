import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hr_data.csv")

# Employees by Department
dept_count = df["Department"].value_counts()

plt.figure(figsize=(6,4))
dept_count.plot(kind="bar")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("hr_chart.png")
plt.show()