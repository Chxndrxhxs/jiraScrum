employees = [
    (1001, "Alice Johnson", "Sales", 15000, 4.2),
    (1002, "Bob Smith", "Sales", 12000, 3.8),
    (1003, "Carol Davis", "Marketing", 8000, 4.5),
    (1004, "David Brown", "Sales", 18000, 4.0),
    (1005, "Eva Wilson", "Marketing", 9500, 3.2),
    (1006, "Frank Miller", "IT", 11000, 3.9),
    (1007, "Grace Lee", "Sales", 13500, 2.1),
    (1008, "Henry Taylor", "IT", 10500, 4.1),
    (1009, "Ivy Chen", "Marketing", 7800, 3.7),
    (1010, "Jack Davis", "IT", 12500, 3.5)
]

departments = {}
for emp in employees:
    dept = emp[2]
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp)

print("Top 3 Performers by Department:")
for dept, emps in departments.items():
    sorted_emps = sorted(emps, key=lambda e: e[3], reverse=True)
    print(f"\n  {dept} Department:")
    for rank, emp in enumerate(sorted_emps[:3], 1):
        print(f"    {rank}. {emp[1]}: ${emp[3]}")

print("\nDepartment Average Ratings:")
for dept, emps in departments.items():
    avg_rating = sum(e[4] for e in emps) / len(emps)
    print(f"  {dept}: {avg_rating:.2f}")

print("\nEmployees Needing Improvement (Rating < 3.0):")
needs_improvement = [e for e in employees if e[4] < 3.0]
if needs_improvement:
    for emp in needs_improvement:
        print(f"  {emp[1]} ({emp[2]}): Rating {emp[4]}")
else:
    print("  None")

print("\nPerformance Ranking (Sales x Rating):")
ranked = sorted(employees, key=lambda e: e[3] * e[4], reverse=True)
for rank, emp in enumerate(ranked, 1):
    score = emp[3] * emp[4]
    print(f"  {rank}. {emp[1]}: {score}")

print("\nDepartment Performance Summary:")
for dept, emps in departments.items():
    count = len(emps)
    avg_sales = sum(e[3] for e in emps) / count
    avg_rating = sum(e[4] for e in emps) / count
    print(f"  {dept}: {count} employees, Avg Sales: ${avg_sales:.2f}, Avg Rating: {avg_rating:.2f}")