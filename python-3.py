tasks_definitions = [
    ("T1", "Compile Code", 1, []),
    ("T2", "Run Unit Tests", 2, ["T1"]),
    ("T3", "Generate Report", 3, ["T2"]),
    ("T4", "Deploy Artifacts", 2, ["T1"]),
    ("T5", "Urgent Patch", 0, []),
]

task_queue = list(tasks_definitions)
print("Task 1 - Initial Queue:")
for task in task_queue:
    print(task)

task_queue.sort(key=lambda t: (t[2], t[0]))
print("\nTask 2 - Sorted by Priority:")
for task in task_queue:
    print(task)

print("\nTask 3 - Processing Tasks:")
completed_tasks = []
skipped_tasks = []

while task_queue:
    task = task_queue.pop(0)
    task_id, description, priority, dependencies = task

    deps_met = all(dep in completed_tasks for dep in dependencies)

    if deps_met:
        print(f"  [PROCESSED] {task_id}: {description} (priority={priority})")
        completed_tasks.append(task_id)
    else:
        unmet = [d for d in dependencies if d not in completed_tasks]
        print(f"  [SKIPPED]   {task_id}: {description} — unmet deps: {unmet}")
        skipped_tasks.append(task)

if skipped_tasks:
    print(f"\n  Skipped tasks (unmet dependencies): {[t[0] for t in skipped_tasks]}")
print(f"  Completed order: {completed_tasks}")

print("\nTask 4 - Insert Emergency Task:")
emergency_task = ("T6", "Emergency DB Backup", 0, [])
task_queue = list(tasks_definitions)
task_queue.insert(0, emergency_task)
print(f"  Inserted {emergency_task[0]} at index 0.")
print(f"  Queue front: {task_queue[0]}")

print("\nTask 5 - Reverse Order Processing:")
task_queue = list(tasks_definitions)
task_queue.sort(key=lambda t: (t[2], t[0]))  
task_queue.reverse()                           

print("  Queue after sort + reverse (pop() from end = highest priority first):")
while task_queue:
    task = task_queue.pop()
    print(f"  [POPPED] {task[0]}: {task[1]} (priority={task[2]})")

print("\nTask 6 - Priority Analysis:")
priorities = [t[2] for t in tasks_definitions]
print(f"  Min priority value : {min(priorities)}")
print(f"  Max priority value : {max(priorities)}")
print(f"  Sum of all priorities: {sum(priorities)}")

print("\nTask 7 - Remove T1 dependency from T4:")
updated_definitions = []
for task in tasks_definitions:
    task_id, description, priority, dependencies = task
    if task_id == "T4":
        new_deps = [d for d in dependencies if d != "T1"]
        updated_definitions.append((task_id, description, priority, new_deps))
    else:
        updated_definitions.append(task)

for task in updated_definitions:
    print(task)