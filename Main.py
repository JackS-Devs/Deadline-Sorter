from datetime import datetime

deadlines = []

print("\n📅 Welcome to Deadline Sorter\n")

def get_valid_date():
    while True:
        date_input = input("Enter due date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

while True:
    name = input("Enter assignment name (or type 'done'): ")

    if name.lower() == "done":
        break

    date = get_valid_date()
    deadlines.append((name, date))

if not deadlines:
    print("No deadlines entered.")
    exit()

deadlines.sort(key=lambda item: item[1])

print("\nUpcoming Deadlines:\n")

for name, date in deadlines:
    print(f"{date} — {name}")

