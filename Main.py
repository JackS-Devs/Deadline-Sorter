deadlines = [
    ("Math Homework", "2026-01-20"),
    ("Biology Exam", "2026-01-18"),
    ("Speech Outline", "2026-01-16"),
    ("Final Project", "2026-01-25")
]

deadlines.sort(key=lambda item: item[1])

print("Upcoming Deadlines:\n")

for name, date in deadlines:
    print(f"{date} — {name}")
