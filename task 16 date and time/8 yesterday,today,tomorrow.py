from datetime import datetime, timedelta

today = datetime.now().date()

print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))
