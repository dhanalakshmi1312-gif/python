from datetime import datetime

d1 = datetime(2025, 1, 1, 10, 30, 00)
d2 = datetime(2025, 1, 2, 12, 40, 30)

diff = d2 - d1

days = diff.days
seconds = diff.seconds

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", secs)
