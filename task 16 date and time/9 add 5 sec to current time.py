from datetime import datetime, timedelta

now = datetime.now()
new_time = now + timedelta(seconds=5)

print("Current Time:", now.time())
print("After 5 Seconds:", new_time.time())
