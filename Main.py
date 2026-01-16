deadlines = []

print("Welcome to Deadline Sorter")

while True:
    name = input("Enter assignment name (or type 'done'): ")

    if name.lower() == "done":
        break

    date = input("Enter due date (YYYY-MM-DD): ")
    deadlines.append((name, date))

deadlines.sort(key=lambda item: item[1])

print("\nUpcoming Deadlines:\n")

for name, date in deadlines:
    print(f"{date} — {name}")
if not deadlines:
    print("No deadlines entered.")
    exit()
