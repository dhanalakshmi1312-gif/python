from datetime import datetime, timedelta

today = datetime.now().date()
new_date = today - timedelta(days=5)

print("Current Date:", today)
print("5 days before Current Date:", new_date)
