employee_data = [
    (101, "Alice Smith", "Engineering", 90000, 5),
    (102, "Bob Johnson", "Marketing", 75000, 3),
    (103, "Charlie Brown", "Engineering", 120000, 8),
    (104, "Diana Prince", "HR", 65000, 2),
    (105, "Edward King", "Marketing", 80000, 5),
    (106, "Frank Castle", "Engineering", 95000, 0),
]

sorted_by_salary = sorted(employee_data, key=lambda emp: emp[3], reverse=True)
print("Task 1 - Sorted by Salary (descending):")
for emp in sorted_by_salary:
    print(emp)

sorted_by_service_name = sorted(employee_data, key=lambda emp: (-emp[4], emp[1]))
print("\nTask 2 - Sorted by Years of Service (desc), then Name (asc):")
for emp in sorted_by_service_name:
    print(emp)

salaries = [emp[3] for emp in employee_data]
years = [emp[4] for emp in employee_data]

total_salary = sum(salaries)
min_salary = min(salaries)
max_salary = max(salaries)
avg_years = sum(years) / len(years)

print(f"\nTask 3 - Statistics:")
print(f"  Total salary expenditure: ${total_salary:,}")
print(f"  Minimum salary: ${min_salary:,}")
print(f"  Maximum salary: ${max_salary:,}")
print(f"  Average years of service: {avg_years:.2f}")

high_earners = [emp[1] for emp in employee_data if emp[3] > 90000]
print(f"\nTask 4 - High Earners (>$90,000): {high_earners}")

index_to_remove = next((i for i, emp in enumerate(employee_data) if emp[0] == 104),None)
del employee_data[index_to_remove]
print(f"\nTask 5 - Employee 104 removed. Remaining records:")
for emp in employee_data:
    print(emp)

all_experienced = all(emp[4] >= 1 for emp in employee_data)
any_low_paid_engineer = any(emp[3] < 70000 for emp in employee_data if emp[2] == "Engineering")

print(f"\nTask 6 - Validation Checks:")
print(f"  All employees have at least 1 year of service: {all_experienced}")
print(f"  Any Engineer earns less than $70,000: {any_low_paid_engineer}")