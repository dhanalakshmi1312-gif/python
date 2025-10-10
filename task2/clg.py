year = int(input("Enter year (1-3): "))
semester = int(input("Enter semester (1-2): "))

if year == 1 and semester == 1:
    subjects = ["English", "criminal justice", "law", "society", "fingerprint"]
elif year == 1 and semester == 2:
    subjects = ["digital fs", "Dermatoglyphics", "", "Communicative english", "Computer"]
elif year == 2 and semester == 1:
    subjects = ["digitalcrime", "medical forensic", "chemistry", "tamil", "digitalcomputer"]
elif year == 2 and semester == 2:
    subjects = ["cyber", "fs", "AI Basics", "project", "laboratory"]
else:
    subjects = ["Semester not available"]

print("Subjects:", subjects)
