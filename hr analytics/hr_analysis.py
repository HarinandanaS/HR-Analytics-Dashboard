import pandas as pd

# Read CSV
df = pd.read_csv("hr_data.csv")

# Total Employees
total_employees = len(df)

# Average Salary
avg_salary = df["Salary"].mean()

# Attrition Count
attrition_count = len(df[df["Attrition"] == "Yes"])

# Department with most employees
top_department = df["Department"].value_counts().idxmax()

print("Total Employees:", total_employees)
print("Average Salary:", avg_salary)
print("Attrition Count:", attrition_count)
print("Top Department:", top_department)