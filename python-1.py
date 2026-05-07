log_data = [
    ("2023-10-26 10:00:00", "INFO", "User logged in"),
    ("2023-10-26 10:01:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:01:30", "INFO", "Data processed successfully"),
    ("2023-10-26 10:02:00", "WARN", "Low disk space"),
    ("2023-10-26 10:03:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:04:00", "INFO", "User logged out"),
    ("2023-10-26 10:05:00", "ERROR", "Null pointer exception"),
    ("2023-10-26 10:05:30", "DEBUG", "Debugging user session"),
]

error_logs = [log for log in log_data if log[1] == "ERROR"]
print("Task -1 Error Logs")
for log in error_logs:
    print(log)

db_fail_count = sum(1 for log in error_logs if log[2] == "Database connection failed")
print("Task -2 Number of Database Connection Failures:", db_fail_count)

first_warn = next((log for log in log_data if log[1] == "WARN"), None)

if first_warn:
    print(f"\nTask 3 - First WARN: timestamp={first_warn[0]}, message={first_warn[2]}")
else:
    print("\nTask 3 - No WARN log found.")

sorted_logs = sorted(log_data, key=lambda log: log[0])
print("\nTask 4 - Sorted Logs:")
for log in sorted_logs:
    print(log)

all_short = all(len(log[2]) < 100 for log in log_data)
has_critical = any(log[1] == "CRITICAL" for log in log_data)
print(f"\nTask 5 - All messages < 100 chars: {all_short}")
print(f"Task 5 - Any CRITICAL log: {has_critical}")

log_data.append(("2023-10-26 10:06:00", "INFO", "System check complete"))
print(f"\nTask 6 - log_data now has {len(log_data)} entries. Last entry: {log_data[-1]}")

